from flask import Flask,request,g

app = Flask(__name__)

@app.before_request
def before():
    g.permission_code_list = ['list','add']


@app.route('/',methods=['GET',"POST"])
def index():
    print(g.permission_code_list)
    return "index"


if __name__ == '__main__':
    app.run()