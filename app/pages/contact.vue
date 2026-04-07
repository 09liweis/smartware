<template>
  <div>
    <!-- Hero Section -->
    <section class="bg-gradient-to-r from-gray-900 to-blue-900 text-white py-20">
      <div class="container mx-auto px-4">
        <div class="max-w-4xl mx-auto text-center">
          <h1 class="text-5xl font-bold mb-6 leading-tight">
            Get a Factory-Direct Quote Today
          </h1>
          <p class="text-xl text-gray-300 mb-6 max-w-3xl mx-auto">
            Whether you need a container of light bars or a custom-branded tripod line, our team is ready to assist.
          </p>
        </div>
      </div>
    </section>

    <!-- Contact Information -->
    <section class="py-20">
      <div class="container mx-auto px-4">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-12">
          <!-- Contact Details -->
          <div>
            <h2 class="text-4xl font-bold mb-8">Contact Information</h2>
            
            <div class="space-y-8">
              <div class="bg-gray-50 p-6 rounded-xl">
                <h3 class="text-xl font-bold mb-3 text-blue-600">Sales & Strategy (North America)</h3>
                <div class="space-y-2 text-gray-600">
                  <div class="flex items-start">
                    <svg class="w-5 h-5 mr-3 mt-0.5 text-gray-400" fill="currentColor" viewBox="0 0 20 20">
                      <path fill-rule="evenodd" d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z" clip-rule="evenodd" />
                    </svg>
                    <span>Toronto, ON, Canada</span>
                  </div>
                  <div class="flex items-center">
                    <svg class="w-5 h-5 mr-3 text-gray-400" fill="currentColor" viewBox="0 0 20 20">
                      <path d="M2 3a1 1 0 011-1h2.153a1 1 0 01.986.836l.74 4.435a1 1 0 01-.54 1.06l-1.548.773a11.037 11.037 0 006.105 6.105l.774-1.548a1 1 0 011.059-.54l4.435.74a1 1 0 01.836.986V17a1 1 0 01-1 1h-2C7.82 18 2 12.18 2 5V3z" />
                    </svg>
                    <span>+1 (XXX) XXX-XXXX</span>
                  </div>
                  <div class="flex items-center">
                    <svg class="w-5 h-5 mr-3 text-gray-400" fill="currentColor" viewBox="0 0 20 20">
                      <path d="M2.003 5.884L10 9.882l7.997-3.998A2 2 0 0016 4H4a2 2 0 00-1.997 1.884z" />
                      <path d="M18 8.118l-8 4-8-4V14a2 2 0 002 2h12a2 2 0 002-2V8.118z" />
                    </svg>
                    <span>sales@powerhouse-lighting.com</span>
                  </div>
                </div>
              </div>
              
              <div class="bg-gray-50 p-6 rounded-xl">
                <h3 class="text-xl font-bold mb-3 text-blue-600">Manufacturing & Logistics</h3>
                <div class="space-y-2 text-gray-600">
                  <div class="flex items-start">
                    <svg class="w-5 h-5 mr-3 mt-0.5 text-gray-400" fill="currentColor" viewBox="0 0 20 20">
                      <path fill-rule="evenodd" d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z" clip-rule="evenodd" />
                    </svg>
                    <span>Bao'an District, Shenzhen, China</span>
                  </div>
                  <div class="flex items-center">
                    <svg class="w-5 h-5 mr-3 text-gray-400" fill="currentColor" viewBox="0 0 20 20">
                      <path d="M10 2a6 6 0 00-6 6v3.586l-.707.707A1 1 0 004 14h12a1 1 0 00.707-1.707L16 11.586V8a6 6 0 00-6-6zM10 18a3 3 0 01-3-3h6a3 3 0 01-3 3z" />
                    </svg>
                    <span>Factory operations 24/7</span>
                  </div>
                  <div class="flex items-center">
                    <svg class="w-5 h-5 mr-3 text-gray-400" fill="currentColor" viewBox="0 0 20 20">
                      <path fill-rule="evenodd" d="M3 17a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zm3.293-7.707a1 1 0 011.414 0L9 10.586V3a1 1 0 112 0v7.586l1.293-1.293a1 1 0 111.414 1.414l-3 3a1 1 0 01-1.414 0l-3-3a1 1 0 010-1.414z" clip-rule="evenodd" />
                    </svg>
                    <span>Direct factory-to-door shipping</span>
                  </div>
                </div>
              </div>
              
              <div class="bg-gray-50 p-6 rounded-xl">
                <h3 class="text-xl font-bold mb-3 text-blue-600">Business Hours</h3>
                <div class="space-y-2 text-gray-600">
                  <div class="flex justify-between">
                    <span>Monday - Friday</span>
                    <span class="font-medium">9:00 AM - 6:00 PM EST</span>
                  </div>
                  <div class="flex justify-between">
                    <span>Saturday</span>
                    <span class="font-medium">10:00 AM - 2:00 PM EST</span>
                  </div>
                  <div class="flex justify-between">
                    <span>Sunday</span>
                    <span class="font-medium">Closed</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
          
          <!-- Inquiry Form -->
          <div>
            <h2 class="text-4xl font-bold mb-8">Start Your Project</h2>
            
            <div class="bg-white rounded-xl shadow-lg p-8">
              <form @submit.prevent class="space-y-6">
                <div>
                  <label class="block text-gray-700 mb-2">I am interested in:</label>
                  <div class="space-y-2">
                    <div class="flex items-center">
                      <input type="checkbox" id="wholesale" class="w-4 h-4 text-blue-600 rounded" />
                      <label for="wholesale" class="ml-2 text-gray-700">Wholesale</label>
                    </div>
                    <div class="flex items-center">
                      <input type="checkbox" id="oem" class="w-4 h-4 text-blue-600 rounded" />
                      <label for="oem" class="ml-2 text-gray-700">OEM/Private Label</label>
                    </div>
                    <div class="flex items-center">
                      <input type="checkbox" id="project" class="w-4 h-4 text-blue-600 rounded" />
                      <label for="project" class="ml-2 text-gray-700">Project Supply</label>
                    </div>
                  </div>
                </div>
                
                <div>
                  <label class="block text-gray-700 mb-2">Estimated Quantity:</label>
                  <div class="grid grid-cols-1 sm:grid-cols-3 gap-2">
                    <button type="button" class="border border-gray-300 text-gray-700 py-2 rounded hover:bg-gray-50 transition-colors">
                      50-100 units
                    </button>
                    <button type="button" class="border border-gray-300 text-gray-700 py-2 rounded hover:bg-gray-50 transition-colors">
                      100-500 units
                    </button>
                    <button type="button" class="border border-gray-300 text-gray-700 py-2 rounded hover:bg-gray-50 transition-colors">
                      500+ units
                    </button>
                  </div>
                </div>
                
                <div>
                  <label class="block text-gray-700 mb-2" for="name">Full Name *</label>
                  <input type="text" id="name" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500" required />
                </div>
                
                <div>
                  <label class="block text-gray-700 mb-2" for="company">Company</label>
                  <input type="text" id="company" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500" />
                </div>
                
                <div>
                  <label class="block text-gray-700 mb-2" for="email">Email *</label>
                  <input type="email" id="email" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500" required />
                </div>
                
                <div>
                  <label class="block text-gray-700 mb-2" for="phone">Phone</label>
                  <input type="tel" id="phone" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500" />
                </div>
                
                <div>
                  <label class="block text-gray-700 mb-2" for="message">Message</label>
                  <textarea id="message" rows="4" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500" placeholder="Tell us about your technical requirements..."></textarea>
                </div>
                
                <button type="submit" class="w-full bg-blue-600 hover:bg-blue-700 text-white py-3 rounded-lg font-semibold transition-colors">
                  Submit Inquiry
                </button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Map & Location -->
    <section class="py-20 bg-gray-50">
      <div class="container mx-auto px-4">
        <div class="text-center mb-12">
          <h2 class="text-4xl font-bold mb-6">Our Global Locations</h2>
          <p class="text-gray-600 max-w-2xl mx-auto text-lg">
            Strategically positioned across continents to serve you better
          </p>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-4xl mx-auto">
          <div class="bg-white p-6 rounded-xl shadow-lg">
            <div class="flex items-center mb-4">
              <div class="w-10 h-10 bg-blue-600 text-white rounded-full flex items-center justify-center mr-4">
                <span>CA</span>
              </div>
              <h3 class="text-xl font-bold">Toronto Office</h3>
            </div>
            <p class="text-gray-600 mb-4">
              Strategic headquarters for North American operations, client relations, and technical support.
            </p>
            <p class="text-gray-500 text-sm">
              <strong>Focus:</strong> Sales, Strategy, Customer Support, Technical Consulting
            </p>
          </div>
          
          <div class="bg-white p-6 rounded-xl shadow-lg">
            <div class="flex items-center mb-4">
              <div class="w-10 h-10 bg-blue-600 text-white rounded-full flex items-center justify-center mr-4">
                <span>CN</span>
              </div>
              <h3 class="text-xl font-bold">Shenzhen Factory</h3>
            </div>
            <p class="text-gray-600 mb-4">
              Primary manufacturing and R&D facility with automated production lines and comprehensive testing.
            </p>
            <p class="text-gray-500 text-sm">
              <strong>Focus:</strong> Manufacturing, R&D, Quality Control, Production
            </p>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import { generateSeoMeta, seoConfigs } from '@/utils/seo'

// Define page meta for SEO
definePageMeta({
  // SEO configuration for the contact page
  ...generateSeoMeta(seoConfigs.contact),
})
</script>