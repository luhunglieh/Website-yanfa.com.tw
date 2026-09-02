import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

// https://astro.build/config
export default defineConfig({
  site: 'https://www.yanfa.com.tw',
  base: '/',
  integrations: [tailwind()],
  devToolbar: {
    enabled: false
  },
  build: {
    format: 'directory'
  }
});
