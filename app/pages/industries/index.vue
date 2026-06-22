<template>
  <div>
    <PageHero
      title="Illumination Architecture Tailored by Sector"
      subtitle="Certified structures and custom-engineered mounting frameworks mapped directly to North American safety compliance metrics."
      :breadcrumbs="[
        { label: 'Home', path: '/' },
        { label: 'Industries & Solutions' },
      ]"
    />

    <!-- Industry Vertical Segments -->
    <section class="py-16 bg-[#121214]">
      <div class="max-w-7xl mx-auto px-4">
        <div class="space-y-0">
          <div
            v-for="(industry, index) in INDUSTRY_DETAILS"
            :key="industry.slug"
            class="py-16 border-b border-[#2D3139] last:border-b-0"
            :class="index % 2 === 1 ? 'bg-[#1C1E22] -mx-4 px-4' : ''"
          >
            <div class="max-w-4xl mx-auto">
              <!-- Industry Header -->
              <div class="mb-8">
                <NuxtLink :to="`/industries/${industry.slug}`" class="inline-block group">
                  <h2 class="text-2xl md:text-3xl font-extrabold text-white group-hover:text-[#FF6B00] transition-colors mb-3">
                    {{ industry.title }}
                  </h2>
                </NuxtLink>
                <p class="text-base text-[#9A9EA6] leading-relaxed mb-4">
                  {{ industry.applicationText }}
                </p>
                <div class="bg-[#121214]/50 border border-[#2D3139] rounded-sm p-4">
                  <p class="text-sm text-[#9A9EA6]">
                    <strong class="text-white">Technical Focus:</strong> {{ industry.focus }}
                  </p>
                </div>
              </div>

              <!-- Sourced Hardware Entry Points -->
              <div>
                <h4 class="text-xs font-semibold text-[#9A9EA6] uppercase tracking-widest mb-4">Sourced Hardware Entry Points</h4>
                <div class="flex flex-wrap gap-3">
                  <NuxtLink
                    v-for="link in industry.hardwareLinks"
                    :key="link.path"
                    :to="link.path"
                    class="inline-flex items-center gap-1 text-sm font-semibold text-[#FF6B00] hover:text-white border border-[#2D3139] hover:border-[#FF6B00] bg-[#1C1E22] px-4 py-2 rounded-sm transition-all"
                  >
                    {{ link.label }}
                  </NuxtLink>
                </div>
              </div>

              <!-- View Full Solution -->
              <div class="mt-6">
                <NuxtLink :to="`/industries/${industry.slug}`" class="text-sm font-semibold text-[#9A9EA6] hover:text-white transition-colors flex items-center gap-1">
                  View Full Industry Solution
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" /></svg>
                </NuxtLink>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA -->
    <section class="py-20 bg-[#1C1E22] border-t border-[#2D3139]">
      <div class="max-w-3xl mx-auto px-4 text-center">
        <h2 class="text-3xl font-extrabold text-white mb-4">Don't See Your Sector?</h2>
        <p class="text-[#9A9EA6] mb-8">Our engineering team can develop custom illumination architectures for any commercial or industrial application.</p>
        <NuxtLink to="/contact" class="inline-block bg-[#FF6B00] hover:bg-[#E65100] text-white px-8 py-4 rounded-sm text-base font-bold transition-colors tracking-wide shadow-structural">
          Speak with a Solutions Engineer
        </NuxtLink>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import { INDUSTRY_DETAILS } from '@/constants/navigation'

useHead({
  title: 'Industries & Solutions | SST-Smartware',
  meta: [{ name: 'description', content: 'Certified LED illumination architectures tailored for commercial fleet, construction, industrial warehousing, and OEM manufacturing sectors.' }],
})
</script>
