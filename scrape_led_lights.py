#!/usr/bin/env python3
"""
Script to scrape LED light data from sst-smartware.com
Parses product listing page, then visits each product detail page to extract:
- name
- description
- images (from swiper-slide rel attribute)
- table data

Output: JSON grouped by category name (from main-class-item classify active)
"""

import requests
from bs4 import BeautifulSoup
import json
import time
import re
import random
from urllib.parse import urljoin

# Try to import Selenium for JavaScript-rendered pages
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options as ChromeOptions
    from selenium.webdriver.firefox.options import Options as FirefoxOptions
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.firefox.service import Service as FirefoxService
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    SELENIUM_AVAILABLE = True
    SELENIUM_BROWSER = None  # Will be set to 'chrome' or 'firefox'
except ImportError:
    SELENIUM_AVAILABLE = False
    print("Note: Selenium not installed. Run: pip install selenium")

BASE_URL = "https://sst-smartware.com"
LISTING_URLS = [
    "https://sst-smartware.com/Product/639505.html",
    "https://sst-smartware.com/Product/639505.html?PageNo=2&ClassID=639505&responseModuleId=672112394",
    "https://sst-smartware.com/Product/639513.html",
    "https://sst-smartware.com/Product/639513.html?PageNo=2&ClassID=639513&responseModuleId=672112394",
    "https://sst-smartware.com/Product/639513.html?PageNo=3&ClassID=639513&responseModuleId=672112394",
    "https://sst-smartware.com/Product/639456.html",
    "https://sst-smartware.com/Product/639515.html",
    "https://sst-smartware.com/Product/639515.html?PageNo=2&ClassID=639515&responseModuleId=672112394",
    "https://sst-smartware.com/Product/639521.html",
    "https://sst-smartware.com/Product/639521.html?PageNo=2&ClassID=639521&responseModuleId=672112394",
]

# Create a session to maintain cookies
session = requests.Session()
session.last_html = None  # Store last HTML for CSRF token extraction
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': BASE_URL,
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'X-Requested-With': 'XMLHttpRequest',  # Helps bypass some CSRF checks
})


def fetch_html(url, delay_range=(5, 10), use_csrf=True):
    """Fetch HTML content from a URL with session handling and random delays."""
    sleep_time = random.uniform(delay_range[0], delay_range[1])
    time.sleep(sleep_time)
    
    # Try requests first with CSRF handling
    for attempt in range(2):
        # Extract and update CSRF token before request
        if use_csrf and hasattr(session, 'last_html') and session.last_html:
            csrf_token = extract_csrf_token(session.last_html)
            if csrf_token:
                # Try different header names the server might expect
                session.headers.update({
                    'X-CSRF-Token': csrf_token,
                    'X-Csrf-Token': csrf_token,
                    'X-xsrf-token': csrf_token,
                    'X-XSRF-TOKEN': csrf_token,
                })
        
        try:
            response = session.get(url, timeout=30)
            if response.status_code == 403:
                print(f"  403 Forbidden - trying cookie token...")
                # Try token from cookies
                cookies = session.cookies.get_dict()
                for cookie_name in ['csrfToken', 'csrf_token', '_csrf', 'xsrf', 'XSRF-TOKEN']:
                    if cookie_name in cookies:
                        session.headers.update({'X-CSRF-Token': cookies[cookie_name]})
                        break
                continue
            
            response.raise_for_status()
            session.last_html = response.text
            return response.text
        except requests.RequestException as e:
            if attempt < 1 and ('403' in str(e) or 'Forbidden' in str(e)):
                print(f"  Attempt {attempt + 1} failed, retrying...")
                time.sleep(2)
                continue
            print(f"  Requests failed: {e}")
            break
    
    # Fallback to Selenium if available
    if SELENIUM_AVAILABLE:
        print(f"  Falling back to Selenium for: {url}")
        return fetch_with_selenium(url, delay_range)
    
    print(f"Error fetching {url}")
    return None


def extract_csrf_token(html, debug=False):
    """Extract CSRF token from HTML page (meta tags, hidden inputs, or data attributes)."""
    if not html:
        return None
    
    soup = BeautifulSoup(html, 'html.parser')
    found_tokens = []
    
    # Method 1: Look for meta tag with CSRF token
    meta_token = soup.find('meta', {'name': re.compile(r'csrf-token|csrftoken|xsrf-token', re.I)})
    if meta_token and meta_token.get('content'):
        found_tokens.append(('meta-name', meta_token['content']))
    
    # Method 2: Look for meta tag with property (some sites use this)
    meta_property = soup.find('meta', {'property': re.compile(r'csrf-token|csrftoken', re.I)})
    if meta_property and meta_property.get('content'):
        found_tokens.append(('meta-property', meta_property['content']))
    
    # Method 3: Look for meta http-equiv (some sites use this)
    meta_equiv = soup.find('meta', {'http-equiv': re.compile(r'csrf|csrf-token', re.I)})
    if meta_equiv and meta_equiv.get('content'):
        found_tokens.append(('meta-http-equiv', meta_equiv['content']))
    
    # Method 4: Look for hidden input with CSRF token
    hidden_input = soup.find('input', {'type': 'hidden', 'name': re.compile(r'csrf|_token|csrf_token|csrftoken|xsrf', re.I)})
    if hidden_input and hidden_input.get('value'):
        found_tokens.append(('hidden-input', hidden_input['value']))
    
    # Method 5: Look for ANY hidden input with value that looks like a token
    for inp in soup.find_all('input', {'type': 'hidden'}):
        val = inp.get('value', '')
        if len(val) > 20 and re.match(r'^[a-zA-Z0-9_-]+$', val):
            found_tokens.append(('hidden-generic', val))
    
    # Method 6: Look for data-* attributes containing csrf
    data_inputs = soup.find_all('input', {'data-csrf': True})
    if data_inputs:
        found_tokens.append(('data-attr', data_inputs[0].get('data-csrf')))
    
    # Method 7: Look in script tags for token assignments
    scripts = soup.find_all('script')
    for script in scripts:
        script_text = script.string or ''
        # Match various patterns: csrfToken, CSRF_TOKEN, csrf_token, etc.
        match = re.search(r'(?:csrf[_-]?token|xsrf[_-]?token)\s*[:=]\s*["\']([^"\']{10,})["\']', script_text, re.I)
        if match:
            found_tokens.append(('script', match.group(1)))
        
        # Also try to find base64-like tokens
        match2 = re.search(r'token["\']?\s*[:=]\s*["\']([A-Za-z0-9+/=]{20,})["\']', script_text)
        if match2:
            found_tokens.append(('script-base64', match2.group(1)))
    
    if debug and found_tokens:
        print(f"  Found {len(found_tokens)} potential tokens")
        for src, tok in found_tokens[:3]:
            print(f"    {src}: {tok[:30]}...")
    
    # Return the first valid-looking token
    if found_tokens:
        return found_tokens[0][1]
    
    return None


def extract_form_token(html, form_action_url=None):
    """Extract tokens from forms that may be needed for subsequent requests."""
    if not html:
        return {}
    
    soup = BeautifulSoup(html, 'html.parser')
    tokens = {}
    
    # Find all hidden inputs
    hidden_inputs = soup.find_all('input', {'type': 'hidden'})
    for inp in hidden_inputs:
        name = inp.get('name')
        value = inp.get('value', '')
        if name and value:
            tokens[name] = value
    
    # Find forms and extract action URL
    if form_action_url:
        forms = soup.find_all('form')
        for form in forms:
            action = form.get('action', '')
            full_action = urljoin(BASE_URL, action) if not action.startswith('http') else action
            if form_action_url in full_action:
                inputs = form.find_all('input', {'type': 'hidden'})
                for inp in inputs:
                    name = inp.get('name')
                    value = inp.get('value', '')
                    if name:
                        tokens[name] = value
    
    return tokens


def post_with_csrf(url, data=None, delay_range=(5, 10)):
    """Make a POST request with CSRF token handling."""
    sleep_time = random.uniform(delay_range[0], delay_range[1])
    time.sleep(sleep_time)
    
    # Get CSRF token from session's last HTML
    if hasattr(session, 'last_html'):
        csrf_token = extract_csrf_token(session.last_html)
        if csrf_token:
            session.headers.update({'X-CSRF-Token': csrf_token})
    
    # Also try to get token from existing cookies
    cookies = session.cookies.get_dict()
    if 'csrf_token' in cookies:
        session.headers.update({'X-CSRF-Token': cookies['csrf_token']})
    elif '_csrf' in cookies:
        session.headers.update({'X-CSRF-Token': cookies['_csrf']})
    
    try:
        response = session.post(url, data=data, timeout=30)
        response.raise_for_status()
        session.last_html = response.text
        return response
    except requests.RequestException as e:
        print(f"Error POSTing to {url}: {e}")
        return None


def get_category_name(html):
    """Extract category name from the active menu item."""
    soup = BeautifulSoup(html, 'html.parser')
    
    # Look for the active classification element
    active_item = soup.find(class_='main-class-item classify active')
    if active_item:
        anchor = active_item.find('a')
        if anchor:
            return anchor.get_text(strip=True)
    
    # Fallback: try to get from page title or h1
    h1 = soup.find('h1')
    if h1:
        return h1.get_text(strip=True)
    
    title = soup.find('title')
    if title:
        title_text = title.get_text(strip=True)
        if '-' in title_text:
            return title_text.split('-')[0].strip()
        return title_text
    
    return None


def get_product_links(html):
    """Extract product links from listing page."""
    soup = BeautifulSoup(html, 'html.parser')
    products = []
    product_items = soup.find_all(class_=re.compile(r'pro-item\s+col-xs-2'))
    print(f"Found {len(product_items)} product items on listing page")
    
    for item in product_items:
        link_tag = item.find('a', href=True)
        if link_tag:
            href = link_tag['href']
            if href.startswith('/'):
                href = BASE_URL + href
            elif not href.startswith('http'):
                href = BASE_URL + '/' + href
            
            name_tag = item.find(class_='pro-name') or item.find('h3') or item.find('h4')
            name = name_tag.get_text(strip=True) if name_tag else None
            
            products.append({'url': href, 'name_from_listing': name})
    
    return products


def parse_product_detail(html, product_url):
    """Parse product detail page HTML."""
    soup = BeautifulSoup(html, 'html.parser')
    data = {'name': None, 'description': None, 'images': [], 'table_data': {}}
    
    # Extract product name
    name_selectors = ['h1.product-title', 'h1.pro-title', '.product-name h1', '.pro-detail h1', 'h1', '.product-info h2', '.pro-info h3']
    for selector in name_selectors:
        name_elem = soup.select_one(selector)
        if name_elem:
            data['name'] = name_elem.get_text(strip=True)
            break
    
    # Extract description
    desc_selectors = ['.product-description', '.pro-description', '.product-detail', '.pro-detail', '.description', '[class*="desc"]']
    for selector in desc_selectors:
        desc_elem = soup.select_one(selector)
        if desc_elem:
            desc_text = ' '.join(desc_elem.get_text(separator=' ', strip=True).split())
            # Clean up multiple dashes and repeated hyphens
            desc_text = re.sub(r'-{2,}', '', desc_text)  # Remove 2 or more consecutive dashes
            desc_text = re.sub(r'\s+', ' ', desc_text)   # Normalize whitespace
            desc_text = desc_text.strip()
            if len(desc_text) > 20:
                data['description'] = desc_text
                break
    
    # Extract images from swiper-slide rel attribute
    swiper_slides = soup.find_all(class_='swiper-slide')
    for slide in swiper_slides:
        rel_attr = slide.get('rel')
        if rel_attr:
            if rel_attr.startswith('/'):
                rel_attr = BASE_URL + rel_attr
            elif not rel_attr.startswith('http'):
                rel_attr = BASE_URL + '/' + rel_attr
            data['images'].append(rel_attr)
        else:
            img = slide.find('img')
            if img:
                src = img.get('src') or img.get('data-src')
                if src:
                    if src.startswith('/'):
                        src = BASE_URL + src
                    elif not src.startswith('http'):
                        src = BASE_URL + '/' + src
                    data['images'].append(src)
    
    # Fallback image selectors
    if not data['images']:
        img_selectors = ['.product-gallery img', '.pro-gallery img', '.product-image img', '.gallery img', '.zoompic img']
        for selector in img_selectors:
            imgs = soup.select(selector)
            for img in imgs:
                src = img.get('src') or img.get('data-src') or img.get('data-original')
                if src:
                    if src.startswith('/'):
                        src = BASE_URL + src
                    elif not src.startswith('http'):
                        src = BASE_URL + '/' + src
                    if src not in data['images']:
                        data['images'].append(src)
    
    # Extract table data
    tables = soup.find_all('table')
    for table in tables:
        rows = table.find_all('tr')
        for row in rows:
            cells = row.find_all(['td', 'th'])
            if len(cells) >= 2:
                key = cells[0].get_text(strip=True)
                value = cells[1].get_text(strip=True)
                if key and value:
                    data['table_data'][key] = value
    
    # Also try definition lists
    dl_elements = soup.find_all('dl')
    for dl in dl_elements:
        dt = dl.find('dt')
        dd = dl.find('dd')
        if dt and dd:
            key = dt.get_text(strip=True)
            value = dd.get_text(strip=True)
            if key and value:
                data['table_data'][key] = value
    
    return data


def process_listing_url(listing_url, all_products_data=None, page_count=1):
    """Process a single listing URL and return its category name and products.
    Handles pagination by checking for page-more class."""
    print(f"\n{'=' * 60}")
    print(f"Processing listing: {listing_url} (page {page_count})")
    print(f"{'=' * 60}")
    
    if all_products_data is None:
        all_products_data = []
    
    listing_html = fetch_html(listing_url, delay_range=(3, 6))
    if not listing_html:
        print(f"Failed to fetch listing page: {listing_url}")
        return None, all_products_data
    
    # Get category name only on first page
    if page_count == 1:
        category_name = get_category_name(listing_html)
        if category_name:
            print(f"Category: {category_name}")
        else:
            category_name = listing_url
    else:
        # Use stored category name for subsequent pages
        category_name = listing_url
    
    products = get_product_links(listing_html)
    print(f"Found {len(products)} products on page {page_count}")
    
    if not products:
        print("No products found. The page structure may have changed.")
        return category_name if page_count == 1 else None, all_products_data
    
    if page_count == 1:
        for i, p in enumerate(products[:5], 1):
            print(f"  {i}. {p['name_from_listing'] or 'Unknown'}")
        if len(products) > 5:
            print(f"  ... and {len(products) - 5} more")
    
    print(f"\nScraping product details from page {page_count}...")
    
    for i, product in enumerate(products, 1):
        print(f"  Processing {i}/{len(products)}: {product['url']}")
        product_html = fetch_html(product['url'], delay_range=(4, 8))
        if product_html:
            detail_data = parse_product_detail(product_html, product['url'])
            detail_data['source_url'] = product['url']
            if not detail_data['name']:
                detail_data['name'] = product['name_from_listing']
            all_products_data.append(detail_data)
        else:
            print(f"    Failed to fetch product page")
    
    return category_name if page_count == 1 else None, all_products_data


def get_selenium_driver():
    """Create a headless driver for JavaScript rendering (Chrome, Brave, or Firefox)."""
    if not SELENIUM_AVAILABLE:
        return None, None
    
    # Try Chrome first
    chrome_options = ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
    
    try:
        driver = webdriver.Chrome(options=chrome_options)
        print("  Using Chrome for Selenium")
        return driver, 'chrome'
    except Exception as e:
        print(f"  Chrome not available: {e}")
    
    # Try Brave
    brave_options = ChromeOptions()
    brave_options.add_argument('--headless')
    brave_options.add_argument('--no-sandbox')
    brave_options.add_argument('--disable-dev-shm-usage')
    brave_options.add_argument('--disable-gpu')
    brave_options.add_argument('--window-size=1920,1080')
    brave_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
    brave_options.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
    
    try:
        driver = webdriver.Chrome(options=brave_options)
        print("  Using Brave Browser for Selenium")
        return driver, 'brave'
    except Exception as e:
        print(f"  Brave not available: {e}")
    
    # Try Firefox
    firefox_options = FirefoxOptions()
    firefox_options.add_argument('--headless')
    firefox_options.add_argument('--width=1920')
    firefox_options.add_argument('--height=1080')
    
    try:
        driver = webdriver.Firefox(options=firefox_options)
        print("  Using Firefox for Selenium")
        return driver, 'firefox'
    except Exception as e:
        print(f"  Firefox not available: {e}")
        return None, None


def fetch_with_selenium(url, delay_range=(3, 5)):
    """Fetch page using Selenium (JavaScript rendering)."""
    if not SELENIUM_AVAILABLE:
        return None
    
    driver, browser = get_selenium_driver()
    if not driver:
        print(f"  No browser available for Selenium")
        return None
    
    print(f"  [Selenium/{browser}] Fetching: {url}")
    
    try:
        driver.get(url)
        time.sleep(random.uniform(delay_range[0], delay_range[1]))
        
        # Wait for page to load
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        
        html = driver.page_source
        driver.quit()
        return html
    except Exception as e:
        print(f"  [Selenium] Error: {e}")
        try:
            driver.quit()
        except:
            pass
        return None


def test_site_connection():
    """Test connection and debug CSRF token extraction."""
    print("\n" + "=" * 60)
    print("Testing site connection and CSRF handling...")
    print("=" * 60)
    
    try:
        response = session.get(BASE_URL + '/', timeout=30)
        print(f"Status: {response.status_code}")
        print(f"Cookies: {dict(session.cookies)}")
        
        csrf = extract_csrf_token(response.text, debug=True)
        if csrf:
            print(f"Extracted CSRF token: {csrf[:50]}...")
            session.last_html = response.text
            return True
        else:
            # Save sample of HTML for debugging
            print("\nNo token found. Saving HTML sample for analysis...")
            with open('debug_page_sample.html', 'w', encoding='utf-8') as f:
                f.write(response.text[:5000])
            print("  Saved first 5000 chars to debug_page_sample.html")
            session.last_html = response.text
            return False
    except Exception as e:
        print(f"Connection error: {e}")
        return False


def main():
    print("=" * 60)
    print("LED Light Data Scraper")
    print("=" * 60)
    print("\nNote: This site has CSRF protection. Using token extraction.")
    print("=" * 60)
    
    # Test connection first
    if not test_site_connection():
        print("\n⚠️  Warning: Could not extract CSRF token from initial page.")
        print("   The site may require JavaScript rendering (Selenium).")
        print("   Trying anyway with standard requests...")
    
    time.sleep(2)
    
    # Process each listing URL and group results by category name
    grouped_results = {}
    total_products = 0
    
    for listing_url in LISTING_URLS:
        category_name, products = process_listing_url(listing_url)
        if category_name:
            grouped_results[category_name] = products
        else:
            grouped_results[listing_url] = products
        total_products += len(products)
        time.sleep(10)  # Long delay between listing pages
    
    # Save results
    output_file = 'led_lights_data.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(grouped_results, f, indent=2, ensure_ascii=False)
    
    print(f"\n{'=' * 60}")
    print(f"Scraping complete!")
    print(f"Total listing URLs processed: {len(LISTING_URLS)}")
    print(f"Total products scraped: {total_products}")
    print(f"Data saved to: {output_file}")
    print(f"{'=' * 60}")
    
    print("\nSummary by category:")
    for category, products in grouped_results.items():
        print(f"  {category}: {len(products)} products")
    
    print("\nSample output (first product from first category):")
    if grouped_results:
        first_category = list(grouped_results.values())[0]
        if first_category:
            sample = first_category[0]
            print(json.dumps(sample, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
