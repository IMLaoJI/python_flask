from flask import Flask,request

app = Flask(__name__)

@app.route("/")
def hello():
    print(request)
    return "Hello World"

if __name__ == '__main__':
    app.__call__
    app.request_class
    app.run()