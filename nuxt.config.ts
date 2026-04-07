// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },
  modules: ['@nuxtjs/tailwindcss'],
  
  // SEO Optimization
  app: {
    head: {
      charset: 'utf-8',
      viewport: 'width=device-width, initial-scale=1',
      title: 'PowerHouse Industrial Lighting',
      meta: [
        { name: 'description', content: 'Industrial LED Lighting Solutions with Factory-Direct Pricing and North American Support' },
        { name: 'keywords', content: 'industrial LED lighting, LED tripods, light bars, work lights, factory-direct pricing' },
        { name: 'author', content: 'PowerHouse Industrial Lighting' },
        { name: 'robots', content: 'index, follow' },
      ],
      link: [
        { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
        { rel: 'sitemap', type: 'application/xml', href: '/sitemap.xml' },
        { rel: 'canonical', href: 'https://powerhouse-lighting.com' },
      ],
    },
  },
  
  // Performance optimization
  nitro: {
    prerender: {
      crawlLinks: true,
      routes: ['/', '/products', '/oem', '/about', '/blog', '/contact']
    }
  },
  
  // Route rules for SEO
  routeRules: {
    '/': { prerender: true },
    '/products': { prerender: true },
    '/oem': { prerender: true },
    '/about': { prerender: true },
    '/blog': { prerender: true },
    '/contact': { prerender: true },
  },
})