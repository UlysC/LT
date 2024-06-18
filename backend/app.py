from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from datetime import datetime
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
api = Api(app)


dataBaseInMemory = [
    {
        'id':1,
        'title': 'Article 1',
        'content': 'lorem ipsum dolor sit amet',
        'image': {
            'alt': 'image 1',
            'src': 'https://picsum.photos/200/300'
        },
        'createdAt': datetime.today().strftime('%Y-%m-%d')
       },
    {
        'id':2,
        'title': 'Article 2',
        'content': 'lorem ipsum dolor sit amet sit amet con laoreet et al et al et', 
        'image': {
            'alt': 'image 2',
            'src': 'https://picsum.photos/200/300'
        },
        'createdAt': datetime.today().strftime('%Y-%m-%d')
       },
    {
        'id':3,
        'title': 'Article 3',
        'content': 'lorem ipsum dolor sit amet sit amet con la reb Universal Rights rights', 
        'image': {
            'alt': 'image 3',
            'src': 'https://picsum.photos/200/300'
        },
        'createdAt': datetime.today().strftime('%Y-%m-%d')
       },
]

class Articles(Resource):
    def get(self): 
        return dataBaseInMemory
    
    def post(self):
        data = request.json
        itemId = len(dataBaseInMemory.keys()) + 1
        dataBaseInMemory[itemId] = {
        'id':itemId,
        'title': data.title,
        'content': data.content,
        'image': {
            'alt': data.image.alt,
            'src': data.image.src
        },
        'createdAt': datetime.today().strftime('%Y-%m-%d')
       }
        return dataBaseInMemory
    
class Article(Resource): 
    def get(self, pk):
        return dataBaseInMemory[pk]
    
api.add_resource(Articles, '/articles')
api.add_resource(Article, '/article/<int:pk>')

if __name__ == '__main__':
    app.run(debug=True)