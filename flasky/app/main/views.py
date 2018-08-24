from flask import render_template, flash
from . import main
import os
from app import create_app, db
from app.models import User, Role
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from datetime import datetime
from flask import render_template, Flask, Response
import os
from wtforms import ValidationError

from .forms import VideoForm


@main.route('/', methods=['GET', 'POST'])
def index():
    form = VideoForm()
    map_on = form.switch_map.data
    video_on = form.switch_video.data
    
    map_switch = Role(map_switch=form.switch_map.data)
    video_switch = Role(video_switch=form.switch_video.data)
    # if map_on == True:
    #     flash(u'success open the map!')
    # else:
    #     flash(u'map closed!')

    # if video_on == True:
    #     flash(u'success open the video!')
    # else:
    #     flash(u'video closed!')
    
    db.session.add(map_switch)
    db.session.add(video_switch)
    # db.session.commit()  
    return render_template('index.html', form=form, map_on=map_on, video_on=video_on)

if os.environ.get('CAMERA'):
    Camera = import_module('camera_' + os.environ['CAMERA']).Camera
else:
    from app.camera import Camera


def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@main.route('/video_feed', methods=['GET', 'POST'])
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

        
