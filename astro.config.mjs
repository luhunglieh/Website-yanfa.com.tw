import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

// https://astro.build/config
export default defineConfig({
  site: 'https://luhunglieh.github.io',
  base: '/Website-yanfa.com.tw/',
  integrations: [tailwind()],
  devToolbar: {
    enabled: false
  },
  build: {
    format: 'directory'
  }
});
