from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
from dbMock import dataBaseInMemory

app = Flask(__name__)
CORS(app)
api = Api(app)



class Articles(Resource):
    def get(self): 
        return dataBaseInMemory
    
    def post(self):
        data = request.json
        itemId = len(dataBaseInMemory) + 1
        dataBaseInMemory.append({
        'id': itemId,
        'title': data['title'],
        'content': data['content'],
        'image': {
            'alt': data['image'].get('alt') or '',
            'src': data['image']['src']
        },
        'createdAt': datetime.today().strftime('%Y-%m-%d')
       })
        return dataBaseInMemory[itemId -1]
    
class Article(Resource): 
    def get(self, pk):
        return dataBaseInMemory[pk]
    
api.add_resource(Articles, '/articles')
api.add_resource(Article, '/article/<int:pk>')

if __name__ == '__main__':
    app.run(debug=True)