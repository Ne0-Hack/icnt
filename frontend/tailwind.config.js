export default {
  purge: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  content: [
    './src/**/*.{vue,js,ts,jsx,tsx}'
  ],
  theme: {
    colors: {
      'light': '#FFFFFF',
      'dark': '#0F0F0F',
      'yellow': '#BCFF00',
      'gray': '#1c1c1c',
      'danger': '#FF0000'
    },
    fontFamily: {
      raleway: ['Raleway', 'sans-serif'],
      manrope: ['Manrope', 'sans-serif'],
      urbanist: ['Urbanist', 'sans-serif'],
      mulish: ['Mulish', 'sans-serif'],
    },
  },
  plugins: [],
}

