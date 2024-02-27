/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.{html,js}',
    './citywatch/templates/**/*.{html,js}',
  ],
  theme: {
    extend: {
      colors: {
        primary: '#ed9320',
        secondary: '#f6f5f3',
      },
      fontFamily: {
        'sans': ['"Poppins"', 'sans-serif'],
      },
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
  ],
}

