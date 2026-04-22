<template>
  <div>
    <!-- Hero Section -->
    <section class="bg-gradient-to-r from-gray-900 to-blue-900 text-white py-20">
      <div class="container mx-auto px-4">
        <div class="max-w-4xl mx-auto text-center">
          <h1 class="text-5xl font-bold mb-6 leading-tight">
            LED Work Lights
          </h1>
          <p class="text-xl text-gray-300 mb-6">
            Professional-grade rechargeable LED work lights for industrial, emergency, and outdoor applications
          </p>
        </div>
      </div>
    </section>

    <!-- Products Grid -->
    <section class="py-20">
      <div class="container mx-auto px-4">
        <div class="text-center mb-16">
          <h2 class="text-4xl font-bold mb-6">Our Products</h2>
          <p class="text-gray-600 max-w-2xl mx-auto text-lg">
            Explore our full range of high-performance LED lighting solutions
          </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          <div
            v-for="product in allProducts"
            :key="product.name"
            class="bg-white rounded-xl shadow-lg overflow-hidden hover:shadow-2xl transition-shadow cursor-pointer"
            @click="navigateToProduct(product.name)"
          >
            <div class="h-64 bg-gradient-to-br from-gray-100 to-gray-200 flex items-center justify-center p-4">
              <img
                v-if="product.images && product.images.length > 0"
                :src="product.images[0]"
                :alt="product.name"
                class="max-h-full max-w-full object-contain"
                @error="$event.target.style.display='none'"
              />
              <div v-else class="text-center text-gray-400">
                <svg class="w-20 h-20 mx-auto mb-2" fill="currentColor" viewBox="0 0 20 20">
                  <path d="M11 3a1 1 0 10-2 0v1a1 1 0 102 0V3zM15.657 5.757a1 1 0 00-1.414-1.414l-.707.707a1 1 0 001.414 1.414l.707-.707zM18 10a1 1 0 01-1 1h-1a1 1 0 110-2h1a1 1 0 011 1zM5.05 6.464A1 1 0 106.464 5.05l-.707-.707a1 1 0 00-1.414 1.414l.707.707zM5 10a1 1 0 01-1 1H3a1 1 0 110-2h1a1 1 0 011 1zM8 16v-1h4v1a2 2 0 11-4 0zM12 14c.015-.34.208-.646.477-.859a4 4 0 10-4.954 0c.27.213.462.519.476.859h4.002z" />
                </svg>
                <p>No Image</p>
              </div>
            </div>
            <div class="p-6">
              <h3 class="text-xl font-bold mb-2">{{ product.name }}</h3>
              <p class="text-gray-600 mb-4 line-clamp-2">{{ product.description?.substring(0, 120) }}...</p>
              <div class="flex items-center justify-between">
                <span v-if="product.table_data?.Lumens" class="text-sm text-blue-600 font-semibold">
                  {{ product.table_data.Lumens }}
                </span>
                <button class="text-blue-600 hover:text-blue-800 font-medium">
                  View Details →
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
import { generateSeoMeta, seoConfigs } from '@/utils/seo'
import ledLightsData from '@/led_lights.json'

interface Product {
  name: string
  description: string
  images: string[]
  table_data: Record<string, string>
  source_url: string
}

definePageMeta({
  ...generateSeoMeta(seoConfigs.products),
})

// Flatten all products from all categories
const allProducts = computed<Product[]>(() => {
  const products: Product[] = []
  for (const category of Object.values(ledLightsData)) {
    if (Array.isArray(category)) {
      products.push(...category)
    }
  }
  return products
})

const router = useRouter()

function navigateToProduct(productName: string) {
  router.push(`/products/${encodeURIComponent(productName)}`)
}
</script>
