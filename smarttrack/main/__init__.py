from flask import Blueprint
import os

main = Blueprint('main', __name__)

import views, forms
