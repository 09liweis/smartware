<template>
  <section class="bg-[#1C1E22] border-b border-[#2D3139] py-20">
    <div class="max-w-7xl mx-auto px-4">
      <div :class="{ 'text-center': centered, 'max-w-4xl mx-auto': centered }">
        <!-- Breadcrumbs -->
        <div v-if="breadcrumbs && breadcrumbs.length > 0" class="flex items-center gap-2 text-xs text-[#9A9EA6] mb-4">
          <template v-for="(crumb, i) in breadcrumbs" :key="i">
            <NuxtLink v-if="crumb.path" :to="crumb.path" class="hover:text-white transition-colors">{{ crumb.label }}</NuxtLink>
            <span v-else class="text-white">{{ crumb.label }}</span>
            <svg v-if="i < breadcrumbs.length - 1" class="w-3 h-3 text-[#2D3139]" fill="currentColor" viewBox="0 0 20 20">
              <path fill-rule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clip-rule="evenodd" />
            </svg>
          </template>
        </div>

        <!-- Title -->
        <h1 class="text-4xl md:text-5xl font-extrabold mb-4 leading-tight text-white">
          {{ title }}
        </h1>

        <!-- Subtitle -->
        <p v-if="subtitle" class="text-lg text-[#9A9EA6] mb-4" :class="centered ? 'max-w-3xl mx-auto' : ''">
          {{ subtitle }}
        </p>

        <!-- Description -->
        <p v-if="description" class="text-[#9A9EA6]" :class="centered ? 'max-w-3xl mx-auto text-lg mb-8' : 'mb-6'">
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
interface Breadcrumb {
  label: string
  path?: string
}

interface Props {
  title: string
  subtitle?: string
  description?: string
  centered?: boolean
  breadcrumbs?: Breadcrumb[]
}

withDefaults(defineProps<Props>(), {
  subtitle: '',
  description: '',
  centered: true,
  breadcrumbs: () => [],
})
</script>
