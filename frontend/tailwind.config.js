/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        krushi: {
          green: '#1b5e20',
          'green-light': '#4caf50',
          yellow: '#ffc107',
          'gray-bg': '#f5f5f5',
          dark: '#212121',
        },
      },
      fontFamily: {
        sans: ['Inter', 'Poppins', 'Noto Sans Kannada', 'sans-serif'],
      },
    },
  },
  plugins: [],
}
