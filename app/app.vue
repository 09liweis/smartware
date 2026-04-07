<template>
  <NuxtLayout>
    <!-- Global structured data for the entire site -->
    <script type="application/ld+json">
      {
        "@context": "https://schema.org",
        "@graph": [
          {
            "@type": "Organization",
            "@id": "https://powerhouse-lighting.com/#organization",
            "name": "PowerHouse Industrial Lighting",
            "url": "https://powerhouse-lighting.com",
            "logo": {
              "@type": "ImageObject",
              "url": "https://powerhouse-lighting.com/logo.png"
            },
            "description": "Industrial LED Lighting Solutions with Factory-Direct Pricing and North American Support",
            "sameAs": [
              "https://twitter.com/powerhouselighting",
              "https://linkedin.com/company/powerhouse-lighting"
            ],
            "address": {
              "@type": "PostalAddress",
              "addressLocality": "Toronto",
              "addressRegion": "ON",
              "addressCountry": "CA"
            }
          },
          {
            "@type": "WebSite",
            "@id": "https://powerhouse-lighting.com/#website",
            "url": "https://powerhouse-lighting.com",
            "name": "PowerHouse Industrial Lighting",
            "description": "Industrial LED Lighting Solutions",
            "publisher": {
              "@id": "https://powerhouse-lighting.com/#organization"
            }
          }
        ]
      }
    </script>
    
    <NuxtRouteAnnouncer />
    <NuxtPage />
  </NuxtLayout>
</template>

<script setup lang="ts">
import { siteConfig } from '@/utils/seo'

// Global SEO configuration
useHead({
  htmlAttrs: {
    lang: 'en',
  },
  link: [
    {
      rel: 'icon',
      type: 'image/x-icon',
      href: '/favicon.ico',
    },
  ],
  meta: [
    { charset: 'utf-8' },
    { name: 'viewport', content: 'width=device-width, initial-scale=1' },
    { name: 'format-detection', content: 'telephone=no' },
  ],
})
</script>
