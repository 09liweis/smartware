<template>
  <div>
    <!-- Hero Section -->
    <PageHero
      title="Commercial-Grade LED Hardware Systems"
      subtitle="High-lumen efficiency, robust thermal management, and extreme weatherproofing built direct from our Shenzhen assembly lines and backed by dedicated North American support."
      :breadcrumbs="[
        { label: 'Home', path: '/' },
        { label: 'B2B Technical Catalog' },
      ]"
    />

    <!-- Category Navigation Cards -->
    <section class="py-20 bg-[#121214]">
      <div class="max-w-7xl mx-auto px-4">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <!-- Card 1: Rechargeable Work Lights -->
          <NuxtLink to="/products/rechargeable-work-lights" class="bg-[#1C1E22] border border-[#2D3139] rounded-sm p-8 hover:border-[#FF6B00] transition-all group shadow-structural">
            <div class="flex items-start justify-between mb-4">
              <div class="w-12 h-12 bg-[#121214] border border-[#2D3139] rounded-sm flex items-center justify-center">
                <svg class="w-6 h-6 text-[#FF6B00]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
                </svg>
              </div>
              <span class="text-xs font-mono text-[#9A9EA6] bg-[#121214] px-2 py-0.5 rounded-sm border border-[#2D3139]">{{ rwCount }} Models</span>
            </div>
            <h3 class="text-xl font-bold text-white mb-2 group-hover:text-[#FF6B00] transition-colors">LED Rechargeable Work Lights</h3>
            <p class="text-sm text-[#9A9EA6] mb-6 leading-relaxed">Portable cordless task lighting featuring integrated industrial magnetic mounting profiles or high-stability multi-position support stands.</p>
            <div class="flex items-center text-sm font-semibold text-[#FF6B00]">
              Explore Rechargeable Work Lights Matrix
              <svg class="w-4 h-4 ml-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" /></svg>
            </div>
          </NuxtLink>

          <!-- Card 2: LED Work Lights -->
          <NuxtLink to="/products/led-work-lights" class="bg-[#1C1E22] border border-[#2D3139] rounded-sm p-8 hover:border-[#FF6B00] transition-all group shadow-structural">
            <div class="flex items-start justify-between mb-4">
              <div class="w-12 h-12 bg-[#121214] border border-[#2D3139] rounded-sm flex items-center justify-center">
                <svg class="w-6 h-6 text-[#FF6B00]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M5 3l14 9-14 9V3z" />
                </svg>
              </div>
              <span class="text-xs font-mono text-[#9A9EA6] bg-[#121214] px-2 py-0.5 rounded-sm border border-[#2D3139]">{{ wlCount }} Models</span>
            </div>
            <h3 class="text-xl font-bold text-white mb-2 group-hover:text-[#FF6B00] transition-colors">LED Work Lights</h3>
            <p class="text-sm text-[#9A9EA6] mb-6 leading-relaxed">Rugged fixed corded flood arrays categorized across three structural power brackets: Light Duty (&le;30W), Medium Duty (&lt;60W), and Heavy Duty (&ge;60W).</p>
            <div class="flex items-center text-sm font-semibold text-[#FF6B00]">
              Explore Fixed Work Lights Matrix
              <svg class="w-4 h-4 ml-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" /></svg>
            </div>
          </NuxtLink>

          <!-- Card 3: LED Light Bars -->
          <NuxtLink to="/products/led-light-bars" class="bg-[#1C1E22] border border-[#2D3139] rounded-sm p-8 hover:border-[#FF6B00] transition-all group shadow-structural">
            <div class="flex items-start justify-between mb-4">
              <div class="w-12 h-12 bg-[#121214] border border-[#2D3139] rounded-sm flex items-center justify-center">
                <svg class="w-6 h-6 text-[#FF6B00]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4" />
                </svg>
              </div>
              <span class="text-xs font-mono text-[#9A9EA6] bg-[#121214] px-2 py-0.5 rounded-sm border border-[#2D3139]">{{ lbCount }} Models</span>
            </div>
            <h3 class="text-xl font-bold text-white mb-2 group-hover:text-[#FF6B00] transition-colors">LED Light Bars</h3>
            <p class="text-sm text-[#9A9EA6] mb-6 leading-relaxed">Low-profile, high-intensity forward and peripheral illumination arrays built for low-voltage commercial fleet vehicle deployment (10V-30V DC).</p>
            <div class="flex items-center text-sm font-semibold text-[#FF6B00]">
              Explore Vehicle Light Bars Matrix
              <svg class="w-4 h-4 ml-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" /></svg>
            </div>
          </NuxtLink>

          <!-- Card 4: LED Tripods -->
          <NuxtLink to="/products/led-tripods" class="bg-[#1C1E22] border border-[#2D3139] rounded-sm p-8 hover:border-[#FF6B00] transition-all group shadow-structural">
            <div class="flex items-start justify-between mb-4">
              <div class="w-12 h-12 bg-[#121214] border border-[#2D3139] rounded-sm flex items-center justify-center">
                <svg class="w-6 h-6 text-[#FF6B00]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M13 10V3L4 14h7v7l9-11h-7z" />
                </svg>
              </div>
              <span class="text-xs font-mono text-[#9A9EA6] bg-[#121214] px-2 py-0.5 rounded-sm border border-[#2D3139]">{{ trCount }} Models</span>
            </div>
            <h3 class="text-xl font-bold text-white mb-2 group-hover:text-[#FF6B00] transition-colors">LED Tripods</h3>
            <p class="text-sm text-[#9A9EA6] mb-6 leading-relaxed">Telescopic rapid-deployment temporary site tower masts available in continuous AC-corded utility profiles or heavy cordless rechargeable setups.</p>
            <div class="flex items-center text-sm font-semibold text-[#FF6B00]">
              Explore Telescopic Tripods Matrix
              <svg class="w-4 h-4 ml-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" /></svg>
            </div>
          </NuxtLink>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import { generateSeoMeta, seoConfigs } from '@/utils/seo'
import ledLightsData from '@/led_lights.json'

definePageMeta({
  ...generateSeoMeta(seoConfigs.products),
})

const rwCount = computed(() => ((ledLightsData as unknown) as Record<string, any[]>)['LED Rechargeable Work Light']?.length || 0)
const wlCount = computed(() => ((ledLightsData as unknown) as Record<string, any[]>)['LED Work Light']?.length || 0)
const lbCount = computed(() => ((ledLightsData as unknown) as Record<string, any[]>)['LED Light Bar']?.length || 0)
const trCount = computed(() => ((ledLightsData as unknown) as Record<string, any[]>)['LED Tripod']?.length || 0)
</script>
