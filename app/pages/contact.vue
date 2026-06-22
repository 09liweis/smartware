<template>
  <div>
    <PageHero
      title="Get a Factory-Direct Quote Today"
      description="Whether you need a container of light bars or a custom-branded tripod line, our team is ready to assist."
      :breadcrumbs="[
        { label: 'Home', path: '/' },
        { label: 'Request RFQ / Contact Us' },
      ]"
    />

    <section class="py-20 bg-[#121214]">
      <div class="max-w-7xl mx-auto px-4">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-12">
          <div>
            <h2 class="text-3xl font-extrabold text-white mb-8">Contact Information</h2>
            <div class="space-y-6">
              <div class="bg-[#1C1E22] border border-[#2D3139] rounded-sm p-6">
                <h3 class="text-lg font-bold text-[#FF6B00] mb-3">Sales & Strategy (North America)</h3>
                <div class="space-y-2 text-sm text-[#9A9EA6]">
                  <div class="flex items-start gap-3">
                    <svg class="w-4 h-4 mt-0.5 shrink-0 text-[#9A9EA6]" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z" clip-rule="evenodd" /></svg>
                    <span>Greater Toronto Area, ON, Canada</span>
                  </div>
                  <div class="flex items-center gap-3">
                    <svg class="w-4 h-4 shrink-0 text-[#9A9EA6]" fill="currentColor" viewBox="0 0 20 20"><path d="M2 3a1 1 0 011-1h2.153a1 1 0 01.986.836l.74 4.435a1 1 0 01-.54 1.06l-1.548.773a11.037 11.037 0 006.105 6.105l.774-1.548a1 1 0 011.059-.54l4.435.74a1 1 0 01.836.986V17a1 1 0 01-1 1h-2C7.82 18 2 12.18 2 5V3z" /></svg>
                    <span>+1 (416) XXX-XXXX</span>
                  </div>
                  <div class="flex items-center gap-3">
                    <svg class="w-4 h-4 shrink-0 text-[#9A9EA6]" fill="currentColor" viewBox="0 0 20 20"><path d="M2.003 5.884L10 9.882l7.997-3.998A2 2 0 0016 4H4a2 2 0 00-1.997 1.884z" /><path d="M18 8.118l-8 4-8-4V14a2 2 0 002 2h12a2 2 0 002-2V8.118z" /></svg>
                    <span>info@sst-smartware.com</span>
                  </div>
                </div>
              </div>

              <div class="bg-[#1C1E22] border border-[#2D3139] rounded-sm p-6">
                <h3 class="text-lg font-bold text-[#FF6B00] mb-3">Manufacturing & Logistics</h3>
                <div class="space-y-2 text-sm text-[#9A9EA6]">
                  <div class="flex items-start gap-3">
                    <svg class="w-4 h-4 mt-0.5 shrink-0 text-[#9A9EA6]" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z" clip-rule="evenodd" /></svg>
                    <span>Bao'an District, Shenzhen, China</span>
                  </div>
                  <div class="flex items-center gap-3">
                    <svg class="w-4 h-4 shrink-0 text-[#9A9EA6]" fill="currentColor" viewBox="0 0 20 20"><path d="M10 2a6 6 0 00-6 6v3.586l-.707.707A1 1 0 004 14h12a1 1 0 00.707-1.707L16 11.586V8a6 6 0 00-6-6zM10 18a3 3 0 01-3-3h6a3 3 0 01-3 3z" /></svg>
                    <span>Factory operations 24/7</span>
                  </div>
                </div>
              </div>

              <div class="bg-[#1C1E22] border border-[#2D3139] rounded-sm p-6">
                <h3 class="text-lg font-bold text-[#FF6B00] mb-3">Business Hours</h3>
                <div class="space-y-2 text-sm text-[#9A9EA6]">
                  <div class="flex justify-between"><span>Monday - Friday</span><span class="text-white font-medium">9:00 AM - 6:00 PM EST</span></div>
                  <div class="flex justify-between"><span>Saturday</span><span class="text-white font-medium">10:00 AM - 2:00 PM EST</span></div>
                  <div class="flex justify-between"><span>Sunday</span><span class="text-white font-medium">Closed</span></div>
                </div>
              </div>
            </div>
          </div>

          <div>
            <h2 class="text-3xl font-extrabold text-white mb-8">Start Your Project</h2>
            <div class="bg-[#1C1E22] border border-[#2D3139] rounded-sm p-8">
              <form @submit.prevent class="space-y-6">
                <div>
                  <label class="block text-sm font-medium text-white mb-2">I am interested in:</label>
                  <div class="space-y-2">
                    <label v-for="opt in inquiryOptions" :key="opt" class="flex items-center gap-2 cursor-pointer text-sm text-[#9A9EA6]">
                      <input type="checkbox" class="w-4 h-4 rounded-sm border-[#2D3139] bg-[#121214] text-[#FF6B00] focus:ring-[#FF6B00]" /> {{ opt }}
                    </label>
                  </div>
                </div>

                <div>
                  <label class="block text-sm font-medium text-white mb-2">Estimated Quantity:</label>
                  <div class="grid grid-cols-3 gap-2">
                    <button type="button" class="border border-[#2D3139] text-[#9A9EA6] py-2 rounded-sm text-sm hover:border-white hover:text-white transition-colors">50-100 units</button>
                    <button type="button" class="border border-[#2D3139] text-[#9A9EA6] py-2 rounded-sm text-sm hover:border-white hover:text-white transition-colors">100-500 units</button>
                    <button type="button" class="border border-[#2D3139] text-[#9A9EA6] py-2 rounded-sm text-sm hover:border-white hover:text-white transition-colors">500+ units</button>
                  </div>
                </div>

                <div>
                  <label class="block text-sm font-medium text-white mb-1">Full Name *</label>
                  <input type="text" class="w-full bg-[#121214] border border-[#2D3139] rounded-sm px-4 py-2.5 text-white text-sm focus:outline-none focus:border-[#FF6B00] transition-colors" required />
                </div>
                <div>
                  <label class="block text-sm font-medium text-white mb-1">Company</label>
                  <input type="text" class="w-full bg-[#121214] border border-[#2D3139] rounded-sm px-4 py-2.5 text-white text-sm focus:outline-none focus:border-[#FF6B00] transition-colors" />
                </div>
                <div>
                  <label class="block text-sm font-medium text-white mb-1">Email *</label>
                  <input type="email" class="w-full bg-[#121214] border border-[#2D3139] rounded-sm px-4 py-2.5 text-white text-sm focus:outline-none focus:border-[#FF6B00] transition-colors" required />
                </div>
                <div>
                  <label class="block text-sm font-medium text-white mb-1">Phone</label>
                  <input type="tel" class="w-full bg-[#121214] border border-[#2D3139] rounded-sm px-4 py-2.5 text-white text-sm focus:outline-none focus:border-[#FF6B00] transition-colors" />
                </div>
                <div>
                  <label class="block text-sm font-medium text-white mb-1">Message</label>
                  <textarea rows="4" class="w-full bg-[#121214] border border-[#2D3139] rounded-sm px-4 py-2.5 text-white text-sm focus:outline-none focus:border-[#FF6B00] transition-colors resize-none" placeholder="Tell us about your technical requirements..."></textarea>
                </div>
                <button type="submit" class="w-full bg-[#FF6B00] hover:bg-[#E65100] text-white py-3 rounded-sm font-bold transition-colors tracking-wide shadow-structural">
                  Submit RFQ Inquiry
                </button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import { generateSeoMeta, seoConfigs } from '@/utils/seo'
definePageMeta({ ...generateSeoMeta(seoConfigs.contact) })

const inquiryOptions = ['Wholesale', 'OEM/Private Label', 'Project Supply']
</script>
