/**
 * Navigation menu constants for SST-Smartware B2B
 */

export interface NavItem {
  label: string
  path: string
  external?: boolean
  children?: { label: string; path: string; description?: string }[]
}

/**
 * Product category sub-navigation
 */
export const PRODUCT_CATEGORIES = [
  {
    label: 'LED Tripod Work Lights',
    path: '/products/led-tripods',
    description: 'ApexTower™ telescopic site systems',
  },
  {
    label: 'Vehicle Light Bars',
    path: '/products/led-light-bars',
    description: 'HorizonView™ fleet illumination',
  },
  {
    label: 'Handheld Task Lights',
    path: '/products/rechargeable-work-lights',
    description: 'ProTask™ cordless portables',
  },
  {
    label: 'High-Bay Area Lighting',
    path: '/products/led-work-lights',
    description: 'DuraFlood™ fixed arrays',
  },
  {
    label: 'Portable Floodlights',
    path: '/products/portable-floodlights',
    description: 'Rapid-deployment area units',
  },
]

/**
 * Industry vertical sub-navigation
 */
export const INDUSTRY_VERTICALS = [
  {
    label: 'Commercial Fleet & Utility Vehicles',
    path: '/industries/commercial-fleet',
    description: 'Service trucks, tow fleets, utility vehicles',
  },
  {
    label: 'Construction & Infrastructure Jobsites',
    path: '/industries/construction-infrastructure',
    description: 'Temporary site lighting for harsh outdoor environments',
  },
  {
    label: 'Industrial Warehousing & Operations',
    path: '/industries/industrial-warehousing',
    description: 'Manufacturing floors, loading docks, facility maintenance',
  },
  {
    label: 'OEM & Private Label Manufacturing',
    path: '/industries/oem-manufacturing',
    description: 'Custom branding, engineering, and supply chain',
  },
]

/**
 * Main navigation menu items
 */
export const MAIN_NAVIGATION: NavItem[] = [
  {
    label: 'Home',
    path: '/',
  },
  {
    label: 'Products',
    path: '/products',
    children: PRODUCT_CATEGORIES,
  },
  {
    label: 'Industries & Solutions',
    path: '/industries',
    children: INDUSTRY_VERTICALS,
  },
  {
    label: 'OEM / Factory Capabilities',
    path: '/oem',
  },
  {
    label: 'Request RFQ / Contact Us',
    path: '/contact',
  },
]

/**
 * Footer quick links
 */
export const FOOTER_QUICK_LINKS: NavItem[] = [
  { label: 'Products', path: '/products' },
  { label: 'Industries', path: '/industries' },
  { label: 'OEM Capabilities', path: '/oem' },
  { label: 'Contact', path: '/contact' },
]

/**
 * Footer product links
 */
export const FOOTER_PRODUCT_LINKS: NavItem[] = [
  { label: 'LED Tripods', path: '/products/led-tripods' },
  { label: 'LED Light Bars', path: '/products/led-light-bars' },
  { label: 'Rechargeable Work Lights', path: '/products/rechargeable-work-lights' },
  { label: 'LED Work Lights', path: '/products/led-work-lights' },
]

/**
 * Footer company links
 */
export const FOOTER_COMPANY_LINKS: NavItem[] = [
  { label: 'About', path: '/about' },
  { label: 'Blog', path: '/blog' },
]

/**
 * CTA Button configuration
 */
export const CTA_BUTTON = {
  label: 'Request RFQ',
  path: '/contact',
} as const

/**
 * Product-to-Industry mapping
 */
export const PRODUCT_INDUSTRY_MAP: Record<string, string[]> = {
  'LED Rechargeable Work Light': ['commercial-fleet', 'industrial-warehousing'],
  'LED Work Light': ['construction-infrastructure', 'industrial-warehousing'],
  'LED Light Bar': ['commercial-fleet'],
  'LED Tripod': ['construction-infrastructure'],
}

/**
 * Industry detail data
 */
export const INDUSTRY_DETAILS = [
  {
    slug: 'commercial-fleet',
    title: 'Commercial Fleet & Utility Vehicles',
    focus: 'Heavy vibration protection, sub-zero operating environments, and low-voltage DC auto-switching layouts.',
    productCategories: ['LED Light Bar', 'LED Rechargeable Work Light'],
    hardwareLinks: [
      { label: 'Explore LED Light Bars Matrix →', path: '/products/led-light-bars' },
      { label: 'Explore Rechargeable Work Lights Matrix →', path: '/products/rechargeable-work-lights' },
    ],
    applicationText: 'Engineered for service trucks, tow fleets, and heavy utility vehicles requiring rugged, vibration-tested mobile warning and work illumination.',
  },
  {
    slug: 'construction-infrastructure',
    title: 'Construction & Infrastructure Jobsites',
    focus: 'High-impact shell shielding, concrete dust ingress blocking, and rapid field deployment and transport tracking.',
    productCategories: ['LED Tripod', 'LED Work Light'],
    hardwareLinks: [
      { label: 'Explore LED Tripods Matrix →', path: '/products/led-tripods' },
      { label: 'Explore LED Work Lights Matrix →', path: '/products/led-work-lights' },
    ],
    applicationText: 'High-output, rapid-deployment temporary site lighting built to survive harsh outdoor weather, impacts, and long night shifts.',
  },
  {
    slug: 'industrial-warehousing',
    title: 'Industrial Warehousing & Operations',
    focus: 'Green energy footprint optimization, maximum lumen-per-watt throughput, and flicker-free solid-state electronic ballasts.',
    productCategories: ['LED Work Light', 'LED Rechargeable Work Light'],
    hardwareLinks: [
      { label: 'Explore LED Work Lights Matrix →', path: '/products/led-work-lights' },
    ],
    applicationText: 'Energy-efficient, high-lumen structural illumination and reliable manual task tools for manufacturing floors, loading docks, and facility maintenance.',
  },
  {
    slug: 'oem-manufacturing',
    title: 'OEM & Private Label Manufacturing',
    focus: 'Custom injection shell styling, proprietary board configuration blueprints, laser brand engraving, and complete cross-border logistics clearing.',
    productCategories: ['LED Rechargeable Work Light', 'LED Work Light', 'LED Light Bar', 'LED Tripod'],
    hardwareLinks: [
      { label: 'Explore All Master Product Categories →', path: '/products' },
    ],
    applicationText: 'Direct pipeline to our Shenzhen engineering and manufacturing facilities. Offering customized casing branding, proprietary volt/amp adjustments, and custom mounts with local Toronto supply chain management.',
  },
]
