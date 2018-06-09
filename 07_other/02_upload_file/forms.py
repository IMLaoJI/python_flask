#encoding: utf-8
from wtforms import Form,FileField,StringField
from wtforms.validators import InputRequired
# flask_wtf
from flask_wtf.file import FileRequired,FileAllowed

class UploadForm(Form):
    avatar = FileField(validators=[FileRequired(),FileAllowed(['jpg','png','gif'])])
    desc = StringField(validators=[InputRequired()])
