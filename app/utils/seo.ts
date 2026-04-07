/**
 * SEO Configuration for PowerHouse Industrial Lighting
 */

// Site-wide SEO configuration
export const siteConfig = {
  title: 'PowerHouse Industrial Lighting',
  description: 'Industrial LED Lighting Solutions with Factory-Direct Pricing and North American Support. High-performance LED Tripods, Light Bars, and Work Lights engineered in Shenzhen and managed from Toronto.',
  keywords: 'industrial LED lighting, LED tripods, light bars, work lights, factory-direct pricing, North American support, Shenzhen manufacturing, Toronto office, industrial lighting solutions',
  url: 'https://powerhouse-lighting.com',
  ogImage: '/og-image.png',
  twitterHandle: '@powerhouselighting',
}

// Helper function to generate SEO meta tags
export const generateSeoMeta = (pageSeo: {
  title?: string
  description?: string
  keywords?: string
  image?: string
  url?: string
}) => {
  const title = pageSeo.title ? `${pageSeo.title} | ${siteConfig.title}` : siteConfig.title
  const description = pageSeo.description || siteConfig.description
  const keywords = pageSeo.keywords || siteConfig.keywords
  const image = pageSeo.image || siteConfig.ogImage
  const url = pageSeo.url || siteConfig.url

  return {
    title,
    meta: [
      // Basic meta tags
      { name: 'description', content: description },
      { name: 'keywords', content: keywords },
      { name: 'author', content: siteConfig.title },

      // Open Graph / Facebook
      { property: 'og:type', content: 'website' },
      { property: 'og:url', content: url },
      { property: 'og:title', content: title },
      { property: 'og:description', content: description },
      { property: 'og:image', content: image },
      { property: 'og:site_name', content: siteConfig.title },

      // Twitter
      { name: 'twitter:card', content: 'summary_large_image' },
      { name: 'twitter:url', content: url },
      { name: 'twitter:title', content: title },
      { name: 'twitter:description', content: description },
      { name: 'twitter:image', content: image },
      { name: 'twitter:creator', content: siteConfig.twitterHandle },

      // Additional SEO
      { name: 'robots', content: 'index, follow' },
      { name: 'googlebot', content: 'index, follow' },
      { name: 'language', content: 'English' },
      { name: 'revisit-after', content: '7 days' },
    ],
    link: [
      { rel: 'canonical', href: url },
    ],
    script: [
      {
        type: 'application/ld+json',
        children: JSON.stringify({
          '@context': 'https://schema.org',
          '@type': 'Organization',
          name: siteConfig.title,
          description: siteConfig.description,
          url: siteConfig.url,
          logo: `${siteConfig.url}/logo.png`,
          sameAs: [
            'https://twitter.com/powerhouselighting',
            'https://linkedin.com/company/powerhouse-lighting',
          ],
          contactPoint: {
            '@type': 'ContactPoint',
            telephone: '+1-XXX-XXX-XXXX',
            contactType: 'sales',
            areaServed: 'US,CA',
            availableLanguage: 'English',
          },
          address: {
            '@type': 'PostalAddress',
            addressLocality: 'Toronto',
            addressRegion: 'ON',
            addressCountry: 'CA',
          },
        }),
      },
    ],
  }
}

// Page-specific SEO configurations
export const seoConfigs = {
  home: {
    title: 'Industrial LED Lighting Solutions',
    description: 'High-performance LED Tripods, Light Bars, and Work Lights with factory-direct pricing. Shenzhen manufacturing with North American support.',
    keywords: 'LED tripods, light bars, work lights, industrial lighting, factory direct, North American support',
  },
  products: {
    title: 'Industrial LED Products',
    description: 'Explore our high-performance industrial LED lighting products including tripods, light bars, and work lights. Technical specifications and features.',
    keywords: 'LED tripod specs, light bar specifications, work light features, industrial LED products',
  },
  oem: {
    title: 'OEM & Custom Lighting Solutions',
    description: 'Private label and custom industrial LED lighting solutions for distributors and brands. Full OEM/ODM services with custom specs.',
    keywords: 'OEM LED lighting, private label lighting, custom industrial lights, branding solutions, custom specifications',
  },
  about: {
    title: 'About PowerHouse Industrial Lighting',
    description: 'Learn about our story - bridging Shenzhen manufacturing excellence with Toronto-based North American support for industrial LED lighting.',
    keywords: 'about us, company story, manufacturing facility, Toronto office, Shenzhen factory',
  },
  blog: {
    title: 'Industrial Lighting Blog & Insights',
    description: 'Industry insights, technical guides, and innovation updates for industrial LED lighting applications and best practices.',
    keywords: 'LED blog, industrial lighting insights, technical guides, case studies, industry updates',
  },
  contact: {
    title: 'Contact Us for Industrial LED Solutions',
    description: 'Get in touch with our Toronto and Shenzhen teams for industrial LED lighting inquiries, quotes, and technical support.',
    keywords: 'contact us, get a quote, technical support, sales inquiry, customer service',
  },
}