from flask import Flask,request
from utils import msg
from utils.message import send_msgs

app = Flask(__name__)

@app.route('/')
def index():
    data = request.query_string.get('val')
    if data == "xyy":
        send_msgs('.....')

    return 'Hello World!'


if __name__ == '__main__':
    app.run()