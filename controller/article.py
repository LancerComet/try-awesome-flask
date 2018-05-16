from app.index import app
import json

@app.route('/article/v1/list')
def getArticles () -> str:
    list = [
        'Hello, Flask!',
        'Python 3.5 with type is awesome!'
    ]
    return json.dumps({
        'name': 'wow',
        'list': list
    })

@app.route('/article/v1/controller-name')
def getControllerName () -> str:
    return 'Article'
