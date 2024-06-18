import { Article } from './Article';

export type SaveArticlePayload = Omit<Article, 'id' | 'createdAt'>