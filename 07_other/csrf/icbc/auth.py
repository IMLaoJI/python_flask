#coding: utf8

import constants
from flask import session
import flask
from exts import db
from models import User
from functools import wraps


def login_required(func):

    @wraps(func)
    def wrapper(*args,**kwargs):
        uid = flask.session.get(constants.USER_SESSION_ID)
        if uid and User.query.get(uid):
            return func(*args,**kwargs)
        else:
            return flask.redirect(flask.url_for('login'))

    return wrapper