/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',
  content: [
    '../../templates/**/*.html',
    '../../../templates/**/*.html',
    '../../**/*.py',
    './src/**/*.js',
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}