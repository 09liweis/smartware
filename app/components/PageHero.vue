<template>
  <section class="bg-gradient-to-r from-gray-900 to-blue-900 text-white py-20">
    <div class="container mx-auto px-4">
      <div class="max-w-4xl mx-auto" :class="{ 'text-center': centered }">
        <!-- Back Button (optional) -->
        <button
          v-if="showBackButton"
          class="text-gray-300 hover:text-white mb-4 flex items-center gap-2"
          @click="$router.back()"
        >
          ← {{ backButtonText }}
        </button>

        <!-- Title -->
        <h1 class="text-5xl font-bold mb-6 leading-tight">
          {{ title }}
        </h1>

        <!-- Subtitle -->
        <p
          v-if="subtitle"
          class="text-xl text-gray-300 mb-6"
          :class="centered ? 'max-w-3xl mx-auto' : ''"
        >
          {{ subtitle }}
        </p>

        <!-- Description -->
        <p
          v-if="description"
          class="text-gray-300"
          :class="centered ? 'max-w-3xl mx-auto text-xl mb-10' : 'mb-6'"
        >
          {{ description }}
        </p>

        <!-- Actions Slot -->
        <div v-if="$slots.actions" class="flex flex-col sm:flex-row gap-4" :class="{ 'justify-center': centered }">
          <slot name="actions" />
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
interface Props {
  title: string
  subtitle?: string
  description?: string
  centered?: boolean
  showBackButton?: boolean
  backButtonText?: string
}

withDefaults(defineProps<Props>(), {
  subtitle: '',
  description: '',
  centered: true,
  showBackButton: false,
  backButtonText: 'Back',
})
</script>
