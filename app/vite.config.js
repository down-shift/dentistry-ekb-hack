import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

const path = require("path");

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  outputDir: 'dist',
  assetsDir: 'static',
  build: {
    sourcemap: true,
  },
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
  server: {
    port: 80,
    host: "127.0.0.1",
    proxy: {
      '^/api': {
        target: 'http://localhost:8000',
        pathRewrite: { '^/api': '/api' },
        logLevel: 'debug'
      },
      '^/media': {
        target: 'http://localhost:8000',
        pathRewrite: { '^/media': '/media' },
        logLevel: 'debug'
      },
      '^/static': {
        target: 'http://localhost:8000',
        pathRewrite: { '^/static': '/static' },
        logLevel: 'debug'
      },
    },
    strictPort: true,
  },
  define: {
    __APP_VERSION__: JSON.stringify(process.env.npm_package_version),
  },
})
