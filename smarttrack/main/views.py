
from flask import render_template
import main


@main.route('/')
def index():
    return render_template('index.html')
