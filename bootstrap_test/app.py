"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)

bootstrap = Bootstrap(app)
moment = Moment(app)

@app.errorhandler(404)
def page_not_find(e): 
    return render_template('404.html'), 404

@app.route('/')
def index():
    return render_template('index.html', current_time=datetime.utcnow())


if __name__ == '__main__':
    app.run(port=45467, debug=True)