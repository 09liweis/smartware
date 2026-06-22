// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },
  modules: ['@nuxtjs/tailwindcss'],

  // Global CSS
  css: ['@/assets/css/main.css'],

  // SEO Optimization
  app: {
    head: {
      charset: 'utf-8',
      viewport: 'width=device-width, initial-scale=1',
      title: 'SST-Smartware | Commercial-Grade LED Hardware Systems',
      meta: [
        { name: 'description', content: 'High-lumen efficiency, robust thermal management, and extreme weatherproofing built direct from our Shenzhen assembly lines and backed by dedicated North American support.' },
        { name: 'keywords', content: 'LED work lights, LED tripods, LED light bars, commercial fleet lighting, industrial LED, B2B lighting, OEM LED manufacturing, construction site lighting, warehouse lighting' },
        { name: 'author', content: 'SST-Smartware Industrial Solutions' },
        { name: 'robots', content: 'index, follow' },
      ],
      link: [
        { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
        { rel: 'sitemap', type: 'application/xml', href: '/sitemap.xml' },
        { rel: 'canonical', href: 'https://sst-smartware.netlify.app' },
      ],
    },
  },

  // Performance optimization
  nitro: {
    prerender: {
      crawlLinks: true,
      routes: [
        '/',
        '/products',
        '/products/rechargeable-work-lights',
        '/products/led-work-lights',
        '/products/led-light-bars',
        '/products/led-tripods',
        '/industries',
        '/industries/commercial-fleet',
        '/industries/construction-infrastructure',
        '/industries/industrial-warehousing',
        '/industries/oem-manufacturing',
        '/oem',
        '/about',
        '/blog',
        '/contact',
      ],
    },
  },

  // Route rules for SEO
  routeRules: {
    '/': { prerender: true },
    '/products': { prerender: true },
    '/products/rechargeable-work-lights': { prerender: true },
    '/products/led-work-lights': { prerender: true },
    '/products/led-light-bars': { prerender: true },
    '/products/led-tripods': { prerender: true },
    '/industries': { prerender: true },
    '/industries/commercial-fleet': { prerender: true },
    '/industries/construction-infrastructure': { prerender: true },
    '/industries/industrial-warehousing': { prerender: true },
    '/industries/oem-manufacturing': { prerender: true },
    '/oem': { prerender: true },
    '/about': { prerender: true },
    '/blog': { prerender: true },
    '/contact': { prerender: true },
  },
})
