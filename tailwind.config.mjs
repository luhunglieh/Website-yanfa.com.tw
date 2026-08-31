/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        brand: {
          blue: '#0284c7',
          dark: '#0f172a',
          navy: '#1e293b',
          accent: '#0369a1',
          primary: '#1d4ed8'
        }
      },
      fontFamily: {
        sans: ['Noto Sans TC', 'Roboto', 'sans-serif']
      }
    },
  },
  plugins: [],
};
