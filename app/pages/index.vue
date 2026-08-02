<script setup lang="ts">
const { data: page } = await useAsyncData('index', () => queryCollection('landing').path('/').first())
if (!page.value) {
  throw createError({ statusCode: 404, statusMessage: 'Page not found', fatal: true })
}

const title = page.value.seo?.title || page.value.title
const description = page.value.seo?.description || page.value.description

const stack = [
  'i-simple-icons-fastapi',
  'i-simple-icons-python',
  'i-simple-icons-postgresql',
  'i-simple-icons-redis',
  'i-simple-icons-pypi',
  'i-simple-icons-prometheus'
]

const ownershipFeatures = [
  {
    title: 'Mounted in your app',
    description: 'Choose the router prefix and expose only the auth surfaces your product needs.',
    icon: 'i-lucide-route'
  },
  {
    title: 'Stored in your Postgres',
    description: 'Users, sessions, roles, entities, and audit events stay in infrastructure you operate.',
    icon: 'i-lucide-database'
  },
  {
    title: 'Enforced in Python',
    description: 'Typed FastAPI dependencies keep authorization beside the code they protect.',
    icon: 'i-lucide-braces'
  }
]

const capabilities = [
  {
    title: 'JWTs & sessions',
    description: 'Access and refresh tokens, optional rotation, and session management for account-security screens.',
    icon: 'i-lucide-key-round',
    to: '/auth/sessions-and-audit'
  },
  {
    title: 'OAuth & social login',
    description: 'Provider login and account linking through routers you opt into and configure.',
    icon: 'i-lucide-log-in',
    to: '/auth/oauth-and-social-login'
  },
  {
    title: 'Invites & passwordless',
    description: 'Email invites, magic links, and phone codes while you keep control of message delivery.',
    icon: 'i-lucide-send',
    to: '/auth/passwordless-and-messaging'
  },
  {
    title: 'API keys',
    description: 'Personal and system-integration keys with host-friendly hashing and management APIs.',
    icon: 'i-lucide-key',
    to: '/integrations/api-keys'
  },
  {
    title: 'Audit & activity',
    description: 'Searchable events plus optional DAU and MAU-style activity tracking for product operations.',
    icon: 'i-lucide-scroll-text',
    to: '/reference/activity-tracking'
  },
  {
    title: 'Observable by default',
    description: 'Prometheus metrics and structured logs that join the tooling your FastAPI service already uses.',
    icon: 'i-lucide-activity',
    to: '/reference/observability'
  }
]

const docs = [
  {
    title: 'Install in one sitting',
    description: 'Package, migrations, configuration, and your first mounted auth router.',
    icon: 'i-lucide-rocket',
    to: '/getting-started/getting-started'
  },
  {
    title: 'Pick the right preset',
    description: 'Choose flat RBAC or hierarchical authorization without guessing at the trade-offs.',
    icon: 'i-lucide-git-compare-arrows',
    to: '/getting-started/choosing-a-preset'
  },
  {
    title: 'Mount only what you need',
    description: 'Explore every router, prefix, and HTTP surface available to your application.',
    icon: 'i-lucide-blocks',
    to: '/build/routers-and-prefixes'
  },
  {
    title: 'Protect host routes',
    description: 'Use the current authentication, permission, entity, tree, and two-phase dependency APIs.',
    icon: 'i-lucide-shield-check',
    to: '/build/authorization-dependencies'
  }
]

useSeoMeta({
  titleTemplate: '',
  title,
  ogTitle: title,
  description,
  ogDescription: description
})

defineOgImage('Docs', {
  title,
  description,
  headline: 'FastAPI authentication and authorization'
})
</script>

<template>
  <div>
    <UPageHero
      orientation="horizontal"
      class="overflow-hidden border-b border-default"
      :ui="{
        container: 'py-20 sm:py-28 lg:py-32',
        title: 'font-display text-5xl sm:text-6xl lg:text-7xl font-semibold',
        description: 'max-w-2xl',
        links: 'gap-3'
      }"
    >
      <template #top>
        <div class="pointer-events-none absolute inset-0 -z-10 bg-[radial-gradient(circle_at_18%_20%,color-mix(in_oklab,var(--ui-primary)_14%,transparent),transparent_36%)]" />
        <div class="pointer-events-none absolute inset-x-0 top-0 -z-10 h-px bg-gradient-to-r from-transparent via-primary/60 to-transparent" />
      </template>

      <template #headline>
        <UBadge
          label="Alpha on PyPI"
          icon="i-lucide-package-check"
          color="primary"
          variant="subtle"
          size="lg"
          class="rounded-full"
        />
      </template>

      <template #title>
        Authentication, inside <span class="text-primary">your FastAPI app.</span>
      </template>

      <template #description>
        Install the library, mount the routers, and keep every user, role, and audit event in your Postgres. Start with simple RBAC and grow into org-aware authorization without moving your identity layer.
      </template>

      <template #links>
        <UButton
          label="Start building"
          to="/getting-started/getting-started"
          size="xl"
          trailing-icon="i-lucide-arrow-right"
        />
        <UButton
          label="Explore on GitHub"
          to="https://github.com/outlabsio/outlabsAuth"
          target="_blank"
          color="neutral"
          variant="outline"
          size="xl"
          icon="i-simple-icons-github"
        />
      </template>

      <UPageCard
        variant="outline"
        spotlight
        spotlight-color="primary"
        class="overflow-hidden shadow-2xl shadow-primary/10"
        :ui="{ container: 'p-0 sm:p-0 gap-0' }"
      >
        <div class="flex items-center justify-between border-b border-default bg-elevated/60 px-4 py-3">
          <div
            class="flex items-center gap-1.5"
            aria-hidden="true"
          >
            <span class="size-2.5 rounded-full bg-error" />
            <span class="size-2.5 rounded-full bg-warning" />
            <span class="size-2.5 rounded-full bg-success" />
          </div>
          <span class="font-mono text-xs text-muted">main.py</span>
          <UBadge
            label="FastAPI"
            color="neutral"
            variant="soft"
            size="sm"
          />
        </div>

        <div class="bg-default p-5 sm:p-7">
          <pre class="overflow-x-auto font-mono text-[13px] leading-6 text-toned"><code><span class="text-primary">from</span> outlabs_auth <span class="text-primary">import</span> SimpleRBAC

auth = SimpleRBAC(
    database_url=DATABASE_URL,
    secret_key=SECRET_KEY,
)

auth.prime_fastapi_routing()
app.include_router(
    get_auth_router(auth, prefix=<span class="text-primary">"/auth"</span>)
)</code></pre>
        </div>

        <div class="grid gap-px border-t border-default bg-default sm:grid-cols-3">
          <div class="bg-elevated/40 p-4">
            <UIcon
              name="i-lucide-circle-check"
              class="mb-2 size-5 text-success"
            />
            <p class="text-sm font-semibold text-highlighted">
              Mounted
            </p>
            <p class="mt-0.5 text-xs text-muted">
              /auth/*
            </p>
          </div>
          <div class="bg-elevated/40 p-4">
            <UIcon
              name="i-lucide-database"
              class="mb-2 size-5 text-primary"
            />
            <p class="text-sm font-semibold text-highlighted">
              Your database
            </p>
            <p class="mt-0.5 text-xs text-muted">
              PostgreSQL
            </p>
          </div>
          <div class="bg-elevated/40 p-4">
            <UIcon
              name="i-lucide-shield-check"
              class="mb-2 size-5 text-info"
            />
            <p class="text-sm font-semibold text-highlighted">
              Protected
            </p>
            <p class="mt-0.5 text-xs text-muted">
              Typed dependencies
            </p>
          </div>
        </div>
      </UPageCard>
    </UPageHero>

    <UContainer class="py-10 sm:py-12">
      <UPageLogos
        title="Built for the Python stack you already operate"
        :items="stack"
        :ui="{
          title: 'text-sm font-medium text-muted',
          logos: 'mt-8 justify-center gap-x-10 sm:gap-x-16',
          logo: 'size-7 sm:size-8 opacity-60 hover:opacity-100 transition-opacity'
        }"
      />
    </UContainer>

    <UPageSection
      headline="Own the control plane"
      title="Your auth should feel like part of your product"
      description="OutlabsAuth runs inside the boundary you already trust. There is no second tenant to reconcile, no remote policy engine in the request path, and no user export waiting in your future."
      :features="ownershipFeatures"
      :ui="{ container: 'border-y border-default' }"
    />

    <UPageSection
      headline="One core, two authorization models"
      title="Start simple. Keep the headroom."
      description="Choose the model that matches your product today. Both presets share the same authentication, invitation, API key, and dependency patterns."
    >
      <UPageGrid class="lg:grid-cols-2">
        <UPageCard
          title="SimpleRBAC"
          description="Flat roles and permissions for SaaS products, internal tools, and applications without hierarchy-scoped access."
          icon="i-lucide-layers-3"
          to="/getting-started/choosing-a-preset"
          variant="subtle"
          spotlight
          spotlight-color="primary"
          :ui="{ container: 'p-6 sm:p-8', leadingIcon: 'size-7' }"
        >
          <template #header>
            <UBadge
              label="The focused default"
              color="primary"
              variant="subtle"
            />
          </template>
          <template #footer>
            <div class="flex flex-wrap gap-2">
              <UBadge
                label="Roles"
                color="neutral"
                variant="soft"
              />
              <UBadge
                label="Permissions"
                color="neutral"
                variant="soft"
              />
              <UBadge
                label="FastAPI deps"
                color="neutral"
                variant="soft"
              />
            </div>
          </template>
        </UPageCard>

        <UPageCard
          title="EnterpriseRBAC"
          description="Entity trees, memberships, context-aware roles, tree permissions, and optional ABAC when the org chart is the permission model."
          icon="i-lucide-network"
          to="/enterprise/core-authorization-concepts"
          variant="outline"
          highlight
          highlight-color="primary"
          :ui="{ container: 'p-6 sm:p-8', leadingIcon: 'size-7' }"
        >
          <template #header>
            <UBadge
              label="For hierarchical products"
              color="primary"
              variant="solid"
            />
          </template>
          <template #footer>
            <div class="flex flex-wrap gap-2">
              <UBadge
                label="Entity trees"
                color="neutral"
                variant="soft"
              />
              <UBadge
                label="Memberships"
                color="neutral"
                variant="soft"
              />
              <UBadge
                label="ABAC"
                color="neutral"
                variant="soft"
              />
            </div>
          </template>
        </UPageCard>
      </UPageGrid>
    </UPageSection>

    <UPageSection
      headline="A complete auth surface"
      title="Mount the capabilities your product needs"
      description="Every surface is available through composable router factories, so you can start small and add features without changing the foundation."
      class="bg-elevated/35"
    >
      <UPageGrid>
        <UPageCard
          v-for="capability in capabilities"
          :key="capability.title"
          v-bind="capability"
          variant="naked"
          class="group"
          :ui="{
            container: 'p-5 sm:p-6 rounded-lg ring ring-default bg-default transition group-hover:ring-accented group-hover:-translate-y-0.5',
            leadingIcon: 'size-6'
          }"
        >
          <template #footer>
            <span class="inline-flex items-center gap-1 text-sm font-medium text-primary">
              Read more
              <UIcon
                name="i-lucide-arrow-up-right"
                class="size-4"
              />
            </span>
          </template>
        </UPageCard>
      </UPageGrid>
    </UPageSection>

    <UPageSection
      headline="Optional operator UI"
      title="See the system before you build the admin screens"
      description="OutlabsAuth UI connects to any mounted host and adapts to the routers it exposes. Use it as your operator console or as a working reference for a UI of your own."
      orientation="horizontal"
      reverse
      :links="[{
        label: 'Explore OutlabsAuth UI',
        to: '/integrations/outlabsauth-ui',
        trailingIcon: 'i-lucide-arrow-right'
      }]"
    >
      <UPageCard
        variant="subtle"
        class="overflow-hidden"
        :ui="{ container: 'p-0 sm:p-0 gap-0' }"
      >
        <div class="flex items-center gap-3 border-b border-default px-5 py-4">
          <div class="flex size-9 items-center justify-center rounded-lg bg-primary/10 text-primary">
            <UIcon
              name="i-lucide-layout-dashboard"
              class="size-5"
            />
          </div>
          <div>
            <p class="text-sm font-semibold text-highlighted">
              Operator console
            </p>
            <p class="text-xs text-muted">
              Connected to /auth/config
            </p>
          </div>
          <UBadge
            label="Live"
            color="success"
            variant="subtle"
            class="ml-auto"
          />
        </div>
        <div class="grid gap-px bg-default sm:grid-cols-2">
          <div
            v-for="item in [
              ['i-lucide-users', 'Users', '1,284'],
              ['i-lucide-shield', 'Roles', '12'],
              ['i-lucide-building-2', 'Entities', '48'],
              ['i-lucide-key-round', 'Active sessions', '326']
            ]"
            :key="item[1]"
            class="bg-elevated/40 p-5"
          >
            <UIcon
              :name="item[0]"
              class="size-5 text-primary"
            />
            <p class="mt-4 text-2xl font-semibold text-highlighted">
              {{ item[2] }}
            </p>
            <p class="text-sm text-muted">
              {{ item[1] }}
            </p>
          </div>
        </div>
      </UPageCard>
    </UPageSection>

    <UPageSection
      headline="Documentation"
      title="Take the shortest path to working auth"
      description="The handbook is organized around the decisions and implementation steps you will make first."
    >
      <UPageGrid>
        <UPageCard
          v-for="item in docs"
          :key="item.title"
          v-bind="item"
          variant="subtle"
          spotlight
          spotlight-color="primary"
        />
      </UPageGrid>
    </UPageSection>

    <UPageCTA
      title="Put auth inside your app"
      description="Install the alpha from PyPI, mount your first router, and keep control of the system from day one."
      orientation="horizontal"
      variant="subtle"
      class="border-y border-default"
      :links="[
        {
          label: 'Read the quickstart',
          to: '/getting-started/getting-started',
          trailingIcon: 'i-lucide-arrow-right',
          color: 'primary'
        },
        {
          label: 'View on PyPI',
          to: 'https://pypi.org/project/outlabs-auth/',
          target: '_blank',
          icon: 'i-simple-icons-pypi',
          color: 'neutral',
          variant: 'outline'
        }
      ]"
    >
      <template #top>
        <div class="pointer-events-none absolute inset-0 -z-10 bg-[radial-gradient(circle_at_85%_50%,color-mix(in_oklab,var(--ui-primary)_12%,transparent),transparent_30%)]" />
      </template>
      <div class="flex items-center justify-center gap-3 lg:justify-end">
        <UIcon
          name="i-simple-icons-fastapi"
          class="size-10 text-muted"
        />
        <UIcon
          name="i-lucide-plus"
          class="size-5 text-dimmed"
        />
        <img
          src="/outlabsAuthLogo.svg"
          alt="OutlabsAuth"
          class="h-12 w-auto brightness-0 dark:brightness-100"
        >
      </div>
    </UPageCTA>
  </div>
</template>
