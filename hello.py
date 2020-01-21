from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

books = [
    {
     'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'
     },
    {
     'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'
     },
    {
     'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'
     }
]

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

#Routing

@app.route('/')
def home():
    return '<h1>Home</h1>', 404


@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name

@app.errorhandler(404)
def page_not_found(error):
    return '<h1>Página no encontrada</h1>'

#API response

@app.route('/api/books/all', methods = ['GET'])
def api_all():
    #Connecting to the database
    conn = sqlite3.connect('books.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_books = cur.execute('SELECT * FROM books;').fetchall()

    return jsonify(all_books)

@app.route('/api/books', methods = ['GET'])
def api_filter():
    query_params = request.args

    id = query_params.get('id')
    published = query_params.get('published')
    author = query_params.get('author')

    query = 'SELECT * FROM books WHERE'
    to_filter = []

    if id:
        query += ' id=? AND'
        to_filter.append(id)
    if published:
        query += ' published=? AND'
        to_filter.append(published)
    if author:
        query += ' author=? AND'
        to_filter.append(author)
    if not (id or published or author):
        return page_not_found(404)
    
    query = query[:-4] + ';'

    conn = sqlite3.connect('books.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    return jsonify(results)

if __name__ == '__main__':
   app.run(debug = True)