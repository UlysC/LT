<template>
  <q-spinner v-if="!articles" size="50" class="home__spinner"></q-spinner>
  <suspense v-else>
    <article-list :articles="articles"></article-list>
  </suspense>
</template>

<script setup lang="ts">
import ArticleList from 'components/articles/ArticleList.vue';
import { Article } from 'src/components/articles/models/Article';
import { ArticleService } from 'src/services/articles.service';
import { ref } from 'vue';

defineOptions({
  name: 'IndexPage',
});

const articles = ref<Article[]>();
articles.value = await ArticleService.getAll();
</script>

<style lang="scss">
.q-spinner {
  margin: auto;
}
</style>
