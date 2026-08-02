<script setup lang="ts">
const { footer } = useAppConfig()
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
