<template>
  <header class="bg-[#121214] border-b border-[#2D3139] sticky top-0 z-50">
    <div class="max-w-7xl mx-auto px-4">
      <div class="flex items-center justify-between h-16">
        <!-- Logo -->
        <NuxtLink to="/" class="flex items-center space-x-3 hover:opacity-90 transition-opacity shrink-0">
          <div class="text-xl font-extrabold tracking-tight">
            <span class="text-[#FF6B00]">SST</span><span class="text-white">-Smartware</span>
          </div>
        </NuxtLink>

        <!-- Desktop Navigation -->
        <nav class="hidden lg:flex items-center space-x-1 ml-8">
          <!-- Home -->
          <NuxtLink
            to="/"
            class="px-3 py-2 text-sm font-medium text-[#9A9EA6] hover:text-white rounded-sm transition-colors"
            active-class="text-white !font-semibold"
          >
            Home
          </NuxtLink>

          <!-- Products Dropdown -->
          <div class="relative group" @mouseenter="activeDropdown = 'products'" @mouseleave="activeDropdown = null">
            <button
              class="flex items-center px-3 py-2 text-sm font-medium text-[#9A9EA6] group-hover:text-white rounded-sm transition-colors"
              :class="{ 'text-white': activeDropdown === 'products' }"
            >
              Products
              <svg class="w-3.5 h-3.5 ml-1 opacity-60 group-hover:opacity-100" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
              </svg>
            </button>
            <div
              v-if="activeDropdown === 'products'"
              class="absolute top-full left-0 mt-0 w-[480px] bg-[#1C1E22] border border-[#2D3139] rounded-sm shadow-2xl z-50"
            >
              <div class="p-4 grid grid-cols-1 gap-1">
                <NuxtLink
                  v-for="cat in PRODUCT_CATEGORIES"
                  :key="cat.path"
                  :to="cat.path"
                  class="flex items-start gap-3 px-3 py-2.5 rounded-sm hover:bg-[#121214] border border-transparent hover:border-[#2D3139] transition-all group/link"
                >
                  <div>
                    <div class="text-sm font-semibold text-white group-hover/link:text-[#FF6B00] transition-colors">
                      {{ cat.label }}
                    </div>
                    <div class="text-xs text-[#9A9EA6] mt-0.5">{{ cat.description }}</div>
                  </div>
                </NuxtLink>
              </div>
            </div>
          </div>

          <!-- Industries Dropdown -->
          <div class="relative group" @mouseenter="activeDropdown = 'industries'" @mouseleave="activeDropdown = null">
            <button
              class="flex items-center px-3 py-2 text-sm font-medium text-[#9A9EA6] group-hover:text-white rounded-sm transition-colors"
              :class="{ 'text-white': activeDropdown === 'industries' }"
            >
              Industries & Solutions
              <svg class="w-3.5 h-3.5 ml-1 opacity-60 group-hover:opacity-100" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
              </svg>
            </button>
            <div
              v-if="activeDropdown === 'industries'"
              class="absolute top-full left-0 mt-0 w-[420px] bg-[#1C1E22] border border-[#2D3139] rounded-sm shadow-2xl z-50"
            >
              <div class="p-4 grid grid-cols-1 gap-1">
                <NuxtLink
                  v-for="ind in INDUSTRY_VERTICALS"
                  :key="ind.path"
                  :to="ind.path"
                  class="flex items-start gap-3 px-3 py-2.5 rounded-sm hover:bg-[#121214] border border-transparent hover:border-[#2D3139] transition-all group/link"
                >
                  <div>
                    <div class="text-sm font-semibold text-white group-hover/link:text-[#FF6B00] transition-colors">
                      {{ ind.label }}
                    </div>
                    <div class="text-xs text-[#9A9EA6] mt-0.5">{{ ind.description }}</div>
                  </div>
                </NuxtLink>
              </div>
            </div>
          </div>

          <!-- OEM -->
          <NuxtLink
            to="/oem"
            class="px-3 py-2 text-sm font-medium text-[#9A9EA6] hover:text-white rounded-sm transition-colors"
            active-class="text-white !font-semibold"
          >
            OEM / Factory
          </NuxtLink>

          <!-- Contact -->
          <NuxtLink
            to="/contact"
            class="px-3 py-2 text-sm font-medium text-[#9A9EA6] hover:text-white rounded-sm transition-colors"
            active-class="text-white !font-semibold"
          >
            Request RFQ / Contact
          </NuxtLink>
        </nav>

        <!-- Desktop CTA -->
        <div class="hidden lg:block shrink-0 ml-4">
          <NuxtLink
            to="/contact"
            class="bg-[#FF6B00] hover:bg-[#E65100] text-white text-sm font-bold px-5 py-2.5 rounded-sm transition-colors shadow-structural inline-block tracking-wide"
          >
            Request RFQ
          </NuxtLink>
        </div>

        <!-- Mobile Menu Button -->
        <button
          @click="isMobileMenuOpen = !isMobileMenuOpen"
          class="lg:hidden p-2 rounded-sm text-[#9A9EA6] hover:text-white hover:bg-[#1C1E22] transition-colors"
          aria-label="Toggle mobile menu"
        >
          <svg v-if="!isMobileMenuOpen" class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
          </svg>
          <svg v-else class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>
      </div>

      <!-- Mobile Menu -->
      <div v-if="isMobileMenuOpen" class="lg:hidden border-t border-[#2D3139] pb-4">
        <div class="pt-2 space-y-1">
          <NuxtLink to="/" class="block px-3 py-2.5 text-sm font-medium text-[#9A9EA6] hover:text-white hover:bg-[#1C1E22] rounded-sm" @click="isMobileMenuOpen = false">Home</NuxtLink>

          <!-- Mobile Products -->
          <div class="px-3 py-2">
            <button @click="mobileProductsOpen = !mobileProductsOpen" class="flex items-center justify-between w-full text-sm font-medium text-[#9A9EA6] hover:text-white">
              Products
              <svg :class="{ 'rotate-180': mobileProductsOpen }" class="w-4 h-4 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" /></svg>
            </button>
            <div v-if="mobileProductsOpen" class="mt-1 ml-3 space-y-1 border-l border-[#2D3139] pl-3">
              <NuxtLink v-for="cat in PRODUCT_CATEGORIES" :key="cat.path" :to="cat.path" class="block px-2 py-2 text-sm text-[#9A9EA6] hover:text-white rounded-sm" @click="isMobileMenuOpen = false">{{ cat.label }}</NuxtLink>
            </div>
          </div>

          <!-- Mobile Industries -->
          <div class="px-3 py-2">
            <button @click="mobileIndustriesOpen = !mobileIndustriesOpen" class="flex items-center justify-between w-full text-sm font-medium text-[#9A9EA6] hover:text-white">
              Industries & Solutions
              <svg :class="{ 'rotate-180': mobileIndustriesOpen }" class="w-4 h-4 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" /></svg>
            </button>
            <div v-if="mobileIndustriesOpen" class="mt-1 ml-3 space-y-1 border-l border-[#2D3139] pl-3">
              <NuxtLink v-for="ind in INDUSTRY_VERTICALS" :key="ind.path" :to="ind.path" class="block px-2 py-2 text-sm text-[#9A9EA6] hover:text-white rounded-sm" @click="isMobileMenuOpen = false">{{ ind.label }}</NuxtLink>
            </div>
          </div>

          <NuxtLink to="/oem" class="block px-3 py-2.5 text-sm font-medium text-[#9A9EA6] hover:text-white hover:bg-[#1C1E22] rounded-sm" @click="isMobileMenuOpen = false">OEM / Factory Capabilities</NuxtLink>
          <NuxtLink to="/contact" class="block px-3 py-2.5 text-sm font-medium text-[#9A9EA6] hover:text-white hover:bg-[#1C1E22] rounded-sm" @click="isMobileMenuOpen = false">Request RFQ / Contact Us</NuxtLink>

          <div class="pt-4 px-3">
            <NuxtLink to="/contact" class="block w-full bg-[#FF6B00] hover:bg-[#E65100] text-white text-sm font-bold py-3 px-4 rounded-sm text-center transition-colors tracking-wide" @click="isMobileMenuOpen = false">
              Request RFQ
            </NuxtLink>
          </div>
        </div>
      </div>
    </div>
  </header>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { PRODUCT_CATEGORIES, INDUSTRY_VERTICALS } from '@/constants/navigation'

const isMobileMenuOpen = ref(false)
const mobileProductsOpen = ref(false)
const mobileIndustriesOpen = ref(false)
const activeDropdown = ref<string | null>(null)
</script>
