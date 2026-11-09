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
    credits: `© ${new Date().getFullYear()} OutLabs LLC`,
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
  relatedDocs: [
    { label: 'Outlabs Auth', to: 'https://auth.outlabs.io/' },
    { label: 'Auth UI', to: 'https://auth.outlabs.io/integrations/outlabsauth-ui/' },
    { label: 'TaskQ', to: 'https://taskq.outlabs.io/' }
  ],
  toc: {
    title: 'On this page',
    bottom: {
      title: 'Resources',
      edit: 'https://github.com/outlabsio/outlabsAuth-docs/edit/main/content',
      links: [{
        icon: 'i-lucide-package',
        label: 'PyPI package',
        to: 'https://pypi.org/project/outlabs-auth/',
        target: '_blank'
      }, {
        icon: 'i-lucide-layout-dashboard',
        label: 'Auth UI guide',
        to: '/integrations/outlabsauth-ui'
      }, {
        icon: 'i-lucide-workflow',
        label: 'Use Auth with TaskQ',
        to: '/integrations/taskq'
      }, {
        icon: 'i-lucide-book-open',
        label: 'TaskQ docs',
        to: 'https://taskq.outlabs.io/'
      }]
    }
  }
})
