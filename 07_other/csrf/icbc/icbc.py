#coding: utf8
from flask import Flask,views
import flask
from exts import db
from models import User
import config
from forms import LoginForm,RegistForm,TransferForm
import constants
from auth import login_required
from flask_wtf import CsrfProtect



app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
# CsrfProtect(app)


@app.route('/')
def index():
    return '<h1>欢迎来到工商银行！</h1>'


class LoginView(views.MethodView):

    def get(self):
        return flask.render_template('login.html')

    def post(self):
        form = LoginForm(flask.request.form,csrf_enabled=False)
        if form.validate():
            email = form.email.data
            password = form.password.data
            remember = form.remember.data

            # 登录
            user = User.query.filter_by(email=email,password=password).first()
            flask.session[constants.USER_SESSION_ID] = user.id

            if remember:
                flask.session.permanent = True

            return flask.redirect(flask.url_for('index'))
        else:
            print(form.errors)
            return u'登录失败！'


class RegistView(views.MethodView):

    def get(self):
        return flask.render_template('regist.html')

    def post(self):
        form = RegistForm(flask.request.form,csrf_enabled=False)
        if form.validate():
            email = form.email.data
            username = form.username.data
            password = form.password.data
            deposit = form.deposit.data or 0
            user = User(email=email,username=username,password=password,deposit=deposit)
            db.session.add(user)
            db.session.commit()
            # 跳转到主页
            return flask.redirect(flask.url_for('index'))
        else:
            print(form.errors)
            return u'注册失败'

class TransferView(views.MethodView):

    decorators = [login_required]

    def get(self):
        return flask.render_template('transfer.html')

    def post(self):
        form = TransferForm(flask.request.form)
        if form.validate():
            email = form.email.data
            money = form.money.data
            user = User.query.filter_by(email=email).first()
            uid = flask.session.get(constants.USER_SESSION_ID)
            myself = User.query.get(uid)
            if myself.deposit > money:
                user.deposit += money
                myself.deposit -= money
                db.session.commit()
                return u'转账成功！'
            else:
                return u'余额不足！'
        else:
            print(form.errors)
            return 'fail'


app.add_url_rule('/login/',view_func=LoginView.as_view('login'))
app.add_url_rule('/regist/',view_func=RegistView.as_view('regist'))
app.add_url_rule('/transfer/',view_func=TransferView.as_view('transfer'))


if __name__ == '__main__':
    app.run(debug=True,port=80)
