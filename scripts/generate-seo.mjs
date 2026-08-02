#!/usr/bin/env bun

import { readdir, writeFile } from 'node:fs/promises'
import { relative, resolve, sep } from 'node:path'

const root = resolve(import.meta.dirname, '..')
const contentRoot = resolve(root, 'content')
const publicRoot = resolve(root, 'public')
const siteUrl = (process.env.NUXT_SITE_URL || 'https://auth.outlabs.io').replace(/\/$/, '')
const isProduction = new URL(siteUrl).hostname === 'auth.outlabs.io'

const markdownFiles = await findMarkdownFiles(contentRoot)
const routes = markdownFiles
  .map(toRoute)
  .filter(Boolean)
  .sort((a, b) => a.localeCompare(b))

const sitemap = [
  '<?xml version="1.0" encoding="UTF-8"?>',
  '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
  ...routes.map(route => `  <url><loc>${escapeXml(`${siteUrl}${route === '/' ? '' : `${route}/`}`)}</loc></url>`),
  '</urlset>',
  ''
].join('\n')

const robots = isProduction
  ? `User-agent: *\nAllow: /\n\nSitemap: ${siteUrl}/sitemap.xml\n`
  : 'User-agent: *\nDisallow: /\n'

await Promise.all([
  writeFile(resolve(publicRoot, 'sitemap.xml'), sitemap),
  writeFile(resolve(publicRoot, 'robots.txt'), robots)
])

console.log(`Generated SEO discovery files for ${routes.length} routes (${siteUrl})`)

async function findMarkdownFiles(directory) {
  const entries = await readdir(directory, { withFileTypes: true })
  const nested = await Promise.all(entries.map((entry) => {
    const path = resolve(directory, entry.name)
    return entry.isDirectory()
      ? findMarkdownFiles(path)
      : entry.isFile() && entry.name.endsWith('.md') ? [path] : []
  }))

  return nested.flat()
}

function toRoute(file) {
  const segments = relative(contentRoot, file)
    .split(sep)
    .map(segment => segment.replace(/\.md$/, '').replace(/^\d+\./, ''))

  if (segments.at(-1) === 'index') {
    segments.pop()
  }

  return `/${segments.join('/')}`.replace(/\/$/, '') || '/'
}

function escapeXml(value) {
  return value
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;')
    .replaceAll('\'', '&apos;')
}
