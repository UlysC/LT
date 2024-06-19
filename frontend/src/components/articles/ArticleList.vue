<template>
  <div class="q-pa-md">
    <q-list bordered separator>
      <q-item
        v-for="article of articles"
        :key="article.id"
        clickable
        v-ripple
        @click="onArticleClick(article.id)"
        :style="{ height: '100px' }"
      >
        <q-item-section>
          <q-img :src="article.image.src" :alt="article.image.alt" height="100%" class="border" />
        </q-item-section>
        <q-item-section :style="{ textWrap: 'balance' }">
          <q-item-label class="text-subtitle2">
            {{ article.title }}
          </q-item-label>
          <q-item-label class="text-body2" lines="2">
            {{ article.content }}
          </q-item-label></q-item-section
        >
        <q-item-section side top>
          <span class="text-caption">{{ article.createdAt }}</span></q-item-section
        >
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
