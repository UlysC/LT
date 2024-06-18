<template>
  <div class="q-pa-md">
    <q-list bordered separator>
      <q-item v-for="article of articles" :key="article.id" clickable v-ripple>
        <q-item-section title wrap>
          <q-item-label>
            {{ article.title }}
          </q-item-label>
        </q-item-section>
        <q-item-section thumbnail>
          <img :src="article.image.src" :alt="article.image.alt" />
        </q-item-section>
        <q-item-section no-wrap>{{ article.content }}</q-item-section>
        <q-item-section top>{{ article.createdAt }}</q-item-section>
      </q-item>
    </q-list>
  </div>
</template>

<script setup lang="ts">
import { Article } from './models/Article';

defineOptions({
  name: 'ArticleList',
});

defineProps<{
  articles: Article[];
}>();
</script>
