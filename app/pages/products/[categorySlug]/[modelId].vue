<template>
  <div v-if="product">
    <!-- Breadcrumbs + Hero -->
    <PageHero
      :title="product.name"
      :subtitle="product.description?.substring(0, 200) + '...'"
      :centered="false"
      :breadcrumbs="[
        { label: 'Home', path: '/' },
        { label: 'B2B Technical Catalog', path: '/products' },
        { label: categoryTitle, path: `/products/${categorySlug}` },
        { label: product.name },
      ]"
    />

    <!-- PDP Main Section -->
    <section class="py-16 bg-[#121214]">
      <div class="max-w-7xl mx-auto px-4">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-12">
          <!-- Left: Product Photography -->
          <div>
            <div class="bg-[#1C1E22] border border-[#2D3139] rounded-sm p-6">
              <div class="aspect-square bg-[#121214] border border-[#2D3139] rounded-sm mb-4 flex items-center justify-center overflow-hidden">
                <img
                  v-if="mainImage"
                  :src="mainImage"
                  :alt="product.name"
                  class="max-h-full max-w-full object-contain filter brightness-95"
                />
                <div v-else class="text-center text-[#9A9EA6]">
                  <svg class="w-20 h-20 mx-auto mb-2 opacity-30" fill="currentColor" viewBox="0 0 20 20">
                    <path d="M11 3a1 1 0 10-2 0v1a1 1 0 102 0V3zM15.657 5.757a1 1 0 00-1.414-1.414l-.707.707a1 1 0 001.414 1.414l.707-.707zM18 10a1 1 0 01-1 1h-1a1 1 0 110-2h1a1 1 0 011 1zM5.05 6.464A1 1 0 106.464 5.05l-.707-.707a1 1 0 00-1.414 1.414l.707.707zM5 10a1 1 0 01-1 1H3a1 1 0 110-2h1a1 1 0 011 1zM8 16v-1h4v1a2 2 0 11-4 0zM12 14c.015-.34.208-.646.477-.859a4 4 0 10-4.954 0c.27.213.462.519.476.859h4.002z" />
                  </svg>
                  <p>No Image Available</p>
                </div>
              </div>

              <!-- Thumbnails -->
              <div v-if="validImages.length > 1" class="flex gap-2 overflow-x-auto pb-2">
                <button
                  v-for="(img, i) in validImages.slice(0, 6)"
                  :key="i"
                  @click="mainImage = img"
                  class="shrink-0 w-16 h-16 bg-[#121214] border rounded-sm overflow-hidden transition-colors"
                  :class="mainImage === img ? 'border-[#FF6B00]' : 'border-[#2D3139] hover:border-[#9A9EA6]'"
                >
                  <img :src="img" :alt="`${product.name} view ${i + 1}`" class="w-full h-full object-cover" />
                </button>
              </div>
            </div>
          </div>

          <!-- Right: Product Info & CTAs -->
          <div>
            <div class="flex items-center gap-3 mb-2">
              <h2 class="text-3xl font-extrabold text-white">{{ product.name }}</h2>
              <span class="text-xs font-mono bg-[#1C1E22] text-[#9A9EA6] px-2 py-1 rounded-sm border border-[#2D3139]">{{ product.name }}</span>
            </div>

            <p class="text-sm text-[#9A9EA6] mb-6 leading-relaxed">{{ product.description?.substring(0, 350) }}{{ product.description?.length > 350 ? '...' : '' }}</p>

            <!-- Stock Status -->
            <div class="flex items-center gap-2 mb-6 bg-emerald-950/20 border border-emerald-900/30 rounded-sm px-4 py-2">
              <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse-glow"></span>
              <span class="text-sm text-emerald-400 font-medium">Toronto Warehouse Stocked / OEM Production Available</span>
            </div>

            <!-- CTA Buttons -->
            <div class="flex flex-col sm:flex-row gap-3 mb-8">
              <button class="flex-1 bg-[#FF6B00] hover:bg-[#E65100] text-white text-sm font-bold py-3 px-6 rounded-sm transition-colors tracking-wide shadow-structural">
                Request Commercial Volume RFQ
              </button>
              <button class="flex-1 border border-[#2D3139] bg-[#1C1E22] hover:bg-[#2D3139] text-white text-sm font-medium py-3 px-6 rounded-sm transition-colors flex items-center justify-center gap-2">
                <svg class="w-4 h-4 text-[#9A9EA6]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v1m-4-4l-4 4m0 0l-4-4m4 4V4" /></svg>
                Download Dimensional Blueprint (PDF)
              </button>
            </div>

            <!-- Industry Tags -->
            <div class="mb-6">
              <h4 class="text-xs font-semibold text-[#9A9EA6] uppercase tracking-widest mb-2">Applicable Industries</h4>
              <div class="flex flex-wrap gap-2">
                <NuxtLink
                  v-for="industry in productIndustries"
                  :key="industry.slug"
                  :to="`/industries/${industry.slug}`"
                  class="text-xs bg-[#1C1E22] border border-[#2D3139] text-[#9A9EA6] hover:text-[#FF6B00] hover:border-[#FF6B00] px-3 py-1 rounded-sm transition-colors"
                >
                  {{ industry.label }}
                </NuxtLink>
              </div>
            </div>
          </div>
        </div>

        <!-- Technical Specification Matrix Table -->
        <div class="mt-16">
          <h3 class="text-2xl font-extrabold text-white mb-6">Technical Specification Matrix</h3>
          <div class="bg-[#1C1E22] border border-[#2D3139] rounded-sm overflow-hidden">
            <table class="w-full">
              <tbody>
                <tr
                  v-for="(value, key, index) in product.table_data"
                  :key="key"
                  class="border-b border-[#2D3139] last:border-b-0"
                  :class="index % 2 === 0 ? 'bg-[#121214]/30' : ''"
                >
                  <td class="py-4 px-6 text-sm font-semibold text-white w-1/3 border-r border-[#2D3139]">{{ key }}</td>
                  <td class="py-4 px-6 text-sm text-[#9A9EA6]">{{ value }}</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <!-- Deployment Instructions -->
        <div class="mt-12">
          <h3 class="text-2xl font-extrabold text-white mb-6">Deployment Guidelines</h3>
          <div class="bg-[#1C1E22] border border-[#2D3139] rounded-sm p-6">
            <ul class="space-y-3">
              <li class="flex items-start gap-3 text-sm text-[#9A9EA6]">
                <svg class="w-5 h-5 mt-0.5 text-[#FF6B00] shrink-0" fill="currentColor" viewBox="0 0 20 20">
                  <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
                </svg>
                Verify mounting surface integrity and bracket locking adjustments before operation.
              </li>
              <li class="flex items-start gap-3 text-sm text-[#9A9EA6]">
                <svg class="w-5 h-5 mt-0.5 text-[#FF6B00] shrink-0" fill="currentColor" viewBox="0 0 20 20">
                  <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
                </svg>
                Ensure all electrical connections comply with local codes and are protected from moisture ingress.
              </li>
              <li class="flex items-start gap-3 text-sm text-[#9A9EA6]">
                <svg class="w-5 h-5 mt-0.5 text-[#FF6B00] shrink-0" fill="currentColor" viewBox="0 0 20 20">
                  <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
                </svg>
                For battery-operated units, monitor charge state indicators regularly and follow prescribed charging cycles.
              </li>
              <li class="flex items-start gap-3 text-sm text-[#9A9EA6]">
                <svg class="w-5 h-5 mt-0.5 text-[#FF6B00] shrink-0" fill="currentColor" viewBox="0 0 20 20">
                  <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
                </svg>
                Inspect housing seals and gaskets quarterly for signs of degradation in extreme environments.
              </li>
            </ul>
          </div>
        </div>
      </div>
    </section>
  </div>

  <!-- Not Found -->
  <div v-else class="py-20 text-center bg-[#121214]">
    <div class="max-w-7xl mx-auto px-4">
      <h1 class="text-4xl font-bold text-white mb-4">Product Not Found</h1>
      <p class="text-[#9A9EA6] mb-8">The product you're looking for doesn't exist in our catalog.</p>
      <NuxtLink to="/products" class="bg-[#FF6B00] hover:bg-[#E65100] text-white py-3 px-8 rounded-sm font-bold transition-colors inline-block">
        Back to Catalog
      </NuxtLink>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useRoute, useRouter } from 'vue-router'
import ledLightsData from '@/led_lights.json'
import { PRODUCT_INDUSTRY_MAP, INDUSTRY_DETAILS } from '@/constants/navigation'

interface Product {
  name: string
  description: string
  images: string[]
  table_data: Record<string, string>
  source_url: string
}

const route = useRoute()
const router = useRouter()

const categorySlug = computed(() => route.params.categorySlug as string)
const modelId = computed(() => decodeURIComponent(route.params.modelId as string))

// Category slug -> data key mapping
const categoryToDataKey: Record<string, string> = {
  'rechargeable-work-lights': 'LED Rechargeable Work Light',
  'led-work-lights': 'LED Work Light',
  'led-light-bars': 'LED Light Bar',
  'led-tripods': 'LED Tripod',
}

const categoryTitle = computed(() => {
  const titles: Record<string, string> = {
    'rechargeable-work-lights': 'ProTask™ Cordless LED Rechargeable Series',
    'led-work-lights': 'DuraFlood™ Commercial Fixed LED Work Lights',
    'led-light-bars': 'HorizonView™ Ultra-Rugged LED Light Bars',
    'led-tripods': 'ApexTower™ Industrial Telescopic LED Tripod Systems',
  }
  return titles[categorySlug.value] || 'Products'
})

const products = computed<Product[]>(() => {
  const key = categoryToDataKey[categorySlug.value]
  if (!key) return []
  return ((ledLightsData as unknown) as Record<string, Product[]>)[key] || []
})

const product = computed<Product | undefined>(() => {
  return products.value.find(p => p.name === modelId.value)
})

// Industry tags for this product
const productIndustries = computed(() => {
  if (!product.value) return []
  // Find which data key this product belongs to
  const dataKey = categoryToDataKey[categorySlug.value]
  if (!dataKey) return []
  const industrySlugs = PRODUCT_INDUSTRY_MAP[dataKey] || []
  return industrySlugs.map(slug => {
    const detail = INDUSTRY_DETAILS.find(d => d.slug === slug)
    return { slug, label: detail?.title || slug }
  })
})

const validImages = computed(() => {
  if (!product.value?.images) return []
  return product.value.images.filter(img => !img.includes('imgbg.png'))
})

const mainImage = ref('')
watch(validImages, (imgs) => { mainImage.value = imgs[0] || '' }, { immediate: true })

// SEO
useHead({
  title: computed(() => product.value ? `${product.value.name} | SST-Smartware` : 'Product Not Found'),
  meta: [{ name: 'description', content: computed(() => product.value?.description?.substring(0, 160) || '') }],
})
</script>
