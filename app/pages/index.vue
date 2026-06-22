<template>
  <div>
    <!-- Hero Section -->
    <section class="bg-[#121214] border-b border-[#2D3139] py-24 md:py-32">
      <div class="max-w-7xl mx-auto px-4">
        <div class="max-w-4xl mx-auto text-center">
          <h1 class="text-4xl md:text-6xl font-extrabold leading-tight mb-6 text-white">
            Commercial-Grade LED Hardware Systems.<br />
            <span class="text-[#FF6B00]">Engineered in Shenzhen. Managed Locally.</span>
          </h1>
          <p class="text-lg md:text-xl text-[#9A9EA6] mb-10 max-w-3xl mx-auto leading-relaxed">
            High-lumen efficiency, robust thermal management, and extreme weatherproofing built direct from our proprietary assembly lines and backed by dedicated North American account support.
          </p>
          <div class="flex flex-col sm:flex-row gap-4 justify-center">
            <NuxtLink to="/products" class="bg-[#FF6B00] hover:bg-[#E65100] text-white px-8 py-4 rounded-sm text-base font-bold transition-colors shadow-structural tracking-wide">
              Explore Technical Catalog
            </NuxtLink>
            <NuxtLink to="/contact" class="border border-[#2D3139] bg-[#1C1E22] hover:bg-[#2D3139] text-white px-8 py-4 rounded-sm text-base font-bold transition-colors tracking-wide">
              Request Bulk RFQ
            </NuxtLink>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 1: Product Spectrum Summary -->
    <section class="py-20 bg-[#121214]">
      <div class="max-w-7xl mx-auto px-4">
        <div class="text-center mb-16">
          <h2 class="text-3xl md:text-4xl font-extrabold text-white mb-4">Product Spectrum Summary</h2>
          <p class="text-[#9A9EA6] text-lg max-w-2xl mx-auto">An instant visual matrix of the hardware we supply for commercial procurement</p>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
          <!-- LED Rechargeable Work Lights -->
          <NuxtLink to="/products/rechargeable-work-lights" class="bg-[#1C1E22] border border-[#2D3139] rounded-sm p-6 hover:border-[#FF6B00] transition-all group">
            <div class="w-20 h-20 bg-[#121214] border border-[#2D3139] rounded-sm flex items-center justify-center mb-5 mx-auto sm:mx-0">
              <svg class="w-10 h-10 text-[#FF6B00] opacity-80" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
              </svg>
            </div>
            <h3 class="text-base font-bold text-white mb-1 group-hover:text-[#FF6B00] transition-colors">LED Rechargeable Work Lights</h3>
            <p class="text-sm text-[#9A9EA6]">Cordless High-Capacity Task Lighting</p>
          </NuxtLink>

          <!-- LED Work Lights -->
          <NuxtLink to="/products/led-work-lights" class="bg-[#1C1E22] border border-[#2D3139] rounded-sm p-6 hover:border-[#FF6B00] transition-all group">
            <div class="w-20 h-20 bg-[#121214] border border-[#2D3139] rounded-sm flex items-center justify-center mb-5 mx-auto sm:mx-0">
              <svg class="w-10 h-10 text-[#FF6B00] opacity-80" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M5 3l14 9-14 9V3z" />
              </svg>
            </div>
            <h3 class="text-base font-bold text-white mb-1 group-hover:text-[#FF6B00] transition-colors">LED Work Lights</h3>
            <p class="text-sm text-[#9A9EA6]">Heavy-Duty Corded Field Arrays</p>
          </NuxtLink>

          <!-- LED Light Bars -->
          <NuxtLink to="/products/led-light-bars" class="bg-[#1C1E22] border border-[#2D3139] rounded-sm p-6 hover:border-[#FF6B00] transition-all group">
            <div class="w-20 h-20 bg-[#121214] border border-[#2D3139] rounded-sm flex items-center justify-center mb-5 mx-auto sm:mx-0">
              <svg class="w-10 h-10 text-[#FF6B00] opacity-80" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4" />
              </svg>
            </div>
            <h3 class="text-base font-bold text-white mb-1 group-hover:text-[#FF6B00] transition-colors">LED Light Bars</h3>
            <p class="text-sm text-[#9A9EA6]">Commercial Vehicle Fleet Illumination</p>
          </NuxtLink>

          <!-- LED Tripods -->
          <NuxtLink to="/products/led-tripods" class="bg-[#1C1E22] border border-[#2D3139] rounded-sm p-6 hover:border-[#FF6B00] transition-all group">
            <div class="w-20 h-20 bg-[#121214] border border-[#2D3139] rounded-sm flex items-center justify-center mb-5 mx-auto sm:mx-0">
              <svg class="w-10 h-10 text-[#FF6B00] opacity-80" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M13 10V3L4 14h7v7l9-11h-7z" />
              </svg>
            </div>
            <h3 class="text-base font-bold text-white mb-1 group-hover:text-[#FF6B00] transition-colors">LED Tripods</h3>
            <p class="text-sm text-[#9A9EA6]">High-Output Telescopic Site Systems</p>
          </NuxtLink>
        </div>
      </div>
    </section>

    <!-- Section 2: Who We Are (The Local North American Edge) -->
    <section class="py-20 bg-[#1C1E22] border-y border-[#2D3139]">
      <div class="max-w-7xl mx-auto px-4">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
          <!-- Left: Map Graphic -->
          <div class="flex items-center justify-center">
            <div class="w-full max-w-md bg-[#121214] border border-[#2D3139] rounded-sm p-8 relative overflow-hidden">
              <!-- Simplified map connector line -->
              <div class="relative h-64 flex items-center justify-center">
                <!-- Shenzhen point -->
                <div class="absolute left-8 top-1/3 text-center">
                  <div class="w-4 h-4 bg-[#FF6B00] rounded-full mx-auto mb-2 shadow-[0_0_12px_rgba(255,107,0,0.5)]"></div>
                  <div class="text-xs font-bold text-white">SHENZHEN</div>
                  <div class="text-[10px] text-[#9A9EA6]">Manufacturing Base</div>
                </div>

                <!-- Connector line -->
                <svg class="absolute inset-0 w-full h-full" viewBox="0 0 400 256" fill="none">
                  <line x1="80" y1="85" x2="310" y2="140" stroke="#FF6B00" stroke-width="2" stroke-dasharray="6 4" opacity="0.5" />
                  <line x1="80" y1="85" x2="310" y2="140" stroke="#FF6B00" stroke-width="1" opacity="0.3">
                    <animate attributeName="stroke-dashoffset" from="10" to="0" dur="2s" repeatCount="indefinite" />
                  </line>
                </svg>

                <!-- Toronto point -->
                <div class="absolute right-8 bottom-1/3 text-center">
                  <div class="w-4 h-4 bg-emerald-400 rounded-full mx-auto mb-2 shadow-[0_0_12px_rgba(52,211,153,0.5)]"></div>
                  <div class="text-xs font-bold text-white">GREATER TORONTO</div>
                  <div class="text-[10px] text-[#9A9EA6]">Logistics & Operations Hub</div>
                </div>
              </div>

              <!-- Animated dotted path -->
              <div class="absolute inset-0 opacity-10">
                <div class="w-full h-full bg-[radial-gradient(circle_at_20%_30%,#FF6B00_1px,transparent_1px),radial-gradient(circle_at_80%_60%,#34D399_1px,transparent_1px)] bg-[length:40px_40px]"></div>
              </div>
            </div>
          </div>

          <!-- Right: Copy -->
          <div>
            <h2 class="text-3xl md:text-4xl font-extrabold text-white mb-6 leading-tight">
              Your Factory-Direct Supply Chain.<br />
              <span class="text-[#FF6B00]">Managed Locally in North America.</span>
            </h2>
            <p class="text-[#9A9EA6] text-base leading-relaxed mb-4">
              SST-Smartware functions as the direct North American sales, logistics, and engineering management arm for our proprietary Shenzhen assembly plants. We eliminate the friction of international sourcing.
            </p>
            <p class="text-[#9A9EA6] text-base leading-relaxed mb-6">
              When you partner with us, you work directly with a local, dedicated account team responsible for custom OEM blueprinting, strict local quality-assurance audits, custom broker clearance, cross-docking operations, and rapid warranty replacement fulfillment directly out of our Toronto regional hubs.
            </p>
            <ul class="space-y-3">
              <li v-for="benefit in localBenefits" :key="benefit" class="flex items-start gap-3 text-sm text-[#9A9EA6]">
                <svg class="w-5 h-5 mt-0.5 text-[#FF6B00] shrink-0" fill="currentColor" viewBox="0 0 20 20">
                  <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
                </svg>
                <span>{{ benefit }}</span>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 3: Inside the Shenzhen Lines (Factory Video) -->
    <section class="relative py-32 bg-[#121214] overflow-hidden">
      <!-- Background gradient overlay -->
      <div class="absolute inset-0 bg-gradient-to-b from-[#121214] via-transparent to-[#121214] z-10"></div>
      <div class="absolute inset-0 bg-[#121214] opacity-90 z-10"></div>

      <!-- Pattern background -->
      <div class="absolute inset-0 opacity-5">
        <div class="w-full h-full" style="background-image: repeating-linear-gradient(45deg, #FF6B00 0, #FF6B00 1px, transparent 0, transparent 20px), repeating-linear-gradient(-45deg, #FF6B00 0, #FF6B00 1px, transparent 0, transparent 20px);"></div>
      </div>

      <div class="relative z-20 max-w-4xl mx-auto px-4 text-center">
        <h2 class="text-3xl md:text-4xl font-extrabold text-white mb-4">
          Engineered for Rigorous Field Performance
        </h2>
        <p class="text-lg text-[#9A9EA6] mb-8 max-w-2xl mx-auto leading-relaxed">
          Every unit undergoes an exhaustive 48-hour automated burn-in and IP67 water-ingress check inside our physical Shenzhen lines before being packed for Canadian transport.
        </p>

        <!-- Play Button -->
        <button
          @click="showVideo = true"
          class="inline-flex items-center gap-3 bg-[#FF6B00] hover:bg-[#E65100] text-white px-8 py-4 rounded-sm text-base font-bold transition-colors shadow-structural tracking-wide"
        >
          <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20">
            <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z" clip-rule="evenodd" />
          </svg>
          Watch Manufacturing Tour
        </button>
      </div>

      <!-- Video Modal Overlay -->
      <div v-if="showVideo" class="fixed inset-0 z-50 flex items-center justify-center bg-black/90 p-4" @click.self="showVideo = false">
        <div class="relative w-full max-w-4xl bg-[#121214] border border-[#2D3139] rounded-sm shadow-2xl">
          <button @click="showVideo = false" class="absolute -top-10 right-0 text-white hover:text-[#FF6B00] transition-colors">
            <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
          <div class="aspect-video bg-[#1C1E22] flex items-center justify-center text-[#9A9EA6]">
            <div class="text-center">
              <svg class="w-20 h-20 mx-auto mb-4 text-[#FF6B00] opacity-50" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z" clip-rule="evenodd" />
              </svg>
              <p class="text-lg font-semibold text-white">Manufacturing Tour Video</p>
              <p class="text-sm text-[#9A9EA6] mt-1">Full HD facility walkthrough</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 4: Market Segments & Industry Solutions -->
    <section class="py-20 bg-[#121214]">
      <div class="max-w-7xl mx-auto px-4">
        <div class="text-center mb-16">
          <h2 class="text-3xl md:text-4xl font-extrabold text-white mb-4">Market Segments & Industry Solutions</h2>
          <p class="text-[#9A9EA6] text-lg max-w-2xl mx-auto">Mapping our hardware to real-world commercial applications</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <NuxtLink
            v-for="industry in industries"
            :key="industry.slug"
            :to="`/industries/${industry.slug}`"
            class="bg-[#1C1E22] border border-[#2D3139] rounded-sm p-8 hover:border-[#FF6B00] transition-all group flex flex-col justify-between min-h-[200px]"
          >
            <div>
              <h3 class="text-xl font-bold text-white mb-3 group-hover:text-[#FF6B00] transition-colors">{{ industry.title }}</h3>
              <p class="text-sm text-[#9A9EA6] leading-relaxed">{{ industry.description }}</p>
            </div>
            <div class="mt-6 flex items-center text-sm font-semibold text-[#FF6B00] group-hover:gap-2 transition-all">
              Explore Solutions
              <svg class="w-4 h-4 ml-1 opacity-0 group-hover:opacity-100 transition-all" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
              </svg>
            </div>
          </NuxtLink>
        </div>
      </div>
    </section>

    <!-- Section 5: High-Intent B2B CTA -->
    <section class="py-20 bg-[#1C1E22] border-y border-[#2D3139]">
      <div class="max-w-3xl mx-auto px-4 text-center">
        <h2 class="text-3xl md:text-4xl font-extrabold text-white mb-4">Have a Specific Question?</h2>
        <p class="text-lg text-[#9A9EA6] mb-4">Speak with a Supply Chain Expert</p>
        <p class="text-sm text-[#9A9EA6] mb-8 max-w-xl mx-auto">
          Our Toronto-based account team is ready to discuss your commercial volume requirements, custom OEM specifications, and delivery timelines.
        </p>
        <NuxtLink to="/contact" class="inline-block bg-[#FF6B00] hover:bg-[#E65100] text-white px-10 py-4 rounded-sm text-base font-bold transition-colors shadow-structural tracking-wide">
          Contact Us
        </NuxtLink>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { generateSeoMeta, seoConfigs } from '@/utils/seo'

definePageMeta({
  ...generateSeoMeta(seoConfigs.home),
})

const showVideo = ref(false)

const localBenefits = [
  'EST time zone account management and rapid response',
  'Custom OEM blueprinting and engineering review',
  'Local quality-assurance audits and compliance verification',
  'Custom broker clearance and cross-docking operations',
  'Rapid warranty replacement from Toronto regional hubs',
]

const industries = [
  {
    slug: 'commercial-fleet',
    title: 'Commercial Fleet & Utility Vehicles',
    description: 'Heavy vibration protection, sub-zero operating environments, and low-voltage DC auto-switching layouts for service trucks, tow fleets, and utility vehicles.',
  },
  {
    slug: 'construction-infrastructure',
    title: 'Construction & Infrastructure Jobsites',
    description: 'High-impact shell shielding, concrete dust ingress blocking, and rapid field deployment for harsh outdoor environments and long night shifts.',
  },
  {
    slug: 'industrial-warehousing',
    title: 'Industrial Warehousing & Supply Chain Operations',
    description: 'Energy-efficient, high-lumen structural illumination and reliable manual task tools for manufacturing floors, loading docks, and facility maintenance.',
  },
  {
    slug: 'oem-manufacturing',
    title: 'OEM & Private Label Manufacturing Partners',
    description: 'Direct pipeline to our Shenzhen engineering and manufacturing facilities. Custom casing branding, proprietary volt/amp adjustments, and custom mounts.',
  },
]
</script>
