#coding: utf8
from flask import Flask
import flask

app = Flask(__name__)


@app.route('/')
def index():
    return flask.render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True,port=9000)
