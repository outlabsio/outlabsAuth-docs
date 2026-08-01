---
seo:
  title: OutlabsAuth — Auth you embed in FastAPI
  description: Library-first authentication and authorization for FastAPI. Your Postgres, your routers, Simple or Enterprise RBAC, optional admin console — not a black-box IdP.
---

::u-page-hero{class="bg-gradient-to-b from-orange-50/70 via-default to-default dark:from-orange-950/25 dark:via-default dark:to-default"}
---
orientation: horizontal
---
#top
:hero-background

#headline
  :::u-badge
  ---
  label: Alpha on PyPI · outlabs-auth
  color: primary
  variant: subtle
  size: md
  ---
  :::

#title
:hero-logo

#description
Authentication you **embed**, not rent. Mount a library into your FastAPI app, keep users and roles in **your** Postgres, and grow from flat RBAC to an org tree without switching products.

#links
  :::u-button
  ---
  to: /getting-started/getting-started
  size: xl
  trailing-icon: i-lucide-arrow-right
  ---
  Get started
  :::

  :::u-button
  ---
  to: /getting-started/choosing-a-preset
  color: neutral
  variant: outline
  size: xl
  ---
  Choose a preset
  :::

  :::u-button
  ---
  to: https://github.com/outlabsio/outlabsAuth
  target: _blank
  color: neutral
  variant: ghost
  size: xl
  icon: i-simple-icons-github
  ---
  GitHub
  :::

#default
  :::prose-pre
  ---
  code: |
    from outlabs_auth import SimpleRBAC
    from outlabs_auth.routers import get_auth_router

    auth = SimpleRBAC(
        database_url=os.environ["DATABASE_URL"],
        secret_key=os.environ["SECRET_KEY"],
    )
    auth.prime_fastapi_routing()
    app.include_router(get_auth_router(auth, prefix="/auth"))
  filename: main.py
  ---

  ```python [main.py]
  from outlabs_auth import SimpleRBAC
  from outlabs_auth.routers import get_auth_router

  auth = SimpleRBAC(
      database_url=os.environ["DATABASE_URL"],
      secret_key=os.environ["SECRET_KEY"],
  )
  auth.prime_fastapi_routing()
  app.include_router(get_auth_router(auth, prefix="/auth"))
  ```
  :::
::

::u-page-logos
---
title: Built for the stack you already run
marquee: true
items:
  - i-simple-icons-fastapi
  - i-simple-icons-postgresql
  - i-simple-icons-python
  - i-simple-icons-redis
  - i-simple-icons-pypi
  - i-simple-icons-prometheus
---
::

::u-page-section
---
headline: Why OutlabsAuth
---
#title
Auth that stays inside your product

#description
No separate IdP tenancy. No “export your users later.” You install the package, mount the routers you need, and keep the full control plane in your deployment.

  :::u-page-grid
    ::::u-page-card
    ---
    icon: i-lucide-package
    variant: subtle
    spotlight: true
    spotlight-color: primary
    ---
    #title
    Library, not a service

    #description
    `pip install outlabs-auth`, wire FastAPI, migrate Postgres. The auth API is *your* API under the prefix you choose.
    ::::

    ::::u-page-card
    ---
    icon: i-lucide-database
    variant: subtle
    spotlight: true
    spotlight-color: primary
    ---
    #title
    Your database, your schema

    #description
    Users, roles, entities, and audit live in PostgreSQL you operate — optionally in a dedicated schema beside the rest of the app.
    ::::

    ::::u-page-card
    ---
    icon: i-lucide-waypoints
    variant: subtle
    spotlight: true
    spotlight-color: primary
    ---
    #title
    Grow without a rewrite

    #description
    Start with SimpleRBAC. Flip on Enterprise hierarchy, ABAC, OAuth, or passwordless when the product needs them — same core, same deps.
    ::::
  :::
::

::u-page-section
---
headline: Presets
---
#title
Two clear starting points

#description
Pick the preset that matches your org model. Both share the same JWT, API key, invite, and dependency patterns.

  :::u-page-grid{class="lg:grid-cols-2"}
    ::::u-page-card
    ---
    icon: i-lucide-layers
    to: /getting-started/choosing-a-preset
    variant: outline
    highlight: true
    highlight-color: primary
    orientation: vertical
    ---
    #title
    SimpleRBAC

    #description
    Flat roles and permissions. Ideal for SaaS tools, internal apps, and products that do not need departments or tree-scoped access.
    ::::

    ::::u-page-card
    ---
    icon: i-lucide-network
    to: /enterprise/core-authorization-concepts
    variant: outline
    highlight: true
    highlight-color: primary
    orientation: vertical
    ---
    #title
    EnterpriseRBAC

    #description
    Entity hierarchy with a closure table, memberships, context-aware roles, tree permissions, and optional ABAC — when the org chart *is* the permission model.
    ::::
  :::
::

::u-page-section
---
headline: Surface
orientation: horizontal
---
#title
The auth surface product teams actually need

#description
Sign-in, provisioning, keys, and ops hooks — exposed as router factories you mount à la carte. Customer-facing screens stay yours; OutlabsAuth owns the contracts.

#features
  :::u-page-feature
  ---
  icon: i-lucide-key-round
  ---
  #title
  JWTs & sessions

  #description
  Access + refresh tokens, optional rotation, and session listing for account security screens.
  :::

  :::u-page-feature
  ---
  icon: i-lucide-key
  ---
  #title
  API keys

  #description
  Personal and system-integration keys with host-friendly hashing and admin surfaces.
  :::

  :::u-page-feature
  ---
  icon: i-lucide-send
  ---
  #title
  Invites & passwordless

  #description
  Invite-by-email, magic links, and phone access codes — you own delivery (SMTP, Twilio, Meta, …).
  :::

  :::u-page-feature
  ---
  icon: i-lucide-log-in
  ---
  #title
  OAuth & social

  #description
  Provider login and account linking when you mount the OAuth routers.
  :::

  :::u-page-feature
  ---
  icon: i-lucide-scroll-text
  ---
  #title
  Audit & activity

  #description
  Searchable user audit events plus optional DAU/MAU-style activity tracking.
  :::

  :::u-page-feature
  ---
  icon: i-lucide-gauge
  ---
  #title
  Ops-ready

  #description
  Packaged migrations, CLI bootstrap, Redis or memory cache, Prometheus metrics in your scrape.
  :::
::

::u-page-section
---
headline: Sidecar console
---
#title
See everything — without building the admin UI first

#description
Point a ready-made operator console at any mounted host, or treat it as a reference implementation for your own UI.

#body
  :::u-page-card
  ---
  icon: i-lucide-layout-dashboard
  to: /integrations/outlabsauth-ui
  variant: soft
  orientation: horizontal
  spotlight: true
  spotlight-color: primary
  ---
  #title
  OutlabsAuth UI

  #description
  A Vite/React sidecar we maintain and use ourselves. Users, roles, entities, keys, audit, and more adapt from `/auth/config` — full gamut when the matching routers are mounted.
  :::
::

::u-page-section
---
headline: Docs
---
#title
Start where you are

#description
Jump into the handbook path that matches what you are shipping this week.

  :::u-page-grid
    ::::u-page-card
    ---
    icon: i-lucide-rocket
    to: /getting-started/getting-started
    variant: subtle
    ---
    #title
    Getting Started

    #description
    Install → migrate → mount → first login in one sitting.
    ::::

    ::::u-page-card
    ---
    icon: i-lucide-route
    to: /build/routers-and-prefixes
    variant: subtle
    ---
    #title
    Routers & Prefixes

    #description
    The menu of HTTP surfaces for your app and the admin console.
    ::::

    ::::u-page-card
    ---
    icon: i-lucide-building-2
    to: /enterprise/core-authorization-concepts
    variant: subtle
    ---
    #title
    Enterprise concepts

    #description
    Entities, memberships, and tree permissions when hierarchy matters.
    ::::

    ::::u-page-card
    ---
    icon: i-lucide-settings
    to: /build/configuration
    variant: subtle
    ---
    #title
    Configuration

    #description
    Secrets, schema, Redis, cache backends, and the CLI.
    ::::

    ::::u-page-card
    ---
    icon: i-lucide-shield
    to: /auth/roles-and-permissions
    variant: subtle
    ---
    #title
    Roles & permissions

    #description
    Permission catalog, role composition, and how deps enforce access.
    ::::

    ::::u-page-card
    ---
    icon: i-lucide-eye
    to: /reference/observability
    variant: subtle
    ---
    #title
    Observability

    #description
    Metrics and structured logs without taking over your FastAPI app.
    ::::
  :::
::

::u-page-section
  :::u-page-c-t-a
  ---
  links:
    - label: Read the docs
      to: '/getting-started/introduction'
      trailingIcon: i-lucide-arrow-right
    - label: View on GitHub
      to: 'https://github.com/outlabsio/outlabsAuth'
      target: _blank
      variant: subtle
      icon: i-simple-icons-github
  title: Ready to embed OutlabsAuth?
  description: Alpha on PyPI — pip install outlabs-auth and follow Getting Started. Your app, your database, your auth.
  ---

  :stars-bg
  :::
::
