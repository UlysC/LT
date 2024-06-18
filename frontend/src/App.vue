<template>
  <suspense>
    <router-view />
  </suspense>
</template>

<script setup lang="ts">
defineOptions({
  name: 'App',
});
</script>
