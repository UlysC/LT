import axios, { AxiosResponse } from 'axios'
import { Article } from 'src/components/articles/models/Article'
import { SaveArticlePayload } from 'src/components/articles/models/SaveArticlePayload'

export class ArticleService {
  public static async getAll(): Promise<Article[]> {
    return (await axios.get('http://127.0.0.1:5000/articles')).data
  }

  public static async saveArticle(article: SaveArticlePayload): Promise<AxiosResponse<Article>> {
    return axios.post('http://127.0.0.1:5000/articles', article)
  }

  public static async getOneById(id: number): Promise<Article> {
    return (await axios.get(`http://127.0.0.1:5000/article/${id}`)).data || null
  }
}
