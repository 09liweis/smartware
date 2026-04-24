<template>
  <section class="py-20 bg-gray-50">
    <div class="container mx-auto px-4">
      <div class="text-center mb-16">
        <h2 class="text-4xl font-bold mb-6">The Global Powerhouse</h2>
        <p class="text-gray-600 max-w-2xl mx-auto text-lg">
          Combining cutting-edge manufacturing with local expertise to deliver unparalleled value
        </p>
      </div>
      
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div
          v-for="item in items"
          :key="item.title"
          class="bg-white p-8 rounded-xl shadow-lg"
        >
          <div class="w-16 h-16 bg-blue-100 rounded-full flex items-center justify-center mb-6">
            <div v-html="item.icon" class="w-8 h-8 text-blue-600"></div>
          </div>
          <h3 class="text-2xl font-bold mb-4">{{ item.title }}</h3>
          <p class="text-gray-600">
            {{ item.description }}
          </p>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
interface WhyUsItem {
  title: string
  description: string
  icon: string
}

const items: WhyUsItem[] = [
  {
    title: 'Shenzhen Manufacturing',
    description: '24/7 production capacity with cutting-edge R&D and rigorous QC testing. Our state-of-the-art facility ensures consistent quality and rapid turnaround.',
    icon: '<svg fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 2a8 8 0 100 16 8 8 0 000-16zm0 14a6 6 0 100-12 6 6 0 000 12z" clip-rule="evenodd" /></svg>',
  },
  {
    title: 'Toronto Strategic Office',
    description: 'Local account management, EST time-zone support, and technical consulting. Our North American team ensures seamless communication and understanding of local standards.',
    icon: '<svg fill="currentColor" viewBox="0 0 20 20"><path d="M2.003 5.884L10 9.882l7.997-3.998A2 2 0 0016 4H4a2 2 0 00-1.997 1.884z" /><path d="M18 8.118l-8 4-8-4V14a2 2 0 002 2h12a2 2 0 002-2V8.118z" /></svg>',
  },
  {
    title: 'Global Logistics',
    description: 'Streamlined factory-to-door shipping with full transparency on lead times. We handle all logistics from production to your warehouse with precision tracking.',
    icon: '<svg fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM4.332 8.027a6.012 6.012 0 011.912-2.706C6.512 5.73 6.974 6 7.5 6A1.5 1.5 0 019 7.5V8a2 2 0 004 0 2 2 0 011.523-1.943A5.977 5.977 0 0116 10c0 .34-.028.675-.083 1H15a2 2 0 00-2 2v2.197A5.973 5.973 0 0110 16v-2a2 2 0 00-2-2 2 2 0 01-2-2 2 2 0 00-1.668-1.973z" clip-rule="evenodd" /></svg>',
  },
]
</script>
