#!/usr/bin/env python3
"""
Script to scrape LED light data from sst-smartware.com
Parses product listing page, then visits each product detail page to extract:
- name
- description
- images (from swiper-slide rel attribute)
- table data
"""

import requests
from bs4 import BeautifulSoup
import json
import time
import re
import random

BASE_URL = "https://sst-smartware.com"
LISTING_URLS = [
    "https://sst-smartware.com/Product/639505.html",
    "https://sst-smartware.com/Product/639513.html",
    "https://sst-smartware.com/Product/639456.html",
    "https://sst-smartware.com/Product/639515.html",
    "https://sst-smartware.com/Product/639521.html",
]

# Create a session to maintain cookies and CSRF tokens
session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': BASE_URL,
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
})


def init_session():
    """Initialize session by visiting homepage to get cookies."""
    try:
        print("Initializing session...")
        response = session.get(BASE_URL, timeout=30)
        response.raise_for_status()
        time.sleep(3)
        print(f"Session initialized. Cookies: {dict(session.cookies)}")
        return True
    except Exception as e:
        print(f"Failed to initialize session: {e}")
        return False


def fetch_html(url, delay_range=(4, 8)):
    """Fetch HTML content from a URL with session handling and random delays."""
    sleep_time = random.uniform(delay_range[0], delay_range[1])
    time.sleep(sleep_time)
    
    try:
        response = session.get(url, timeout=30)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None


def get_category_name(html):
    """Extract category name from the active menu item."""
    soup = BeautifulSoup(html, 'html.parser')
    
    active_item = soup.find(class_='main-class-item classify active')
    if active_item:
        anchor = active_item.find('a')
        if anchor:
            return anchor.get_text(strip=True)
    
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
    soup = BeautifulSoup(html, 'html.parser')
    data = {'name': None, 'description': None, 'images': [], 'table_data': {}}
    
    name_selectors = ['h1.product-title', 'h1.pro-title', '.product-name h1', '.pro-detail h1', 'h1', '.product-info h2', '.pro-info h3']
    for selector in name_selectors:
        name_elem = soup.select_one(selector)
        if name_elem:
            data['name'] = name_elem.get_text(strip=True)
            break
    
    desc_selectors = ['.product-description', '.pro-description', '.product-detail', '.pro-detail', '.description', '[class*="desc"]']
    for selector in desc_selectors:
        desc_elem = soup.select_one(selector)
        if desc_elem:
            desc_text = ' '.join(desc_elem.get_text(separator=' ', strip=True).split())
            if len(desc_text) > 20:
                data['description'] = desc_text
                break
    
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


def process_listing_url(listing_url):
    """Process a single listing URL and return its category name and products."""
    print(f"\n{'=' * 60}")
    print(f"Processing listing: {listing_url}")
    print(f"{'=' * 60}")
    
    listing_html = fetch_html(listing_url)
    if not listing_html:
        print(f"Failed to fetch listing page: {listing_url}")
        return None, []
    
    category_name = get_category_name(listing_html)
    if category_name:
        print(f"Category: {category_name}")
    else:
        category_name = listing_url
    
    products = get_product_links(listing_html)
    print(f"Found {len(products)} products")
    
    if not products:
        print("No products found. The page structure may have changed.")
        return category_name, []
    
    for i, p in enumerate(products[:5], 1):
        print(f"  {i}. {p['name_from_listing'] or 'Unknown'}")
    if len(products) > 5:
        print(f"  ... and {len(products) - 5} more")
    
    print(f"\nScraping product details...")
    all_products_data = []
    
    for i, product in enumerate(products, 1):
        print(f"  Processing {i}/{len(products)}: {product['url']}")
        product_html = fetch_html(product['url'])
        if product_html:
            detail_data = parse_product_detail(product_html, product['url'])
            detail_data['source_url'] = product['url']
            if not detail_data['name']:
                detail_data['name'] = product['name_from_listing']
            all_products_data.append(detail_data)
        else:
            print(f"    Failed to fetch product page")
    
    return category_name, all_products_data


def main():
    print("=" * 60)
    print("LED Light Data Scraper - Multiple Categories")
    print("=" * 60)
    
    # Initialize session first
    if not init_session():
        print("Warning: Session initialization failed, continuing anyway...")
    
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
