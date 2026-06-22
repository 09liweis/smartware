<template>
  <NuxtLayout>
    <NuxtRouteAnnouncer />
    <NuxtPage />
  </NuxtLayout>
</template>

<script setup lang="ts">
import { COMPANY } from '@/constants/company'

// Global structured data for the entire site
const structuredData = JSON.stringify({
  '@context': 'https://schema.org',
  '@graph': [
    {
      '@type': 'Organization',
      '@id': `${COMPANY.WEBSITE}/#organization`,
      name: COMPANY.FULL_NAME,
      url: COMPANY.WEBSITE,
      description: COMPANY.DESCRIPTION,
      address: {
        '@type': 'PostalAddress',
        addressLocality: COMPANY.LOCATIONS.HEADQUARTERS.city,
        addressRegion: COMPANY.LOCATIONS.HEADQUARTERS.region,
        addressCountry: COMPANY.LOCATIONS.HEADQUARTERS.country,
      },
    },
    {
      '@type': 'WebSite',
      '@id': `${COMPANY.WEBSITE}/#website`,
      url: COMPANY.WEBSITE,
      name: COMPANY.NAME,
      description: COMPANY.DESCRIPTION,
      publisher: { '@id': `${COMPANY.WEBSITE}/#organization` },
    },
  ],
})

useHead({
  htmlAttrs: { lang: 'en' },
  link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }],
  meta: [
    { charset: 'utf-8' },
    { name: 'viewport', content: 'width=device-width, initial-scale=1' },
    { name: 'format-detection', content: 'telephone=no' },
  ],
  script: [{ type: 'application/ld+json', innerHTML: structuredData }],
})
</script>
