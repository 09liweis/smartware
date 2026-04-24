<template>
  <div>

    
    <!-- Hero Section -->
    <PageHero
      title="Industrial LED Lighting. Factory-Direct Pricing. North American Support."
      description="High-performance LED Tripods, Light Bars, and Work Lights engineered in Shenzhen and managed from Toronto."
    >
      <template #actions>
        <button class="bg-blue-600 hover:bg-blue-700 text-white px-8 py-4 rounded-lg text-lg font-semibold transition-colors shadow-lg">
          View Product Catalog
        </button>
        <button class="bg-transparent border-2 border-white hover:bg-white hover:text-gray-900 text-white px-8 py-4 rounded-lg text-lg font-semibold transition-colors">
          Request Wholesale Quote
        </button>
      </template>
    </PageHero>

    <!-- Why Us Section -->
    <WhyUsSection />

    <!-- Featured Series -->
    <section class="py-20">
      <div class="container mx-auto px-4">
        <div class="text-center mb-16">
          <h2 class="text-4xl font-bold mb-6">Featured Series</h2>
          <p class="text-gray-600 max-w-2xl mx-auto text-lg">
            Industry-leading lighting solutions built for demanding environments
          </p>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-4xl mx-auto">
          <div class="bg-gradient-to-br from-blue-900 to-gray-900 text-white p-8 rounded-2xl shadow-xl">
            <h3 class="text-3xl font-bold mb-4">The ApexTower™ (Tripods)</h3>
            <p class="text-xl text-blue-200 mb-6 italic">"The gold standard for portable site lighting."</p>
            <ul class="space-y-3">
              <li class="flex items-center">
                <svg class="w-5 h-5 mr-3 text-blue-400" fill="currentColor" viewBox="0 0 20 20">
                  <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
                </svg>
                <span>Portable telescopic design</span>
              </li>
              <li class="flex items-center">
                <svg class="w-5 h-5 mr-3 text-blue-400" fill="currentColor" viewBox="0 0 20 20">
                  <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
                </svg>
                <span>Weatherproof & impact resistant</span>
              </li>
              <li class="flex items-center">
                <svg class="w-5 h-5 mr-3 text-blue-400" fill="currentColor" viewBox="0 0 20 20">
                  <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
                </svg>
                <span>High-efficiency LED technology</span>
              </li>
            </ul>
          </div>
          
          <div class="bg-gradient-to-br from-gray-900 to-blue-900 text-white p-8 rounded-2xl shadow-xl">
            <h3 class="text-3xl font-bold mb-4">The HorizonView™ (Light Bars)</h3>
            <p class="text-xl text-blue-200 mb-6 italic">"Unmatched beam precision for heavy-duty fleets."</p>
            <ul class="space-y-3">
              <li class="flex items-center">
                <svg class="w-5 h-5 mr-3 text-blue-400" fill="currentColor" viewBox="0 0 20 20">
                  <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
                </svg>
                <span>Precision beam control</span>
              </li>
              <li class="flex items-center">
                <svg class="w-5 h-5 mr-3 text-blue-400" fill="currentColor" viewBox="0 0 20 20">
                  <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
                </svg>
                <span>Durable aluminum housing</span>
              </li>
              <li class="flex items-center">
                <svg class="w-5 h-5 mr-3 text-blue-400" fill="currentColor" viewBox="0 0 20 20">
                  <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
                </svg>
                <span>Advanced thermal management</span>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import { generateSeoMeta, seoConfigs } from '@/utils/seo'

// Define page meta for SEO
definePageMeta({
  // SEO configuration for the home page
  ...generateSeoMeta(seoConfigs.home),
})
</script>