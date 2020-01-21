from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Home</h1>', 404


@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name

@app.errorhandler(404)
def page_not_found(error):
    return '<h1>Página no encontrada</h1>'

@app.route('/api/books/all', methods = ['GET'])
def api_all():
    return jsonify(books)

books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

if __name__ == '__main__':
   app.run(debug = True)