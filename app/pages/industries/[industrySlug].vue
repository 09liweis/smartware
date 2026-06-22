<template>
  <div v-if="industry">
    <PageHero
      :title="industry.title"
      :subtitle="industry.applicationText"
      :breadcrumbs="[
        { label: 'Home', path: '/' },
        { label: 'Industries & Solutions', path: '/industries' },
        { label: industry.title },
      ]"
    />

    <!-- Industry Detail -->
    <section class="py-16 bg-[#121214]">
      <div class="max-w-7xl mx-auto px-4">
        <!-- Technical Focus -->
        <div class="max-w-4xl mx-auto mb-16">
          <div class="bg-[#1C1E22] border border-[#2D3139] rounded-sm p-8">
            <h3 class="text-lg font-bold text-white mb-4">Technical Focus</h3>
            <p class="text-[#9A9EA6] leading-relaxed">{{ industry.focus }}</p>
          </div>
        </div>

        <!-- Product Categories Grid -->
        <div class="mb-16">
          <h3 class="text-2xl font-extrabold text-white mb-8 text-center">Mapped Product Categories</h3>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6 max-w-4xl mx-auto">
            <NuxtLink
              v-for="cat in industryProductCategories"
              :key="cat.path"
              :to="cat.path"
              class="bg-[#1C1E22] border border-[#2D3139] rounded-sm p-8 hover:border-[#FF6B00] transition-all group"
            >
              <div class="flex items-start justify-between mb-4">
                <h4 class="text-lg font-bold text-white group-hover:text-[#FF6B00] transition-colors">{{ cat.label }}</h4>
                <span class="text-xs font-mono text-[#9A9EA6] bg-[#121214] px-2 py-0.5 rounded-sm border border-[#2D3139]">{{ cat.count }} Models</span>
              </div>
              <p class="text-sm text-[#9A9EA6] mb-6">{{ cat.description }}</p>
              <div class="flex items-center text-sm font-semibold text-[#FF6B00]">
                Explore Matrix
                <svg class="w-4 h-4 ml-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" /></svg>
              </div>
            </NuxtLink>
          </div>
        </div>

        <!-- Sourced Hardware Entry Points -->
        <div class="max-w-4xl mx-auto mb-16">
          <h3 class="text-2xl font-extrabold text-white mb-8 text-center">Sourced Hardware Entry Points</h3>
          <div class="flex flex-wrap justify-center gap-4">
            <NuxtLink
              v-for="link in industry.hardwareLinks"
              :key="link.path"
              :to="link.path"
              class="inline-flex items-center gap-2 text-base font-bold text-[#FF6B00] hover:text-white bg-[#1C1E22] border border-[#2D3139] hover:border-[#FF6B00] px-6 py-3 rounded-sm transition-all"
            >
              {{ link.label }}
            </NuxtLink>
          </div>
        </div>

        <!-- Featured Products Preview -->
        <div class="max-w-4xl mx-auto" v-if="previewProducts.length > 0">
          <h3 class="text-2xl font-extrabold text-white mb-8 text-center">Representative Hardware</h3>
          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
            <div
              v-for="product in previewProducts.slice(0, 6)"
              :key="product.name"
              class="bg-[#1C1E22] border border-[#2D3139] rounded-sm p-4 hover:border-[#FF6B00] transition-all group cursor-pointer"
              @click="navigateToProduct(product.categorySlug, product.name)"
            >
              <div class="w-full h-32 bg-[#121214] border border-[#2D3139] rounded-sm flex items-center justify-center mb-3 overflow-hidden">
                <img
                  v-if="product.images && product.images.length > 0"
                  :src="product.images[0]"
                  :alt="product.name"
                  class="max-h-full object-contain filter brightness-90"
                  @error="($event.target as HTMLImageElement).style.display='none'"
                />
                <svg v-else class="w-8 h-8 text-[#2D3139]" fill="currentColor" viewBox="0 0 20 20">
                  <path d="M11 3a1 1 0 10-2 0v1a1 1 0 102 0V3zM15.657 5.757a1 1 0 00-1.414-1.414l-.707.707a1 1 0 001.414 1.414l.707-.707zM18 10a1 1 0 01-1 1h-1a1 1 0 110-2h1a1 1 0 011 1z" />
                </svg>
              </div>
              <h4 class="text-sm font-bold text-white group-hover:text-[#FF6B00] transition-colors">{{ product.name }}</h4>
              <p class="text-xs text-[#9A9EA6] mt-1 line-clamp-2">{{ product.description?.substring(0, 80) }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA -->
    <section class="py-20 bg-[#1C1E22] border-t border-[#2D3139]">
      <div class="max-w-3xl mx-auto px-4 text-center">
        <h2 class="text-3xl font-extrabold text-white mb-4">Ready to Source for {{ industry.title }}?</h2>
        <p class="text-[#9A9EA6] mb-8">Our Toronto account team will match your operational requirements to the right hardware configuration.</p>
        <NuxtLink to="/contact" class="inline-block bg-[#FF6B00] hover:bg-[#E65100] text-white px-8 py-4 rounded-sm text-base font-bold transition-colors tracking-wide shadow-structural">
          Request Industry-Specific RFQ
        </NuxtLink>
      </div>
    </section>
  </div>

  <!-- Not Found -->
  <div v-else class="py-20 text-center bg-[#121214]">
    <div class="max-w-7xl mx-auto px-4">
      <h1 class="text-4xl font-bold text-white mb-4">Industry Not Found</h1>
      <NuxtLink to="/industries" class="text-[#FF6B00] hover:text-[#E65100] font-semibold">View All Industries</NuxtLink>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'
import ledLightsData from '@/led_lights.json'
import { INDUSTRY_DETAILS, PRODUCT_INDUSTRY_MAP } from '@/constants/navigation'

const route = useRoute()
const router = useRouter()
const industrySlug = computed(() => route.params.industrySlug as string)

const industry = computed(() => INDUSTRY_DETAILS.find(d => d.slug === industrySlug.value))

// Map industry product categories to links
const categoryToSlug: Record<string, string> = {
  'LED Rechargeable Work Light': 'rechargeable-work-lights',
  'LED Work Light': 'led-work-lights',
  'LED Light Bar': 'led-light-bars',
  'LED Tripod': 'led-tripods',
}

const categoryLabels: Record<string, { label: string; description: string }> = {
  'LED Rechargeable Work Light': { label: 'ProTask™ Cordless Rechargeable Series', description: 'Portable cordless task lighting with industrial magnetic mounting or multi-position stands.' },
  'LED Work Light': { label: 'DuraFlood™ Fixed Work Lights', description: 'Rugged corded flood arrays across Light, Medium, and Heavy Duty power brackets.' },
  'LED Light Bar': { label: 'HorizonView™ LED Light Bars', description: 'Low-profile, high-intensity illumination for low-voltage fleet vehicle deployment.' },
  'LED Tripod': { label: 'ApexTower™ Telescopic Tripod Systems', description: 'Rapid-deployment site tower masts up to 10 feet for jobsite shadow mitigation.' },
}

const industryProductCategories = computed(() => {
  if (!industry.value) return []
  return industry.value.productCategories.map(cat => ({
    label: categoryLabels[cat]?.label || cat,
    description: categoryLabels[cat]?.description || '',
    path: `/products/${categoryToSlug[cat] || ''}`,
    count: ((ledLightsData as unknown) as Record<string, any[]>)[cat]?.length || 0,
  }))
})

interface PreviewProduct {
  name: string
  description: string
  images: string[]
  categorySlug: string
}

const previewProducts = computed<PreviewProduct[]>(() => {
  if (!industry.value) return []
  const results: PreviewProduct[] = []
  for (const cat of industry.value.productCategories) {
    const products = ((ledLightsData as unknown) as Record<string, any[]>)[cat] || []
    const slug = categoryToSlug[cat] || ''
    for (const p of products.slice(0, 2)) {
      results.push({ ...p, categorySlug: slug })
    }
  }
  return results
})

function navigateToProduct(catSlug: string, productName: string) {
  router.push(`/products/${catSlug}/${encodeURIComponent(productName)}`)
}

useHead({
  title: computed(() => industry.value ? `${industry.value.title} | SST-Smartware` : 'Industry Not Found'),
  meta: [{ name: 'description', content: computed(() => industry.value?.applicationText || '') }],
})
</script>
