from flask_restful import Resource
from dbMock import dataBaseInMemory
from flask import request
from datetime import datetime

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
        return dataBaseInMemory[pk - 1]