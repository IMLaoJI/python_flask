#coding: utf8
from flask import Flask
import flask
from exts import db,mail
import config
from views.frontviews import postviews,accountviews
from views.cmsviews import cmsviews
from flask_wtf import CSRFProtect
from flask_mail import Mail,Message
import constants
from models.frontmodels import FrontUser
from utils import xtjson

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
mail.init_app(app)

CSRFProtect(app)

app.register_blueprint(postviews.bp)
app.register_blueprint(accountviews.bp)
app.register_blueprint(cmsviews.bp)



@app.before_request
def post_before_request():
    id = flask.session.get(constants.FRONT_SESSION_ID)
    if id:
        user = FrontUser.query.get(id)
        flask.g.front_user = user

@app.context_processor
def post_context_processor():
    if hasattr(flask.g,'front_user'):
        return {'front_user': flask.g.front_user}
    return {'front_user':None}

@app.route('/test/')
def test():
    mail = Mail(app)
    message = Message(subject=u'知了课堂Python学院邮件验证码',recipients=['hynever@qq.com'],body='abcd')
    mail.send(message)
    return 'success'

@app.errorhandler(401)
def post_auth_forbidden(error):
    if flask.request.is_xhr:
        return xtjson.json_unauth_error()
    else:
        return flask.redirect(flask.url_for('account.login'))

@app.errorhandler(404)
def post_page_not_found(error):
    if flask.request.is_xhr:
        return xtjson.json_params_error()
    else:
        return flask.render_template('front/front_404.html'),404

@app.template_filter('to_list')
def to_list(value):
    return list(value)

if __name__ == '__main__':
    app.run(debug=True)
