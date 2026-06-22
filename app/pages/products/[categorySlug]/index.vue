<template>
  <div>
    <PageHero
      :title="categoryTitle"
      :subtitle="categorySubtitle"
      :breadcrumbs="[
        { label: 'Home', path: '/' },
        { label: 'B2B Technical Catalog', path: '/products' },
        { label: categoryTitle },
      ]"
    />

    <section class="py-16 bg-[#121214]">
      <div class="max-w-7xl mx-auto px-4">
        <div class="flex flex-col lg:flex-row gap-8">
          <!-- Left Sidebar: Faceted Filters -->
          <aside class="w-full lg:w-1/4 shrink-0">
            <div class="bg-[#1C1E22] border border-[#2D3139] rounded-sm p-5 sticky top-20">
              <h3 class="text-sm font-bold text-white uppercase tracking-widest mb-4">Technical Filters</h3>

              <!-- Filter groups -->
              <div v-for="group in filterGroups" :key="group.label" class="mb-6 last:mb-0">
                <h4 class="text-xs font-semibold text-[#9A9EA6] uppercase tracking-wide mb-3">{{ group.label }}</h4>
                <div class="space-y-2">
                  <label
                    v-for="filter in group.options"
                    :key="filter.value"
                    class="flex items-center gap-2 cursor-pointer group/filter"
                  >
                    <input
                      type="checkbox"
                      :value="filter.value"
                      v-model="selectedFilters"
                      class="w-4 h-4 rounded-sm border-[#2D3139] bg-[#121214] text-[#FF6B00] focus:ring-[#FF6B00] focus:ring-offset-0"
                    />
                    <span class="text-sm text-[#9A9EA6] group-hover/filter:text-white transition-colors">{{ filter.label }}</span>
                    <span class="text-xs text-[#9A9EA6] ml-auto opacity-50">{{ filter.count }}</span>
                  </label>
                </div>
              </div>

              <button
                v-if="selectedFilters.length > 0"
                @click="selectedFilters = []"
                class="mt-4 w-full border border-[#2D3139] text-[#9A9EA6] hover:text-white hover:border-white text-xs py-2 rounded-sm transition-colors"
              >
                Clear All Filters
              </button>
            </div>
          </aside>

          <!-- Right Side: Product Rows -->
          <div class="w-full lg:w-3/4">
            <!-- Results count -->
            <div class="flex items-center justify-between mb-4">
              <p class="text-sm text-[#9A9EA6]">
                Showing <span class="text-white font-semibold">{{ filteredProducts.length }}</span>
                of <span class="text-white font-semibold">{{ products.length }}</span> models
              </p>
            </div>

            <!-- Empty state -->
            <div v-if="filteredProducts.length === 0" class="bg-[#1C1E22] border border-[#2D3139] rounded-sm p-12 text-center">
              <p class="text-[#9A9EA6] text-lg">No products match the selected filters.</p>
              <button @click="selectedFilters = []" class="mt-4 text-[#FF6B00] hover:text-[#E65100] text-sm font-semibold">Clear all filters</button>
            </div>

            <!-- Product Rows - Banner Engineering Matrix Style -->
            <div v-for="product in filteredProducts" :key="product.name" class="flex flex-col md:flex-row items-center justify-between border border-[#2D3139] bg-[#1C1E22] p-6 rounded-sm shadow-structural hover:border-[#FF6B00] transition-all mb-4 group">
              <!-- Left: Image & Tech Parameters -->
              <div class="flex flex-col sm:flex-row items-center gap-6 w-full md:w-3/5 cursor-pointer" @click="navigateToProduct(product.name)">
                <!-- Image Box -->
                <div class="w-32 h-32 bg-[#121214] flex items-center justify-center p-2 border border-[#2D3139] rounded-sm shrink-0">
                  <img
                    v-if="product.images && product.images.length > 0"
                    :src="product.images[0]"
                    :alt="product.name"
                    class="max-h-full object-contain filter brightness-90"
                    @error="($event.target as HTMLImageElement).style.display='none'"
                  />
                  <svg v-else class="w-12 h-12 text-[#2D3139]" fill="currentColor" viewBox="0 0 20 20">
                    <path d="M11 3a1 1 0 10-2 0v1a1 1 0 102 0V3zM15.657 5.757a1 1 0 00-1.414-1.414l-.707.707a1 1 0 001.414 1.414l.707-.707zM18 10a1 1 0 01-1 1h-1a1 1 0 110-2h1a1 1 0 011 1zM5.05 6.464A1 1 0 106.464 5.05l-.707-.707a1 1 0 00-1.414 1.414l.707.707zM5 10a1 1 0 01-1 1H3a1 1 0 110-2h1a1 1 0 011 1zM8 16v-1h4v1a2 2 0 11-4 0zM12 14c.015-.34.208-.646.477-.859a4 4 0 10-4.954 0c.27.213.462.519.476.859h4.002z" />
                  </svg>
                </div>

                <!-- Title and Metadata -->
                <div class="text-center sm:text-left">
                  <div class="flex flex-wrap items-center justify-center sm:justify-start gap-3 mb-1">
                    <h3 class="text-xl font-bold text-white group-hover:text-[#FF6B00] transition-colors">{{ product.name }}</h3>
                    <span class="text-xs font-mono bg-[#121214] text-[#9A9EA6] px-2 py-0.5 rounded-sm border border-[#2D3139]">{{ product.name }}</span>
                  </div>
                  <p class="text-sm text-[#9A9EA6] mb-3 line-clamp-2">{{ product.description?.substring(0, 150) }}</p>

                  <!-- Technical Param Badges -->
                  <div class="flex flex-wrap justify-center sm:justify-start gap-2">
                    <span v-if="product.table_data?.Lumens" class="text-xs font-semibold bg-blue-950/40 text-blue-400 px-2.5 py-1 rounded-sm border border-blue-900/50">{{ product.table_data.Lumens }}</span>
                    <span v-if="product.table_data?.['Input Voltage']" class="text-xs font-semibold bg-orange-950/40 text-orange-400 px-2.5 py-1 rounded-sm border border-orange-900/50">{{ getPowerType(product) }}</span>
                    <span v-if="product.table_data?.['IP Rate']" class="text-xs font-semibold bg-green-950/40 text-green-400 px-2.5 py-1 rounded-sm border border-green-900/50">{{ product.table_data['IP Rate'] }}</span>
                    <span v-if="product.table_data?.['Beam Angle']" class="text-xs font-semibold bg-purple-950/40 text-purple-400 px-2.5 py-1 rounded-sm border border-purple-900/50">{{ product.table_data['Beam Angle'] }}</span>
                    <span v-if="product.table_data?.Warranty" class="text-xs font-semibold bg-emerald-950/40 text-emerald-400 px-2.5 py-1 rounded-sm border border-emerald-900/50">{{ product.table_data.Warranty }}</span>
                  </div>
                </div>
              </div>

              <!-- Right: B2B Procurement Action Station -->
              <div class="flex flex-col sm:flex-row md:flex-col gap-2 w-full md:w-1/5 mt-4 md:mt-0 border-t md:border-t-0 md:border-l border-[#2D3139] pt-4 md:pt-0 md:pl-6">
                <div class="text-xs text-center md:text-right text-emerald-400 font-medium mb-1 flex items-center justify-center md:justify-end gap-1">
                  <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse-glow"></span> OEM Open
                </div>
                <button class="w-full bg-[#FF6B00] hover:bg-[#E65100] text-white text-sm font-bold py-2.5 px-4 rounded-sm transition-colors tracking-wide shadow-structural" @click="$router.push('/contact')">
                  Request Bulk Quote
                </button>
                <button class="w-full border border-[#2D3139] bg-[#121214] hover:bg-[#2D3139] text-white text-sm font-medium py-2 px-4 rounded-sm transition-colors flex items-center justify-center gap-1">
                  <svg class="w-4 h-4 text-[#9A9EA6]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v1m-4-4l-4 4m0 0l-4-4m4 4V4" /></svg>
                  Download Spec Sheet
                </button>
                <button class="w-full text-xs text-[#9A9EA6] hover:text-white transition-colors flex items-center justify-center gap-1 mt-1" @click="navigateToProduct(product.name)">
                  View Engineering Blueprints →
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'
import ledLightsData from '@/led_lights.json'

interface Product {
  name: string
  description: string
  images: string[]
  table_data: Record<string, string>
  source_url: string
}

const router = useRouter()

// Category slug mapping
const categoryMap: Record<string, { title: string; subtitle: string; dataKey: string; filters: { label: string; options: { label: string; value: string; count: number }[] }[] }> = {
  'rechargeable-work-lights': {
    title: 'ProTask™ Cordless LED Rechargeable Series',
    subtitle: 'Industrial-capacity lithium-ion portable task gear built for continuous field deployment and maintenance operations.',
    dataKey: 'LED Rechargeable Work Light',
    filters: [
      {
        label: 'By Application',
        options: [
          { label: 'Integrated Magnetic Base', value: 'magnetic', count: 18 },
          { label: 'Non-Magnetic Stand / Hook', value: 'non-magnetic', count: 4 },
        ],
      },
      {
        label: 'By Lumen Output',
        options: [
          { label: '1k–3k lm', value: '1k-3k', count: 12 },
          { label: '3k–5k lm', value: '3k-5k', count: 6 },
          { label: '5k+ lm', value: '5k-plus', count: 4 },
        ],
      },
      {
        label: 'By Power Input',
        options: [
          { label: 'Rechargeable USB-C', value: 'usb-c', count: 15 },
          { label: 'AC Plug-In', value: 'ac', count: 10 },
          { label: '12V-24V DC Mobile', value: 'dc', count: 8 },
        ],
      },
    ],
  },
  'led-work-lights': {
    title: 'DuraFlood™ Commercial Fixed LED Work Lights',
    subtitle: 'Heavy-duty corded site illumination built for continuous overhead mounting and industrial bay configurations.',
    dataKey: 'LED Work Light',
    filters: [
      {
        label: 'By Power Class',
        options: [
          { label: 'Light Duty (≤30W)', value: 'light', count: 12 },
          { label: 'Medium Duty (<60W)', value: 'medium', count: 14 },
          { label: 'Heavy Duty (≥60W)', value: 'heavy', count: 10 },
        ],
      },
      {
        label: 'By Lumen Output',
        options: [
          { label: '1k–3k lm', value: '1k-3k', count: 8 },
          { label: '3k–5k lm', value: '3k-5k', count: 12 },
          { label: '5k+ lm', value: '5k-plus', count: 16 },
        ],
      },
      {
        label: 'By Power Input',
        options: [
          { label: 'AC Plug-In', value: 'ac', count: 30 },
          { label: '12V-24V DC Mobile', value: 'dc', count: 6 },
        ],
      },
    ],
  },
  'led-light-bars': {
    title: 'HorizonView™ Ultra-Rugged LED Light Bars',
    subtitle: 'Long-range combo spot/flood peripheral lighting bars optimized for commercial fleets and field service trucks.',
    dataKey: 'LED Light Bar',
    filters: [
      {
        label: 'By Beam Optics',
        options: [
          { label: 'Spot Beam Optics', value: 'spot', count: 7 },
          { label: 'Flood Array Optics', value: 'flood', count: 7 },
          { label: 'Combo Precision Optics', value: 'combo', count: 7 },
        ],
      },
      {
        label: 'By Lumen Output',
        options: [
          { label: '1k–3k lm', value: '1k-3k', count: 6 },
          { label: '3k–5k lm', value: '3k-5k', count: 8 },
          { label: '5k+ lm', value: '5k-plus', count: 7 },
        ],
      },
      {
        label: 'By Power Input',
        options: [
          { label: '12V-24V DC Mobile', value: 'dc', count: 21 },
        ],
      },
    ],
  },
  'led-tripods': {
    title: 'ApexTower™ Industrial Telescopic LED Tripod Systems',
    subtitle: 'High-stature site tower infrastructure extending up to 10 feet for rapid jobsite shadow mitigation.',
    dataKey: 'LED Tripod',
    filters: [
      {
        label: 'By Power Source',
        options: [
          { label: 'Continuous AC Utility Power', value: 'ac', count: 10 },
          { label: 'Cordless Lithium Rechargeable', value: 'battery', count: 10 },
        ],
      },
      {
        label: 'By Lumen Output',
        options: [
          { label: '3k–5k lm', value: '3k-5k', count: 6 },
          { label: '5k+ lm', value: '5k-plus', count: 14 },
        ],
      },
    ],
  },
}

const route = useRoute()
const categorySlug = computed(() => route.params.categorySlug as string)
const config = computed(() => categoryMap[categorySlug.value])

const categoryTitle = computed(() => config.value?.title || 'Products')
const categorySubtitle = computed(() => config.value?.subtitle || '')
const filterGroups = computed(() => config.value?.filters || [])

const products = computed<Product[]>(() => {
  const key = config.value?.dataKey
  if (!key) return []
  return ((ledLightsData as unknown) as Record<string, Product[]>)[key] || []
})

const selectedFilters = ref<string[]>([])

const filteredProducts = computed(() => {
  if (selectedFilters.value.length === 0) return products.value
  // For now return all products — filters would need specific logic per category
  return products.value
})

function getPowerType(product: Product): string {
  const voltage = product.table_data?.['Input Voltage'] || ''
  if (voltage.includes('AC')) return 'AC/DC Hybrid'
  if (voltage.includes('DC')) return 'DC Powered'
  return 'Multi-Input'
}

function navigateToProduct(productName: string) {
  router.push(`/products/${categorySlug.value}/${encodeURIComponent(productName)}`)
}

// SEO
useHead({
  title: computed(() => `${categoryTitle.value} | SST-Smartware`),
  meta: [{ name: 'description', content: computed(() => categorySubtitle.value) }],
})
</script>
