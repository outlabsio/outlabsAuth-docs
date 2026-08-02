// https://nuxt.com/docs/api/configuration/nuxt-config
const siteUrl = process.env.NUXT_SITE_URL || 'https://auth.outlabs.io'

export default defineNuxtConfig({
  modules: [
    '@nuxt/eslint',
    '@nuxt/image',
    '@nuxt/ui',
    '@nuxt/content',
    'nuxt-og-image',
    'nuxt-llms',
    '@nuxtjs/mcp-toolkit'
  ],

  devtools: {
    enabled: true
  },

  // Umami (self-hosted). Only inject on production builds so local `nuxt dev`
  // does not pollute auth.outlabs.io analytics. SPA navigations are tracked
  // automatically by the Umami script via the History API.
  app: {
    head: {
      script: process.env.NODE_ENV === 'production'
        ? [{
            'src': 'https://analytics.outlabs.io/script.js',
            'defer': true,
            'data-website-id': 'f883bacb-b746-4036-9ece-187a0d84513e'
          }]
        : []
    }
  },

  css: ['~/assets/css/main.css'],

  site: {
    url: siteUrl,
    name: 'OutlabsAuth Docs'
  },

  content: {
    build: {
      markdown: {
        toc: {
          searchDepth: 1
        }
      }
    },
    experimental: {
      sqliteConnector: 'native'
    }
  },

  runtimeConfig: {
    public: {
      siteUrl
    }
  },

  experimental: {
    asyncContext: true
  },

  compatibilityDate: '2026-06-30',

  nitro: {
    preset: 'static',
    prerender: {
      routes: [
        '/'
      ],
      crawlLinks: true
    }
  },

  eslint: {
    config: {
      stylistic: {
        commaDangle: 'never',
        braceStyle: '1tbs'
      }
    }
  },

  // Fonts via @nuxt/fonts (registered by Nuxt UI) — families referenced in CSS
  fonts: {
    families: [
      { name: 'DM Sans', provider: 'google', weights: [400, 500, 600, 700] },
      { name: 'Fraunces', provider: 'google', weights: [500, 600, 700] }
    ]
  },

  llms: {
    domain: siteUrl,
    title: 'OutlabsAuth',
    description: 'Library-first authentication and authorization for FastAPI.',
    full: {
      title: 'OutlabsAuth — Full Documentation',
      description: 'Complete OutlabsAuth implementer documentation.'
    },
    sections: [
      {
        title: 'Getting Started',
        contentCollection: 'docs',
        contentFilters: [
          { field: 'path', operator: 'LIKE', value: '/getting-started%' }
        ]
      },
      {
        title: 'Build',
        contentCollection: 'docs',
        contentFilters: [
          { field: 'path', operator: 'LIKE', value: '/build%' }
        ]
      },
      {
        title: 'Auth',
        contentCollection: 'docs',
        contentFilters: [
          { field: 'path', operator: 'LIKE', value: '/auth%' }
        ]
      },
      {
        title: 'Enterprise',
        contentCollection: 'docs',
        contentFilters: [
          { field: 'path', operator: 'LIKE', value: '/enterprise%' }
        ]
      },
      {
        title: 'Integrations',
        contentCollection: 'docs',
        contentFilters: [
          { field: 'path', operator: 'LIKE', value: '/integrations%' }
        ]
      },
      {
        title: 'Reference',
        contentCollection: 'docs',
        contentFilters: [
          { field: 'path', operator: 'LIKE', value: '/reference%' }
        ]
      }
    ]
  },

  mcp: {
    name: 'OutlabsAuth Docs'
  },

  ogImage: {
    zeroRuntime: true
  }
})
