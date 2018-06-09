#coding: utf8

from flask_wtf import FlaskForm
from wtforms import StringField,ValidationError,IntegerField,FloatField,Form
from wtforms.validators import Email,InputRequired,Length,EqualTo
from models import User
from exts import db



class LoginForm(FlaskForm):
    email = StringField(validators=[Email(),InputRequired()])
    password = StringField(validators=[InputRequired(),Length(min=6,max=20)])
    remember = StringField()

    def validate(self):
        if not super(LoginForm,self).validate():
            return False

        email = self.email.data
        password = self.password.data
        user = User.query.filter_by(email=email,password=password).first()
        if not user:
            self.email.errors.append(u'邮箱或密码错误!')
            return False

        return True

class RegistForm(FlaskForm):
    email = StringField(validators=[Email(), InputRequired()])
    username = StringField(validators=[InputRequired(),Length(min=2,max=20)])
    password = StringField(validators=[InputRequired(), Length(min=6, max=20)])
    password_repeat = StringField(validators=[EqualTo('password')])
    deposit = FloatField(validators=[InputRequired()])

    def validate_email(self,field):
        email = field.data
        user = User.query.filter_by(email=email).first()
        if user:
            raise ValidationError(message=u'该邮箱已经注册，不能重复注册！')


class TransferForm(Form):
    email = StringField(validators=[InputRequired(),Email()])
    money = FloatField(validators=[InputRequired()])
