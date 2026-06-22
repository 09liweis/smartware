/**
 * SEO Configuration for SST-Smartware
 */
import { COMPANY } from '@/constants/company'

export const siteConfig = {
  title: COMPANY.FULL_NAME,
  description: 'High-lumen efficiency, robust thermal management, and extreme weatherproofing built direct from our Shenzhen assembly lines and backed by dedicated North American support.',
  keywords: 'LED work lights, LED tripods, LED light bars, commercial fleet lighting, industrial LED, B2B lighting, OEM LED manufacturing, construction site lighting, warehouse lighting, rechargeable work lights',
  url: 'https://sst-smartware.netlify.app',
  ogImage: '/og-image.png',
  twitterHandle: COMPANY.SOCIAL.TWITTER,
}

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
      { name: 'description', content: description },
      { name: 'keywords', content: keywords },
      { name: 'author', content: siteConfig.title },
      { property: 'og:type', content: 'website' },
      { property: 'og:url', content: url },
      { property: 'og:title', content: title },
      { property: 'og:description', content: description },
      { property: 'og:image', content: image },
      { property: 'og:site_name', content: siteConfig.title },
      { name: 'twitter:card', content: 'summary_large_image' },
      { name: 'twitter:url', content: url },
      { name: 'twitter:title', content: title },
      { name: 'twitter:description', content: description },
      { name: 'twitter:image', content: image },
      { name: 'twitter:creator', content: siteConfig.twitterHandle },
      { name: 'robots', content: 'index, follow' },
      { name: 'googlebot', content: 'index, follow' },
    ],
    link: [{ rel: 'canonical', href: url }],
  }
}

export const seoConfigs = {
  home: {
    title: 'Commercial-Grade LED Hardware Systems',
    description: 'High-lumen efficiency, robust thermal management, and extreme weatherproofing built direct from Shenzhen assembly lines. Factory-direct pricing with North American support.',
    keywords: 'LED work lights, commercial LED lighting, industrial LED, B2B lighting, OEM LED, factory-direct lighting',
  },
  products: {
    title: 'B2B Technical Catalog',
    description: 'Explore our commercial-grade LED hardware systems including tripods, light bars, work lights, and rechargeable task lighting. Technical specifications and OEM availability.',
    keywords: 'LED product catalog, LED work lights, LED tripods, LED light bars, commercial LED hardware, B2B lighting catalog',
  },
  oem: {
    title: 'OEM & Private Label Manufacturing',
    description: 'Full-service OEM/ODM solutions for North American distributors. Custom branding, engineering, private labeling, and factory-direct logistics from Shenzhen to Toronto.',
    keywords: 'OEM LED manufacturing, private label lighting, custom LED branding, factory-direct OEM, Shenzhen manufacturing',
  },
  about: {
    title: 'About SST-Smartware',
    description: 'Bridging Shenzhen manufacturing excellence with Toronto-based North American support. Learn about our 50,000 sq. ft. facility and dedicated local account management.',
    keywords: 'about SST-Smartware, Shenzhen factory, Toronto LED company, industrial lighting manufacturer, North American LED supplier',
  },
  blog: {
    title: 'Industrial Lighting Blog & Insights',
    description: 'Industry insights, technical guides, and innovation updates for commercial LED lighting, fleet illumination, and industrial applications.',
    keywords: 'LED lighting blog, industrial lighting insights, fleet lighting guides, commercial LED articles',
  },
  contact: {
    title: 'Request RFQ / Contact Us',
    description: 'Get a factory-direct quote for commercial LED lighting. Contact our Toronto team for wholesale, OEM, and project supply inquiries.',
    keywords: 'contact SST-Smartware, request LED quote, LED RFQ, commercial lighting inquiry, OEM lighting contact',
  },
}
