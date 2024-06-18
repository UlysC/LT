<template>
  <div class="q-pa-md">
    <q-list bordered separator>
      <q-item v-for="article of articles" :key="article.id" clickable v-ripple @click="onArticleClick(article.id)">
        <q-item-section title wrap>
          <q-item-label>
            {{ article.title }}
          </q-item-label>
        </q-item-section>
        <q-item-section thumbnail>
          <img :src="article.image.src" :alt="article.image.alt" />
        </q-item-section>
        <q-item-section>{{ article.content }}</q-item-section>
        <q-item-section top>{{ article.createdAt }}</q-item-section>
      </q-item>
    </q-list>
    <create-article-btn />
  </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'
import { Article } from './models/Article'
import CreateArticleBtn from 'src/components/articles/CreateArticleBtn.vue'

defineOptions({
  name: 'ArticleList',
})

defineProps<{
  articles: Article[]
}>()

const router = useRouter()

function onArticleClick(articleId: string | number) {
  router.push(`/${articleId}`)
}
</script>
