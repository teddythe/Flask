from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from datetime import datetime
from flask.ext.moment import Moment

app = Flask(__name__)
Bootstrap(app)
Moment(app)
@app.route('/')
def index():
  return render_template('index.html', current_time=datetime.utcnow())
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

@app.errorhandler(505)
def internal_server_error(e):
	return render_template('500.html'), 500

#@app.route('/user/<name>')
#def user(name):
#  return render_template('user.html', name=name)

if __name__ == '__main__':
  app.run(debug = True, host = "0.0.0.0", port = 80)
