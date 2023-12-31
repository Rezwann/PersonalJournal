import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
    build: { manifest: true },
    base: process.env.mode === "production" ? "/static/" : "/",
    root: "./src",
    plugins: [vue()]
});