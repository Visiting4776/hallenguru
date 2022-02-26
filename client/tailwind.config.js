module.exports = {
  content: ['./public/index.html', './src/**/*.svelte'], // files monitored for tailwind classes
  theme: {
    extend: {
      fontFamily: {
        'serif': ['EB Garamond', 'ui-serif', 'Georgia', 'Cambria', 'Times New Roman', 'Times', 'serif']
      }
    },
  },
  plugins: [],
}
