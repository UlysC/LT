from db import db

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(5000), nullable=False)
    image_src = db.Column(db.String(300), nullable=False)
    image_alt = db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.DateTime(), nullable=False)
    
    def __repr__(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'image': {
                'src': self.image_src,
                'alt': self.image_alt,
            },
            'created_at': self.created_at
        }