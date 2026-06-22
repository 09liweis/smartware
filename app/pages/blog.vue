<template>
  <div>
    <PageHero
      title="The Knowledge Hub"
      description="Industry insights, technical expertise, and innovation updates from the SST-Smartware team"
      :breadcrumbs="[
        { label: 'Home', path: '/' },
        { label: 'Blog' },
      ]"
    />

    <!-- Category Filter -->
    <section class="py-8 bg-[#1C1E22] border-b border-[#2D3139]">
      <div class="max-w-7xl mx-auto px-4">
        <div class="flex flex-wrap gap-3 justify-center">
          <button class="bg-[#FF6B00] text-white px-5 py-2 rounded-sm text-sm font-semibold">All Articles</button>
          <button class="border border-[#2D3139] text-[#9A9EA6] hover:text-white hover:border-white px-5 py-2 rounded-sm text-sm transition-colors">Industry Insights</button>
          <button class="border border-[#2D3139] text-[#9A9EA6] hover:text-white hover:border-white px-5 py-2 rounded-sm text-sm transition-colors">Technical Guides</button>
          <button class="border border-[#2D3139] text-[#9A9EA6] hover:text-white hover:border-white px-5 py-2 rounded-sm text-sm transition-colors">Product Updates</button>
          <button class="border border-[#2D3139] text-[#9A9EA6] hover:text-white hover:border-white px-5 py-2 rounded-sm text-sm transition-colors">Case Studies</button>
        </div>
      </div>
    </section>

    <!-- Featured Articles -->
    <section class="py-20 bg-[#121214]">
      <div class="max-w-4xl mx-auto px-4">
        <div class="text-center mb-16">
          <h2 class="text-3xl md:text-4xl font-extrabold text-white mb-4">Industry Insights</h2>
          <p class="text-[#9A9EA6] text-lg">Expert analysis and practical guidance for industrial lighting applications</p>
        </div>

        <div v-for="(article, i) in featuredArticles" :key="i" class="mb-10 last:mb-0">
          <div class="bg-[#1C1E22] border border-[#2D3139] rounded-sm overflow-hidden md:flex hover:border-[#FF6B00] transition-colors group">
            <div class="md:w-1/3 bg-gradient-to-br from-[#FF6B00]/20 to-[#121214] min-h-48 flex items-center justify-center">
              <svg class="w-12 h-12 text-[#2D3139]" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M4 4a2 2 0 012-2h4.586A2 2 0 0112 2.586L15.414 6A2 2 0 0116 7.414V16a2 2 0 01-2 2H6a2 2 0 01-2-2V4zm2 6a1 1 0 011-1h6a1 1 0 110 2H7a1 1 0 01-1-1zm1 3a1 1 0 100 2h6a1 1 0 100-2H7z" clip-rule="evenodd" /></svg>
            </div>
            <div class="md:w-2/3 p-8">
              <div class="flex items-center mb-3 gap-3">
                <span class="bg-[#121214] text-[#FF6B00] px-3 py-0.5 rounded-sm text-xs font-semibold border border-[#2D3139]">{{ article.category }}</span>
                <span class="text-xs text-[#9A9EA6]">{{ article.date }}</span>
              </div>
              <h3 class="text-xl font-bold text-white mb-3 group-hover:text-[#FF6B00] transition-colors">{{ article.title }}</h3>
              <p class="text-sm text-[#9A9EA6] mb-4">{{ article.excerpt }}</p>
              <div class="flex items-center justify-between">
                <span class="text-xs text-[#9A9EA6]">{{ article.readTime }}</span>
                <span class="text-sm font-semibold text-[#FF6B00] cursor-pointer hover:text-white transition-colors">Read Article →</span>
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
definePageMeta({ ...generateSeoMeta(seoConfigs.blog) })

const featuredArticles = [
  { category: 'Industry Insights', date: 'March 15, 2024', title: 'Why IP69K is the Only Rating That Matters for Canadian Winter Fleet Lights', excerpt: 'Discover why standard waterproof ratings fall short in harsh Canadian winter conditions and how IP69K certification ensures reliable performance through snow, ice, and salt spray.', readTime: '8 min read' },
  { category: 'Technical Guides', date: 'February 28, 2024', title: 'The Hidden Costs of Cheap LEDs: How Thermal Management Extends Lifespan', excerpt: 'Understanding the engineering behind thermal management in LED systems and why investing in proper cooling solutions pays off through dramatically extended product lifespan.', readTime: '10 min read' },
  { category: 'Business Strategy', date: 'January 22, 2024', title: 'How to Launch Your Own Lighting Brand via Our OEM Program', excerpt: 'A comprehensive guide for distributors and entrepreneurs looking to create their own branded lighting line, covering everything from product specification to market positioning.', readTime: '12 min read' },
]
</script>
