"""
The flask application package.
"""

from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

import smarttrack.views

 
mongo = PyMongo(app, uri="mongodb://localhost:27017/runoobdb")
 