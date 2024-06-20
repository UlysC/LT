<template>
  <q-spinner v-if="!articles" size="50" class="q-m-auto"></q-spinner>
  <suspense v-else>
    <article-list :articles="articles"></article-list>
  </suspense>
</template>

<script setup lang="ts">
import ArticleList from 'components/articles/ArticleList.vue'
import { useArticleStore } from 'src/stores/articles'

defineOptions({
  name: 'ArticleListPage',
})
await useArticleStore().setArticles()
const { articles } = useArticleStore()
</script>
