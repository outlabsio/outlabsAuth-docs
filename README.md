# OutlabsAuth Docs

Public documentation for [OutlabsAuth](https://github.com/outlabsio/outlabsAuth),
built from the [Nuxt UI docs template](https://github.com/nuxt-ui-templates/docs).

Live: [https://auth.outlabs.io](https://auth.outlabs.io) (staging: [auth-staging.outlabs.io](https://auth-staging.outlabs.io))

## Conventions (do it the Nuxt way)

We follow the template + [Nuxt UI typography](https://ui.nuxt.com/docs/typography/callout) patterns:

| Pattern | How we use it |
|---------|----------------|
| File-based nav | Numbered folders (`1.getting-started/`) + `.navigation.yml` |
| Page titles | Frontmatter `title` / `description` / `navigation.icon` — **no H1 in body** |
| Callouts | `::note` `::tip` `::warning` `::caution` (not ad-hoc HTML) |
| Cards | `::card` / `::card-group` for feature grids and related links |
| Steps | `::steps{level="3"}` wrapping `###` headings for tutorials |
| Code | Fences with filenames: `` ```python [main.py] `` |
| Links | Root-relative (`/getting-started/...`), never `./file.md` |
| Fonts | `@nuxt/fonts` via Nuxt UI (`nuxt.config` `fonts.families`) |
| Landing | `content/index.md` with `::u-page-hero` / `::u-page-section` MDC |

Hand-crafted exemplars (preferred over blind port):

- `content/1.getting-started/*`
- `content/2.build/1.routers-and-prefixes.md`
- `content/5.integrations/2.outlabsauth-ui.md`

Other pages are generated from `../outlabsAuth/docs-library/` and then edited
toward the same MDC style over time.

## Setup

```bash
bun install
bun run dev
```

Open [http://localhost:3000](http://localhost:3000).

## Refresh generated pages

```bash
bun run port:handbook
# or: python3 scripts/port_handbook.py
```

The port script **skips** hand-crafted pages listed in `SKIP`.

## Branding

- `app/app.config.ts` — site name, header/footer, TOC
- `app/app.config.ts` — `ui.colors.primary: orange`, `neutral: zinc`
- `app/assets/css/main.css` — fonts + container tokens (palette via Nuxt UI semantics)
- `content/index.md` — landing
- `public/outlabsAuthLogo.svg` — header + hero wordmark

## Deployment

Same Cloudflare Workers + static assets pattern as `outlabs-site` (Wrangler custom domains).

Production:

```bash
bun run deploy production
```

Staging:

```bash
bun run deploy staging
```

`bun deploy` cannot be used here because Bun reserves that subcommand in its own CLI.

The deploy scripts:

1. Generate the static Nuxt site with the environment-specific `NUXT_SITE_URL`
2. Deploy `.output/public` using the matching Wrangler config

| Environment | URL | Wrangler config | Worker name |
|-------------|-----|-----------------|-------------|
| Production | `https://auth.outlabs.io` | `wrangler.main.jsonc` | `outlabs-auth-docs` |
| Staging | `https://auth-staging.outlabs.io` | `wrangler.staging.jsonc` | `outlabs-auth-docs-staging` |

Each config pins the OutLabs Cloudflare `account_id`, so a credential for another
account cannot receive the deployment. Custom domains must belong to an active
Cloudflare zone in that account.

Preview steps without deploying:

```bash
bun run deploy staging --dry-run
```

First-time Wrangler login (once per machine):

```bash
bunx wrangler login
```
