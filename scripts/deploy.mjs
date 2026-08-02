#!/usr/bin/env bun

import { spawnSync } from 'node:child_process'

const ENVIRONMENT_MAP = {
  production: 'production',
  prod: 'production',
  main: 'production',
  staging: 'staging'
}

const args = process.argv.slice(2)
const dryRun = args.includes('--dry-run')
const envArg = args.find(arg => !arg.startsWith('-'))
const environment = envArg ? ENVIRONMENT_MAP[envArg.toLowerCase()] : undefined

if (!environment) {
  printUsage()
  process.exit(1)
}

const buildScript = environment === 'production' ? 'build:production' : 'build:staging'
const wranglerConfig = environment === 'production' ? 'wrangler.main.jsonc' : 'wrangler.staging.jsonc'
const steps = [
  {
    label: 'Generate static Nuxt site',
    command: ['bun', 'run', buildScript]
  },
  {
    label: 'Deploy to Cloudflare Workers',
    command: ['bunx', 'wrangler', 'deploy', '--config', wranglerConfig]
  }
]

console.log(`Deploy target: ${environment}`)

if (dryRun) {
  console.log('Dry run enabled. Planned steps:')

  for (const step of steps) {
    console.log(`- ${step.label}: ${step.command.join(' ')}`)
  }

  process.exit(0)
}

for (const step of steps) {
  console.log(`\n==> ${step.label}`)
  run(step.command)
}

function run(command) {
  const [cmd, ...cmdArgs] = command
  const result = spawnSync(cmd, cmdArgs, {
    cwd: process.cwd(),
    stdio: 'inherit',
    env: process.env
  })

  if (result.status !== 0) {
    process.exit(result.status ?? 1)
  }
}

function printUsage() {
  console.error('Usage: bun run deploy <staging|production> [--dry-run]')
  console.error('Note: `bun deploy` is reserved by the Bun CLI and cannot be used for package scripts.')
}
