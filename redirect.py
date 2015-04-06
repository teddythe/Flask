from flask import redirect
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return redirect('http://teddy-the.strikingly.com')

if __name__ == '__main__':
  app.run(debug=True)
