from flask import Flask,render_template
import os
from ueditor import bp
import config

app = Flask(__name__)
app.config.from_object(config)

app.register_blueprint(bp)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True,port=9000)
