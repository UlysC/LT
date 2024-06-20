from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from controllers.ArticleControllers import Articles, Article

app = Flask(__name__)
CORS(app)
api = Api(app)
    
api.add_resource(Articles, '/articles')
api.add_resource(Article, '/article/<int:pk>')

if __name__ == '__main__':
    app.run(debug=True)