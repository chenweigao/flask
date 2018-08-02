"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, Flask, Response
from smarttrack import app
#from smarttrack.config import MongoDB
import os
from . import main



@main.route('/')
def index():
    return render_template('index.html')

## import camera driver
#if os.environ.get('CAMERA'):
#    Camera = import_module('camera_' + os.environ['CAMERA']).Camera
#else:
#    from smarttrack.camera import Camera


#@app.route('/')
#@app.route('/home')
#def home():
#    """Renders the home page."""
#    return render_template(
#        'index.html',
#        title='Home Page',
#        year=datetime.now().year,
#    )

#@app.route('/contact')
#def contact():
#    """Renders the contact page."""
#    return render_template(
#        'contact.html',
#        title='Contact',
#        year=datetime.now().year,
#        message='Your contact page.'
#    )

#@app.route('/about')
#def about():
#    """Renders the about page."""
#    return render_template(
#        'about.html',
#        title='About',
#        year=datetime.now().year,
#        message='Your application description page.'
#    )


#def gen(camera):
#    """Video streaming generator function."""
#    while True:
#        frame = camera.get_frame()
#        yield (b'--frame\r\n'
#               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


#@app.route('/video_feed')
#def video_feed():
#    """Video streaming route. Put this in the src attribute of an img tag."""
#    return Response(gen(Camera()),
#                    mimetype='multipart/x-mixed-replace; boundary=frame')
