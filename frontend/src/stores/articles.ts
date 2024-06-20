import { defineStore } from 'pinia'
import { Article } from 'src/components/articles/models/Article'
import { ArticleService } from 'src/services/articles.service'

export const useArticleStore = defineStore('articles', {
  state: () => ({
    articles: [] as Article[],
  }),

  actions: {
    async setArticles() {
      this.articles = await ArticleService.getAll()
    },
  },

  // getters: {
  //   getArticle(id: number) {
  //     return this.articles.find(article => article.id == id)
  //   },
  // },
})
