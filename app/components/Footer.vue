<template>
  <footer class="bg-gray-900 text-white py-12">
    <div class="container mx-auto px-4">
      <div class="grid grid-cols-1 md:grid-cols-4 gap-8">
        <!-- Company Info -->
        <div>
          <NuxtLink to="/" class="inline-block text-2xl font-bold mb-4 hover:opacity-80 transition-opacity">
            <span class="text-blue-500">SMART</span><span class="text-white">WARE</span>
          </NuxtLink>
          <p class="text-gray-400 mb-4">
            {{ COMPANY.TAGLINE }}
          </p>
          <p class="text-gray-400 text-sm">
            {{ COMPANY.DESCRIPTION }}
          </p>
        </div>

        <!-- Quick Links -->
        <div>
          <h4 class="text-lg font-semibold mb-4">Quick Links</h4>
          <ul class="space-y-2">
            <li
              v-for="item in FOOTER_QUICK_LINKS"
              :key="item.path"
            >
              <NuxtLink
                :to="item.path"
                class="text-gray-400 hover:text-blue-400 transition-colors"
              >
                {{ item.label }}
              </NuxtLink>
            </li>
          </ul>
        </div>

        <!-- Contact Info -->
        <div>
          <h4 class="text-lg font-semibold mb-4">Contact Info</h4>
          <ul class="space-y-2 text-gray-400">
            <li class="flex items-start">
              <svg class="w-5 h-5 mr-2 mt-0.5" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z" clip-rule="evenodd" />
              </svg>
              <span>{{ headquartersLocation }}</span>
            </li>
            <li class="flex items-start">
              <svg class="w-5 h-5 mr-2 mt-0.5" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z" clip-rule="evenodd" />
              </svg>
              <span>{{ manufacturingLocation }}</span>
            </li>
            <li class="flex items-center">
              <svg class="w-5 h-5 mr-2" fill="currentColor" viewBox="0 0 20 20">
                <path d="M2.003 5.884L10 9.882l7.997-3.998A2 2 0 0016 4H4a2 2 0 00-1.997 1.884z" />
                <path d="M18 8.118l-8 4-8-4V14a2 2 0 002 2h12a2 2 0 002-2V8.118z" />
              </svg>
              <span>{{ COMPANY.EMAIL }}</span>
            </li>
          </ul>
        </div>

        <!-- Newsletter -->
        <div>
          <h4 class="text-lg font-semibold mb-4">Newsletter</h4>
          <p class="text-gray-400 mb-4 text-sm">
            Stay updated with our latest products and industry insights.
          </p>
          <form @submit.prevent class="flex">
            <input
              type="email"
              placeholder="Your email"
              class="bg-gray-800 text-white px-4 py-2 rounded-l-lg flex-grow focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
            <button type="submit" class="bg-blue-600 hover:bg-blue-700 px-4 py-2 rounded-r-lg transition-colors">
              Subscribe
            </button>
          </form>
        </div>
      </div>

      <!-- Copyright -->
      <div class="border-t border-gray-800 mt-8 pt-8 text-center text-gray-400 text-sm">
        <p>&copy; {{ currentYear }} {{ COMPANY.FULL_NAME }}. All rights reserved.</p>
      </div>
    </div>
  </footer>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { FOOTER_QUICK_LINKS } from '@/constants/navigation'
import { COMPANY } from '@/constants/company'

// Computed properties for location formatting
const headquartersLocation = computed(() => {
  const loc = COMPANY.LOCATIONS.HEADQUARTERS
  return `${loc.city}, ${loc.region}, ${loc.country}`
})

const manufacturingLocation = computed(() => {
  const loc = COMPANY.LOCATIONS.MANUFACTURING
  return `${loc.city}, ${loc.region}, ${loc.country}`
})

// Current year for copyright
const currentYear = computed(() => new Date().getFullYear())
</script>