<template>
  <header class="bg-gray-900 text-white sticky top-0 z-50 shadow-lg">
    <div class="container mx-auto px-4">
      <div class="flex items-center justify-between h-16">
        <!-- Logo -->
        <NuxtLink to="/" class="flex items-center space-x-3 hover:opacity-80 transition-opacity">
          <div class="text-2xl font-bold tracking-tight">
            <span class="text-blue-500">SMART</span><span class="text-white">WARE</span>
          </div>
          <div class="hidden md:block text-sm text-gray-300">
            {{ COMPANY.TAGLINE }}
          </div>
        </NuxtLink>

        <!-- Desktop Navigation -->
        <nav class="hidden md:flex items-center space-x-8">
          <NuxtLink
            v-for="item in MAIN_NAVIGATION"
            :key="item.path"
            :to="item.path"
            class="hover:text-blue-400 transition-colors font-medium"
          >
            {{ item.label }}
          </NuxtLink>
        </nav>

        <!-- Desktop CTA Button -->
        <div class="hidden md:block">
          <NuxtLink
            :to="CTA_BUTTON.path"
            class="bg-blue-600 hover:bg-blue-700 text-white px-6 py-2 rounded-lg font-medium transition-colors shadow-md hover:shadow-lg inline-block"
          >
            {{ CTA_BUTTON.label }}
          </NuxtLink>
        </div>

        <!-- Mobile Menu Button -->
        <button
          @click="isMobileMenuOpen = !isMobileMenuOpen"
          class="md:hidden p-2 rounded-md text-gray-400 hover:text-white hover:bg-gray-800 focus:outline-none focus:ring-2 focus:ring-blue-500"
          aria-label="Toggle mobile menu"
        >
          <svg
            class="w-6 h-6"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
            :class="{ 'hidden': isMobileMenuOpen, 'block': !isMobileMenuOpen }"
          >
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
          </svg>
          <svg
            class="w-6 h-6"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
            :class="{ 'block': isMobileMenuOpen, 'hidden': !isMobileMenuOpen }"
          >
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>
      </div>

      <!-- Mobile Menu -->
      <div
        v-if="isMobileMenuOpen"
        class="md:hidden bg-gray-800 border-t border-gray-700"
        @click="isMobileMenuOpen = false"
      >
        <div class="px-2 pt-2 pb-3 space-y-1">
          <NuxtLink
            v-for="item in MAIN_NAVIGATION"
            :key="item.path"
            :to="item.path"
            class="block px-3 py-2 rounded-md text-base font-medium hover:text-blue-400 hover:bg-gray-700 transition-colors"
          >
            {{ item.label }}
          </NuxtLink>

          <!-- Mobile CTA Button -->
          <div class="pt-4 px-3">
            <NuxtLink
              :to="CTA_BUTTON.path"
              class="w-full bg-blue-600 hover:bg-blue-700 text-white px-4 py-3 rounded-lg font-medium transition-colors shadow-md inline-block text-center"
            >
              {{ CTA_BUTTON.label }}
            </NuxtLink>
          </div>

          <!-- Mobile Tagline -->
          <div class="pt-4 px-3 text-sm text-gray-400 text-center">
            {{ COMPANY.TAGLINE }}
          </div>
        </div>
      </div>
    </div>
  </header>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'
import { MAIN_NAVIGATION, CTA_BUTTON } from '@/constants/navigation'
import { COMPANY } from '@/constants/company'

const isMobileMenuOpen = ref(false)

// Close mobile menu when clicking outside
const handleClickOutside = (event: MouseEvent) => {
  const target = event.target as HTMLElement
  if (isMobileMenuOpen.value && !target.closest('.md\\:hidden')) {
    isMobileMenuOpen.value = false
  }
}

onMounted(() => {
  document.addEventListener('click', handleClickOutside)
})

onUnmounted(() => {
  document.removeEventListener('click', handleClickOutside)
})
</script>

<style scoped>
.router-link-active {
  color: #60a5fa;
  font-weight: 600;
}

/* Smooth transitions */
header {
  transition: all 0.3s ease;
}

/* Mobile menu animations */
.mobile-menu-enter-active,
.mobile-menu-leave-active {
  transition: all 0.3s ease;
}

.mobile-menu-enter-from,
.mobile-menu-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}
</style>