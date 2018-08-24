from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')

class VideoForm(FlaskForm):
    switch_map = BooleanField('Open the map')
    switch_video = BooleanField('Open the video')
    submit = SubmitField('Submit')