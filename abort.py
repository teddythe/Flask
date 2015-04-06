from flask import Flask
from flask import abort
app = Flask(__name__)

@app.route('/')
def index():
  return '<h1>Hello World!</h1>'

@app.route('/user/<name>')
def user(name):
  if name != 'Teddy':
    abort(404)
  return '<h1> Hello %s!</h1>' % name

if __name__ == '__main__':
  app.run(debug = True)
