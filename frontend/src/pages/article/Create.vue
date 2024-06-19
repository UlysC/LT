<template>
  <div class="q-pa-md">
    <q-btn to="/" class="fixed-top-left q-ma-md"> <q-icon  name="arrow_back"/></q-btn>
    <q-form @submit="onSubmit" @reset="onReset" class="q-gutter-lg q-mt-xl">
      <q-input
        filled
        v-model="article.title"
        label="Title *"
        hint="The title of the article"
        lazy-rules
        :rules="[val => (val && val.length > 0) || 'Please type something']"
      />

      <q-input
        filled
        type="textarea"
        v-model="article.content"
        label="Content *"
        hint="A brief description"
        lazy-rules
        :rules="[val => (val !== null && val !== '') || 'Please type something']"
      />

      <q-input
        filled
        v-model="article.image!.src"
        label="Image source *"
        hint="Url of the image"
        lazy-rules
        :rules="[
          val => (val !== null && val !== '') || 'Please type something',
          val => isUrl(val) || 'Please enter a valid URL',
        ]"
      />

      <q-input filled v-model="article.image!.alt" label="Image alt" hint="Image alt text" />
      <div>
        <q-btn label="Submit" type="submit" color="primary" />
        <q-btn label="Reset" type="reset" color="primary" flat class="q-ml-sm" />
      </div>
    </q-form>
  </div>
</template>

<script setup lang="ts">
import { useQuasar } from 'quasar'
import { SaveArticlePayload } from 'src/components/articles/models/SaveArticlePayload'
import { ArticleService } from 'src/services/articles.service'
import { isUrl } from 'src/utils'
import { ref } from 'vue'

defineOptions({
  name: 'CreateArticlePage',
})

const $q = useQuasar()

const article = ref<SaveArticlePayload>({
  image: {},
})

async function onSubmit() {
  const response = await ArticleService.saveArticle(article.value)
  if (200 === response.status) {
    $q.notify({
      color: 'green-4',
      textColor: 'white',
      icon: 'cloud_done',
      message: 'Submitted',
    })
    onReset()
  }
  else {
    $q.notify({
      color: 'red-4',
      textColor: 'white',
      icon: 'warning',
      message: 'Oopsy 🤭',
    })
  }
}

function onReset() {
  article.value = { image: {} }
}
</script>
