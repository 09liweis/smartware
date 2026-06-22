<template>
  <!-- Trust Anchor GEO Strip -->
  <section class="border-t border-[#2D3139] bg-[#1C1E22] py-8 px-6 text-center md:text-left">
    <div class="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between gap-4">
      <p class="text-sm text-white max-w-3xl leading-relaxed">
        <strong class="text-[#FF6B00]">The SST Advantage:</strong> High-precision manufacturing engineering and scale direct from our
        <span class="underline decoration-[#FF6B00]">Shenzhen production facilities</span>, fully secured and backed by localized
        account management, logistical oversight, and warranty fulfillment straight out of the
        <span class="underline decoration-[#FF6B00]">Greater Toronto Area</span>.
      </p>
      <div class="flex items-center gap-4 opacity-50">
        <span class="text-xs font-mono font-bold tracking-widest text-white border border-white px-2 py-1 rounded-sm">cULus</span>
        <span class="text-xs font-mono font-bold tracking-widest text-white border border-white px-2 py-1 rounded-sm">ETL</span>
        <span class="text-xs font-mono font-bold tracking-widest text-white border border-white px-2 py-1 rounded-sm">CE</span>
        <span class="text-xs font-mono font-bold tracking-widest text-white border border-white px-2 py-1 rounded-sm">IP65</span>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer class="bg-[#121214] border-t border-[#2D3139] py-12">
    <div class="max-w-7xl mx-auto px-4">
      <div class="grid grid-cols-1 md:grid-cols-5 gap-8">
        <!-- Company Info -->
        <div class="md:col-span-2">
          <NuxtLink to="/" class="inline-block text-xl font-extrabold mb-4 hover:opacity-90 transition-opacity">
            <span class="text-[#FF6B00]">SST</span><span class="text-white">-Smartware</span>
          </NuxtLink>
          <p class="text-[#9A9EA6] text-sm mb-3 leading-relaxed">
            {{ COMPANY.TAGLINE }}
          </p>
          <p class="text-[#9A9EA6] text-xs leading-relaxed">
            {{ COMPANY.DESCRIPTION }}
          </p>
        </div>

        <!-- Products -->
        <div>
          <h4 class="text-xs font-semibold text-white uppercase tracking-widest mb-4">Products</h4>
          <ul class="space-y-2">
            <li v-for="item in FOOTER_PRODUCT_LINKS" :key="item.path">
              <NuxtLink :to="item.path" class="text-sm text-[#9A9EA6] hover:text-white transition-colors">
                {{ item.label }}
              </NuxtLink>
            </li>
          </ul>
        </div>

        <!-- Industries -->
        <div>
          <h4 class="text-xs font-semibold text-white uppercase tracking-widest mb-4">Industries</h4>
          <ul class="space-y-2">
            <li v-for="ind in INDUSTRY_VERTICALS" :key="ind.path">
              <NuxtLink :to="ind.path" class="text-sm text-[#9A9EA6] hover:text-white transition-colors">
                {{ ind.label }}
              </NuxtLink>
            </li>
          </ul>
        </div>

        <!-- Locations -->
        <div>
          <h4 class="text-xs font-semibold text-white uppercase tracking-widest mb-4">Locations</h4>
          <ul class="space-y-3 text-sm text-[#9A9EA6]">
            <li class="flex items-start gap-2">
              <svg class="w-4 h-4 mt-0.5 shrink-0 text-[#FF6B00]" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z" clip-rule="evenodd" />
              </svg>
              <span>{{ COMPANY.LOCATIONS.HEADQUARTERS.city }}, {{ COMPANY.LOCATIONS.HEADQUARTERS.region }}, {{ COMPANY.LOCATIONS.HEADQUARTERS.country }}</span>
            </li>
            <li class="flex items-start gap-2">
              <svg class="w-4 h-4 mt-0.5 shrink-0 text-[#FF6B00]" fill="currentColor" viewBox="0 0 20 20">
                <path d="M10.394 2.08a1 1 0 00-.788 0l-7 3a1 1 0 000 1.84L5.25 8.051a.999.999 0 01.356-.257l4-1.714a1 1 0 11.788 1.838L7.667 9.088l1.94.831a1 1 0 00.787 0l7-3a1 1 0 000-1.838l-7-3z" />
              </svg>
              <span>{{ COMPANY.LOCATIONS.MANUFACTURING.city }}, {{ COMPANY.LOCATIONS.MANUFACTURING.country }}</span>
            </li>
            <li class="flex items-center gap-2">
              <svg class="w-4 h-4 shrink-0 text-[#FF6B00]" fill="currentColor" viewBox="0 0 20 20">
                <path d="M2.003 5.884L10 9.882l7.997-3.998A2 2 0 0016 4H4a2 2 0 00-1.997 1.884z" />
                <path d="M18 8.118l-8 4-8-4V14a2 2 0 002 2h12a2 2 0 002-2V8.118z" />
              </svg>
              <span>{{ COMPANY.EMAIL }}</span>
            </li>
          </ul>
        </div>
      </div>

      <!-- Bottom Bar -->
      <div class="border-t border-[#2D3139] mt-10 pt-8 flex flex-col md:flex-row items-center justify-between gap-4">
        <p class="text-xs text-[#9A9EA6]">
          &copy; {{ currentYear }} {{ COMPANY.FULL_NAME }}. All rights reserved.
        </p>
        <div class="flex items-center gap-6 text-xs text-[#9A9EA6]">
          <NuxtLink to="/about" class="hover:text-white transition-colors">About</NuxtLink>
          <NuxtLink to="/blog" class="hover:text-white transition-colors">Blog</NuxtLink>
          <NuxtLink to="/contact" class="hover:text-white transition-colors">Contact</NuxtLink>
        </div>
      </div>
    </div>
  </footer>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { COMPANY } from '@/constants/company'
import { FOOTER_PRODUCT_LINKS, INDUSTRY_VERTICALS } from '@/constants/navigation'

const currentYear = computed(() => new Date().getFullYear())
</script>
