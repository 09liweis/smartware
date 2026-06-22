<template>
  <div>
    <PageHero
      title="Bridging the Gap Between Quality and Cost"
      :breadcrumbs="[
        { label: 'Home', path: '/' },
        { label: 'About SST-Smartware' },
      ]"
    />

    <section class="py-20 bg-[#121214]">
      <div class="max-w-4xl mx-auto px-4">
        <div class="bg-[#1C1E22] border border-[#2D3139] rounded-sm p-8 mb-12">
          <p class="text-lg text-[#9A9EA6] mb-6 leading-relaxed">
            "Headquartered in Toronto with our primary manufacturing facility in Shenzhen, <span class="font-semibold text-white">SST-Smartware Industrial Solutions</span> was founded to solve a major problem: the gap between high-cost local suppliers and inconsistent overseas technology providers."
          </p>
          <p class="text-base text-[#9A9EA6] leading-relaxed">
            We recognized that businesses needed reliable, high-quality industrial lighting solutions at competitive prices, but were stuck choosing between expensive domestic manufacturers with quality assurance and lower-cost international suppliers with questionable reliability and support.
          </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-12">
          <div>
            <div class="w-16 h-16 bg-[#FF6B00] rounded-full flex items-center justify-center mb-6">
              <svg class="w-8 h-8 text-white" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 2a8 8 0 100 16 8 8 0 000-16zm0 14a6 6 0 100-12 6 6 0 000 12z" clip-rule="evenodd" /></svg>
            </div>
            <h3 class="text-2xl font-bold text-white mb-4">The Toronto Advantage</h3>
            <p class="text-[#9A9EA6] mb-4">Our Toronto office handles all client relations, technical specifications, and warranty oversight. You get a partner who speaks your language, works in your time zone, and understands North American electrical and safety standards (UL/ETL/CSA).</p>
            <ul class="space-y-2 text-sm text-[#9A9EA6]">
              <li class="flex items-start gap-2"><svg class="w-4 h-4 mt-0.5 text-[#FF6B00] shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" /></svg> EST time zone support and local account management</li>
              <li class="flex items-start gap-2"><svg class="w-4 h-4 mt-0.5 text-[#FF6B00] shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" /></svg> North American electrical standards expertise</li>
              <li class="flex items-start gap-2"><svg class="w-4 h-4 mt-0.5 text-[#FF6B00] shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" /></svg> Warranty and technical support from North America</li>
            </ul>
          </div>

          <div>
            <div class="w-16 h-16 bg-[#FF6B00] rounded-full flex items-center justify-center mb-6">
              <svg class="w-8 h-8 text-white" fill="currentColor" viewBox="0 0 20 20"><path d="M10.394 2.08a1 1 0 00-.788 0l-7 3a1 1 0 000 1.84L5.25 8.051a.999.999 0 01.356-.257l4-1.714a1 1 0 11.788 1.838L7.667 9.088l1.94.831a1 1 0 00.787 0l7-3a1 1 0 000-1.838l-7-3z" /></svg>
            </div>
            <h3 class="text-2xl font-bold text-white mb-4">The Shenzhen Strength</h3>
            <p class="text-[#9A9EA6] mb-4">Our 50,000 sq. ft. facility in Shenzhen is equipped with automated SMT lines and rigorous testing labs for vibration, salt spray, and extreme temperatures. By owning the factory, we control the quality and the cost.</p>
            <ul class="space-y-2 text-sm text-[#9A9EA6]">
              <li class="flex items-start gap-2"><svg class="w-4 h-4 mt-0.5 text-[#FF6B00] shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" /></svg> 50,000 sq. ft. state-of-the-art facility</li>
              <li class="flex items-start gap-2"><svg class="w-4 h-4 mt-0.5 text-[#FF6B00] shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" /></svg> Automated SMT lines and precision assembly</li>
              <li class="flex items-start gap-2"><svg class="w-4 h-4 mt-0.5 text-[#FF6B00] shrink-0" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" /></svg> Vibration, salt spray, temperature extreme testing</li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <section class="py-20 bg-[#1C1E22] border-t border-[#2D3139]">
      <div class="max-w-4xl mx-auto px-4">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
          <div class="bg-[#121214] border border-[#2D3139] rounded-sm p-8">
            <h3 class="text-xl font-bold text-[#FF6B00] mb-4">Our Mission</h3>
            <p class="text-sm text-[#9A9EA6] leading-relaxed">To deliver superior industrial lighting solutions that combine exceptional quality with factory-direct pricing, supported by North American expertise and service.</p>
          </div>
          <div class="bg-[#121214] border border-[#2D3139] rounded-sm p-8">
            <h3 class="text-xl font-bold text-[#FF6B00] mb-4">Our Vision</h3>
            <p class="text-sm text-[#9A9EA6] leading-relaxed">To become the most trusted partner for industrial lighting in North America by redefining value through vertical integration and transparent operations.</p>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import { generateSeoMeta, seoConfigs } from '@/utils/seo'
definePageMeta({ ...generateSeoMeta(seoConfigs.about) })
</script>
