<template>
  <back-to-home-btn />
  <div class="q-pa-md q-gutter-md article">
    <div class="row justify-between">
      <q-parallax :src="article?.image.src">
        <h1 class="text-white">{{ article?.title }}</h1>
      </q-parallax>
    </div>
    <div class="article__content text-body1 q-px-sm">{{ article?.content }}</div>
  </div>
</template>

<script setup lang="ts">
import { Article } from 'src/components/articles/models/Article'
import { ArticleService } from 'src/services/articles.service'
import { useArticleStore } from 'src/stores/articles'
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import BackToHomeBtn from 'src/components/articles/BackToHomeBtn.vue'

defineOptions({
  name: 'IndividualArticlePage',
})
const router = useRouter()
const article = ref<Article | undefined>()
const articleId = ref(parseInt(router.currentRoute.value.params.id as string))

article.value = useArticleStore().articles.find(
  article => article.id == parseInt(router.currentRoute.value.params.id as string)
)

if (!article.value) {
  article.value = await ArticleService.getOneById(articleId.value)
}
</script>

<style lang="scss">
.article {
  &__content {
    text-wrap: balance;
    text-align: center;
  }
}
</style>
