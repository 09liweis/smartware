<template>
  <div>
    <!-- Hero Section -->
    <PageHero
      title="The Knowledge Hub"
      description="Industry insights, technical expertise, and innovation updates from the PowerHouse team"
    />

    <!-- Category Filter -->
    <section class="py-8 bg-gray-50">
      <div class="container mx-auto px-4">
        <div class="flex flex-wrap gap-4 justify-center">
          <button class="bg-blue-600 text-white px-6 py-2 rounded-full font-medium">
            All Articles
          </button>
          <button class="bg-white border border-gray-300 text-gray-700 px-6 py-2 rounded-full font-medium hover:bg-gray-50">
            Industry Insights
          </button>
          <button class="bg-white border border-gray-300 text-gray-700 px-6 py-2 rounded-full font-medium hover:bg-gray-50">
            Technical Guides
          </button>
          <button class="bg-white border border-gray-300 text-gray-700 px-6 py-2 rounded-full font-medium hover:bg-gray-50">
            Product Updates
          </button>
          <button class="bg-white border border-gray-300 text-gray-700 px-6 py-2 rounded-full font-medium hover:bg-gray-50">
            Case Studies
          </button>
        </div>
      </div>
    </section>

    <!-- Featured Articles -->
    <section class="py-20">
      <div class="container mx-auto px-4">
        <div class="text-center mb-16">
          <h2 class="text-4xl font-bold mb-6">Industry Insights</h2>
          <p class="text-gray-600 max-w-2xl mx-auto text-lg">
            Expert analysis and practical guidance for industrial lighting applications
          </p>
        </div>
        
        <!-- Article 1 -->
        <div class="max-w-4xl mx-auto mb-16">
          <div class="bg-white rounded-xl shadow-lg overflow-hidden">
            <div class="md:flex">
              <div class="md:w-1/3 bg-gradient-to-br from-blue-900 to-gray-900 min-h-48"></div>
              <div class="md:w-2/3 p-8">
                <div class="flex items-center mb-4">
                  <span class="bg-blue-100 text-blue-600 px-3 py-1 rounded-full text-sm font-medium">
                    Industry Insights
                  </span>
                  <span class="ml-4 text-gray-500">March 15, 2024</span>
                </div>
                <h3 class="text-2xl font-bold mb-4">
                  "Why IP69K is the only rating that matters for Canadian Winter Fleet Lights"
                </h3>
                <p class="text-gray-600 mb-6">
                  Discover why standard waterproof ratings fall short in harsh Canadian winter conditions and how IP69K certification ensures reliable performance through snow, ice, and salt spray.
                </p>
                <div class="flex items-center justify-between">
                  <span class="text-gray-500">8 min read</span>
                  <button class="text-blue-600 hover:text-blue-700 font-medium">
                    Read Article →
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
        
        <!-- Article 2 -->
        <div class="max-w-4xl mx-auto mb-16">
          <div class="bg-white rounded-xl shadow-lg overflow-hidden">
            <div class="md:flex">
              <div class="md:w-1/3 bg-gradient-to-br from-gray-900 to-blue-900 min-h-48"></div>
              <div class="md:w-2/3 p-8">
                <div class="flex items-center mb-4">
                  <span class="bg-blue-100 text-blue-600 px-3 py-1 rounded-full text-sm font-medium">
                    Technical Guides
                  </span>
                  <span class="ml-4 text-gray-500">February 28, 2024</span>
                </div>
                <h3 class="text-2xl font-bold mb-4">
                  "The hidden costs of 'Cheap' LEDs: How thermal management extends lifespan"
                </h3>
                <p class="text-gray-600 mb-6">
                  Understanding the engineering behind thermal management in LED systems and why investing in proper cooling solutions pays off through dramatically extended product lifespan and reduced maintenance costs.
                </p>
                <div class="flex items-center justify-between">
                  <span class="text-gray-500">10 min read</span>
                  <button class="text-blue-600 hover:text-blue-700 font-medium">
                    Read Article →
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
        
        <!-- Article 3 -->
        <div class="max-w-4xl mx-auto mb-16">
          <div class="bg-white rounded-xl shadow-lg overflow-hidden">
            <div class="md:flex">
              <div class="md:w-1/3 bg-gradient-to-br from-blue-800 to-gray-800 min-h-48"></div>
              <div class="md:w-2/3 p-8">
                <div class="flex items-center mb-4">
                  <span class="bg-blue-100 text-blue-600 px-3 py-1 rounded-full text-sm font-medium">
                    Business Strategy
                  </span>
                  <span class="ml-4 text-gray-500">January 22, 2024</span>
                </div>
                <h3 class="text-2xl font-bold mb-4">
                  "How to launch your own lighting brand via our OEM program"
                </h3>
                <p class="text-gray-600 mb-6">
                  A comprehensive guide for distributors and entrepreneurs looking to create their own branded lighting line, covering everything from product specification to market positioning.
                </p>
                <div class="flex items-center justify-between">
                  <span class="text-gray-500">12 min read</span>
                  <button class="text-blue-600 hover:text-blue-700 font-medium">
                    Read Article →
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Recent Articles Grid -->
    <section class="py-20 bg-gray-50">
      <div class="container mx-auto px-4">
        <div class="text-center mb-16">
          <h2 class="text-4xl font-bold mb-6">Recent Articles</h2>
          <p class="text-gray-600 max-w-2xl mx-auto text-lg">
            More insights and updates from our technical team
          </p>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-6xl mx-auto">
          <!-- Article 4 -->
          <div class="bg-white rounded-xl shadow-lg overflow-hidden">
            <div class="bg-gradient-to-br from-gray-800 to-blue-800 h-48"></div>
            <div class="p-6">
              <div class="flex items-center mb-3">
                <span class="bg-gray-100 text-gray-600 px-2 py-1 rounded text-xs font-medium">
                  Technical
                </span>
                <span class="ml-2 text-gray-500 text-sm">Dec 10, 2023</span>
              </div>
              <h3 class="text-xl font-bold mb-3">
                LED Driver Selection Guide for Industrial Applications
              </h3>
              <p class="text-gray-600 mb-4 text-sm">
                Choosing the right driver for different environmental conditions and power requirements.
              </p>
              <button class="text-blue-600 hover:text-blue-700 text-sm font-medium">
                Read More →
              </button>
            </div>
          </div>
          
          <!-- Article 5 -->
          <div class="bg-white rounded-xl shadow-lg overflow-hidden">
            <div class="bg-gradient-to-br from-blue-900 to-gray-800 h-48"></div>
            <div class="p-6">
              <div class="flex items-center mb-3">
                <span class="bg-gray-100 text-gray-600 px-2 py-1 rounded text-xs font-medium">
                  Case Study
                </span>
                <span class="ml-2 text-gray-500 text-sm">Nov 25, 2023</span>
              </div>
              <h3 class="text-xl font-bold mb-3">
                Mining Operation: 40% Energy Savings with LED Retrofit
              </h3>
              <p class="text-gray-600 mb-4 text-sm">
                How a Canadian mining company reduced lighting energy costs by switching to our industrial LEDs.
              </p>
              <button class="text-blue-600 hover:text-blue-700 text-sm font-medium">
                Read More →
              </button>
            </div>
          </div>
          
          <!-- Article 6 -->
          <div class="bg-white rounded-xl shadow-lg overflow-hidden">
            <div class="bg-gradient-to-br from-gray-900 to-blue-900 h-48"></div>
            <div class="p-6">
              <div class="flex items-center mb-3">
                <span class="bg-gray-100 text-gray-600 px-2 py-1 rounded text-xs font-medium">
                  Innovation
                </span>
                <span class="ml-2 text-gray-500 text-sm">Oct 18, 2023</span>
              </div>
              <h3 class="text-xl font-bold mb-3">
                Smart Lighting Integration for Construction Sites
              </h3>
              <p class="text-gray-600 mb-4 text-sm">
                The future of connected lighting systems in temporary work environments.
              </p>
              <button class="text-blue-600 hover:text-blue-700 text-sm font-medium">
                Read More →
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Newsletter Subscription -->
    <section class="py-20">
      <div class="container mx-auto px-4">
        <div class="max-w-3xl mx-auto text-center">
          <h2 class="text-4xl font-bold mb-6">Stay Updated</h2>
          <p class="text-gray-600 mb-8 text-lg">
            Subscribe to our newsletter for the latest industry insights, product updates, and technical guides delivered directly to your inbox.
          </p>
          
          <form @submit.prevent class="flex flex-col sm:flex-row gap-4 max-w-md mx-auto">
            <input 
              type="email" 
              placeholder="Your email address" 
              class="flex-grow px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
            <button type="submit" class="bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-lg font-semibold transition-colors">
              Subscribe
            </button>
          </form>
          
          <p class="text-gray-500 text-sm mt-4">
            No spam. Unsubscribe anytime.
          </p>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import { generateSeoMeta, seoConfigs } from '@/utils/seo'

// Define page meta for SEO
definePageMeta({
  // SEO configuration for the blog page
  ...generateSeoMeta(seoConfigs.blog),
})
</script>