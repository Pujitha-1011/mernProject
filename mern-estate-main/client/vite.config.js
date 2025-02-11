import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react-swc';

export default defineConfig({
  server: {
    proxy: {
      '/api': {
        target: 'http://localhost:3000',
        secure: false,
        changeOrigin: true, // Ensure proper origin handling
      },
    },
    watch: {
      usePolling: true, // Reduce sensitivity for HMR
      interval: 100,
    },
    hmr: true, // Disable this temporarily for debugging if needed
  },
  plugins: [react()],
});
