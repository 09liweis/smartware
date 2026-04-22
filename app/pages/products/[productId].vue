<template>
  <div v-if="product">
    <!-- Hero Section -->
    <section class="bg-gradient-to-r from-gray-900 to-blue-900 text-white py-16">
      <div class="container mx-auto px-4">
        <div class="max-w-4xl mx-auto">
          <button
            class="text-gray-300 hover:text-white mb-4 flex items-center gap-2"
            @click="$router.back()"
          >
            ← Back to Products
          </button>
          <h1 class="text-4xl md:text-5xl font-bold mb-4 leading-tight">
            {{ product.name }}
          </h1>
          <p class="text-xl text-gray-300">
            {{ product.description?.substring(0, 200) }}...
          </p>
        </div>
      </div>
    </section>

    <!-- Product Details -->
    <section class="py-16">
      <div class="container mx-auto px-4">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-12">
          <!-- Image Gallery -->
          <div>
            <div class="bg-gray-100 rounded-xl p-8 mb-6">
              <div class="aspect-square bg-white rounded-lg mb-6 flex items-center justify-center overflow-hidden">
                <img
                  v-if="mainImage"
                  :src="mainImage"
                  :alt="product.name"
                  class="max-h-full max-w-full object-contain"
                />
                <div v-else class="text-center text-gray-400">
                  <svg class="w-32 h-32 mx-auto mb-4" fill="currentColor" viewBox="0 0 20 20">
                    <path d="M11 3a1 1 0 10-2 0v1a1 1 0 102 0V3zM15.657 5.757a1 1 0 00-1.414-1.414l-.707.707a1 1 0 001.414 1.414l.707-.707zM18 10a1 1 0 01-1 1h-1a1 1 0 110-2h1a1 1 0 011 1zM5.05 6.464A1 1 0 106.464 5.05l-.707-.707a1 1 0 00-1.414 1.414l.707.707zM5 10a1 1 0 01-1 1H3a1 1 0 110-2h1a1 1 0 011 1zM8 16v-1h4v1a2 2 0 11-4 0zM12 14c.015-.34.208-.646.477-.859a4 4 0 10-4.954 0c.27.213.462.519.476.859h4.002z" />
                  </svg>
                  <p class="text-lg">No Image Available</p>
                </div>
              </div>

              <!-- Thumbnail Gallery -->
              <div v-if="product.images && product.images.length > 1" class="flex gap-3 overflow-x-auto pb-2">
                <button
                  v-for="(img, index) in validImages"
                  :key="index"
                  class="flex-shrink-0 w-20 h-20 rounded-lg overflow-hidden border-2 transition-colors"
                  :class="mainImage === img ? 'border-blue-600' : 'border-gray-200 hover:border-gray-400'"
                  @click="mainImage = img"
                >
                  <img
                    :src="img"
                    :alt="`${product.name} - ${index + 1}`"
                    class="w-full h-full object-cover"
                  />
                </button>
              </div>
            </div>

            <div class="flex gap-4">
              <button class="flex-1 bg-blue-600 hover:bg-blue-700 text-white py-3 rounded-lg font-semibold transition-colors">
                Request Quote
              </button>
              <button class="flex-1 border-2 border-blue-600 text-blue-600 hover:bg-blue-50 py-3 rounded-lg font-semibold transition-colors">
                Download Spec Sheet
              </button>
            </div>
          </div>

          <!-- Technical Specs -->
          <div>
            <h2 class="text-3xl font-bold mb-6">Technical Specifications</h2>
            <div class="bg-white rounded-xl shadow-lg overflow-hidden">
              <table class="w-full">
                <tbody>
                  <tr
                    v-for="(value, key, index) in product.table_data"
                    :key="key"
                    class="border-b border-gray-200 last:border-b-0"
                    :class="index % 2 === 1 ? 'bg-gray-50' : ''"
                  >
                    <td class="py-4 px-6 font-semibold text-gray-700 w-1/3">{{ key }}</td>
                    <td class="py-4 px-6 text-gray-600">{{ value }}</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <!-- Description -->
            <div class="mt-8">
              <h2 class="text-2xl font-bold mb-4">Description</h2>
              <p class="text-gray-600 leading-relaxed">{{ product.description }}</p>
            </div>

            <!-- Source Link -->
            <div class="mt-8">
              <a
                :href="product.source_url"
                target="_blank"
                rel="noopener noreferrer"
                class="text-blue-600 hover:text-blue-800 font-medium"
              >
                View on Manufacturer Website →
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Related Products -->
    <section class="py-16 bg-gray-50">
      <div class="container mx-auto px-4">
        <div class="text-center mb-12">
          <h2 class="text-3xl font-bold mb-4">Related Products</h2>
          <p class="text-gray-600">Explore more products from our collection</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-5xl mx-auto">
          <div
            v-for="relatedProduct in relatedProducts"
            :key="relatedProduct.name"
            class="bg-white rounded-xl shadow-lg overflow-hidden cursor-pointer hover:shadow-xl transition-shadow"
            @click="navigateToProduct(relatedProduct.name)"
          >
            <div class="h-48 bg-gradient-to-br from-gray-100 to-gray-200 flex items-center justify-center p-4">
              <img
                v-if="relatedProduct.images && relatedProduct.images.length > 0"
                :src="relatedProduct.images[0]"
                :alt="relatedProduct.name"
                class="max-h-full max-w-full object-contain"
              />
              <div v-else class="text-center text-gray-400">
                <svg class="w-16 h-16 mx-auto" fill="currentColor" viewBox="0 0 20 20">
                  <path d="M11 3a1 1 0 10-2 0v1a1 1 0 102 0V3zM15.657 5.757a1 1 0 00-1.414-1.414l-.707.707a1 1 0 001.414 1.414l.707-.707zM18 10a1 1 0 01-1 1h-1a1 1 0 110-2h1a1 1 0 011 1zM5.05 6.464A1 1 0 106.464 5.05l-.707-.707a1 1 0 00-1.414 1.414l.707.707zM5 10a1 1 0 01-1 1H3a1 1 0 110-2h1a1 1 0 011 1zM8 16v-1h4v1a2 2 0 11-4 0zM12 14c.015-.34.208-.646.477-.859a4 4 0 10-4.954 0c.27.213.462.519.476.859h4.002z" />
                </svg>
              </div>
            </div>
            <div class="p-6">
              <h3 class="text-lg font-bold mb-2">{{ relatedProduct.name }}</h3>
              <p class="text-gray-600 text-sm line-clamp-2">{{ relatedProduct.description?.substring(0, 100) }}...</p>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>

  <!-- Not Found -->
  <div v-else class="py-20 text-center">
    <div class="container mx-auto px-4">
      <h1 class="text-4xl font-bold mb-4">Product Not Found</h1>
      <p class="text-gray-600 mb-8">The product you're looking for doesn't exist.</p>
      <button
        class="bg-blue-600 hover:bg-blue-700 text-white py-3 px-8 rounded-lg font-semibold transition-colors"
        @click="$router.push('/products')"
      >
        Back to Products
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useRoute, useRouter } from 'vue-router'
import ledLightsData from '@/led_lights.json'

interface Product {
  name: string
  description: string
  images: string[]
  table_data: Record<string, string>
  source_url: string
}

const route = useRoute()
const router = useRouter()
const productId = computed(() => decodeURIComponent(route.params.productId as string))

// Get all products flattened
const allProducts = computed<Product[]>(() => {
  const products: Product[] = []
  for (const category of Object.values(ledLightsData)) {
    if (Array.isArray(category)) {
      products.push(...category)
    }
  }
  return products
})

// Find current product
const product = computed<Product | undefined>(() => {
  return allProducts.value.find(p => p.name === productId.value)
})

// Filter out placeholder images
const validImages = computed(() => {
  if (!product.value?.images) return []
  return product.value.images.filter(img => !img.includes('imgbg.png'))
})

// Main display image
const mainImage = ref('')

watch(validImages, (images) => {
  mainImage.value = images[0] || ''
}, { immediate: true })

// Get related products (random 3 excluding current)
const relatedProducts = computed<Product[]>(() => {
  if (!product.value) return []
  const others = allProducts.value.filter(p => p.name !== product.value?.name)
  return others.slice(0, 3)
})

function navigateToProduct(productName: string) {
  router.push(`/products/${encodeURIComponent(productName)}`)
}

// SEO
useHead({
  title: computed(() => product.value ? `${product.value.name} - LED Work Light` : 'Product Not Found'),
  meta: [
    {
      name: 'description',
      content: computed(() => product.value?.description?.substring(0, 160) || ''),
    },
  ],
})
</script>
