import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import path from 'path';
// https://vitejs.dev/config/
export default defineConfig({
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
      '@templates': path.resolve(__dirname, './src/templates'),
      '@components': path.resolve(__dirname, './src/components'),
      '@images': path.resolve(__dirname, './src/assets/images'),
    },
  },
  plugins: [vue()],
})
