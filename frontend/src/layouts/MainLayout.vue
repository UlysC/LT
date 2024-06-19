<template>
  <q-layout>
    <q-page-container class="container">
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script setup lang="ts">
defineOptions({
  name: 'MainLayout',
})
</script>

<style>
.container {
  width: 85%;
  margin: auto;
}

@media (max-width: 768px) {
  .container {
    width: 100%;
  }
}
</style>
