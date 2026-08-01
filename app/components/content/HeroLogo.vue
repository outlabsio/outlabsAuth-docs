<script setup lang="ts">
const ready = ref(false)

onMounted(() => {
  requestAnimationFrame(() => {
    ready.value = true
  })
})
</script>

<template>
  <span
    class="hero-logo relative inline-flex mx-auto lg:mx-0"
    :class="{ 'hero-logo--ready': ready }"
  >
    <span
      class="hero-logo__glow pointer-events-none absolute inset-0 -z-10"
      aria-hidden="true"
    />
    <img
      src="/outlabsAuthLogo.svg"
      alt="OutlabsAuth"
      class="hero-logo__mark relative h-28 w-auto sm:h-40 brightness-0 dark:brightness-100"
    >
  </span>
</template>

<style scoped>
.hero-logo {
  --hero-glow: color-mix(in oklab, var(--ui-primary) 55%, transparent);
}

.hero-logo__mark {
  opacity: 0;
  transform: translateY(0.75rem) scale(0.94);
  transition:
    opacity 900ms cubic-bezier(0.22, 1, 0.36, 1),
    transform 900ms cubic-bezier(0.22, 1, 0.36, 1);
}

.hero-logo--ready .hero-logo__mark {
  opacity: 1;
  transform: translateY(0) scale(1);
}

.hero-logo__glow {
  opacity: 0;
  border-radius: 9999px;
  background:
    radial-gradient(
      55% 70% at 50% 50%,
      var(--hero-glow),
      transparent 72%
    );
  filter: blur(28px);
  transform: scale(0.85);
  transition:
    opacity 1100ms ease,
    transform 1100ms ease;
}

.hero-logo--ready .hero-logo__glow {
  opacity: 0.85;
  transform: scale(1.15);
  animation: hero-logo-breathe 4.5s ease-in-out 900ms infinite;
}

@keyframes hero-logo-breathe {
  0%,
  100% {
    opacity: 0.55;
    transform: scale(1.05);
  }
  50% {
    opacity: 0.95;
    transform: scale(1.22);
  }
}

@media (prefers-reduced-motion: reduce) {
  .hero-logo__mark,
  .hero-logo__glow {
    transition: none;
    animation: none;
  }

  .hero-logo__mark {
    opacity: 1;
    transform: none;
  }

  .hero-logo__glow {
    opacity: 0.45;
    transform: scale(1.1);
  }
}
</style>
