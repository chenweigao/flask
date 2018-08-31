from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')

class VideoForm(FlaskForm):
    switch_map = BooleanField(u'Open the map', default=1)
    switch_video = BooleanField(u'Open the video')
    submit = SubmitField(u'Submit')