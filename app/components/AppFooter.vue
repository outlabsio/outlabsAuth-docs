<script setup lang="ts">
const { footer, relatedDocs } = useAppConfig()
</script>

<template>
  <UFooter>
    <template #left>
      <div class="flex flex-wrap items-center gap-x-2 gap-y-1">
        <span>{{ footer.credits }}</span>
        <span aria-hidden="true">·</span>
        <ULink
          to="https://github.com/outlabsio/outlabsAuth/blob/main/LICENSE"
          target="_blank"
          class="font-medium text-primary hover:underline"
        >
          MIT License
        </ULink>
      </div>
    </template>

    <nav
      aria-label="Outlabs documentation"
      class="flex flex-wrap items-center justify-center gap-x-4 gap-y-2 text-sm"
    >
      <ULink
        v-for="link in relatedDocs"
        :key="link.to"
        :to="link.to"
        class="font-medium text-primary hover:underline"
      >
        {{ link.label }}
      </ULink>
    </nav>

    <template #right>
      <UColorModeButton v-if="footer?.colorMode" />

      <template v-if="footer?.links">
        <UButton
          v-for="(link, index) of footer?.links"
          :key="index"
          v-bind="{ color: 'neutral', variant: 'ghost', ...link }"
        />
      </template>
    </template>
  </UFooter>
</template>
