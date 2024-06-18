export interface ArticleImage {
    src: string;
    alt?: string;
}

export interface Article {
    id: number;
    title: string;
    content: string;
    image: ArticleImage;
    createdAt: string
}