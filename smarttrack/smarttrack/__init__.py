"""
The flask application package.
"""

from flask import Flask
from flask_pymongo import PyMongo
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_moment import Moment

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'


def create_app(config_name):
    app = Flask(__name__)

    bootstrap.init_app()
    mail.init_app()
    db.init_app()
    moment.init_app()
    login_manager.init_app()

    return app

 