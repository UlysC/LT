import axios from 'axios';
import { Article } from 'src/components/articles/models/Article';

export class ArticleService {
  public static async getAll(): Promise<Article[]> {
    return (await axios.get('http://127.0.0.1:5000/articles')).data;
  }
}
