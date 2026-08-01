export default defineAppConfig({
  ui: {
    colors: {
      // Semantic aliases → Tailwind palettes (Nuxt UI design system).
      // Orange brand accents; zinc for surfaces (slate reads too blue).
      primary: 'orange',
      neutral: 'zinc'
    },
    footer: {
      slots: {
        root: 'border-t border-default',
        left: 'text-sm text-muted'
      }
    }
  },
  seo: {
    siteName: 'OutlabsAuth Docs'
  },
  header: {
    title: '',
    to: '/',
    logo: {
      alt: 'OutlabsAuth',
      light: '/outlabsAuthLogo.svg',
      dark: '/outlabsAuthLogo.svg'
    },
    search: true,
    colorMode: true,
    links: [{
      'icon': 'i-simple-icons-github',
      'to': 'https://github.com/outlabsio/outlabsAuth',
      'target': '_blank',
      'aria-label': 'OutlabsAuth on GitHub'
    }, {
      'icon': 'i-simple-icons-pypi',
      'to': 'https://pypi.org/project/outlabs-auth/',
      'target': '_blank',
      'aria-label': 'outlabs-auth on PyPI'
    }]
  },
  footer: {
    credits: `OutlabsAuth Docs • © ${new Date().getFullYear()} OutLabs`,
    colorMode: false,
    links: [{
      'icon': 'i-simple-icons-github',
      'to': 'https://github.com/outlabsio/outlabsAuth',
      'target': '_blank',
      'aria-label': 'GitHub'
    }, {
      'icon': 'i-simple-icons-pypi',
      'to': 'https://pypi.org/project/outlabs-auth/',
      'target': '_blank',
      'aria-label': 'PyPI'
    }]
  },
  toc: {
    title: 'On this page',
    bottom: {
      title: 'Resources',
      edit: 'https://github.com/outlabsio/outlabsAuth/edit/main/docs-library',
      links: [{
        icon: 'i-lucide-package',
        label: 'PyPI package',
        to: 'https://pypi.org/project/outlabs-auth/',
        target: '_blank'
      }, {
        icon: 'i-lucide-layout-dashboard',
        label: 'OutlabsAuth UI',
        to: 'https://github.com/outlabsio/OutlabsAuthUI',
        target: '_blank'
      }]
    }
  }
})
