from flask import Flask,request,render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/list/',methods=['POST'])
def my_list():
    return 'list'

@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        return 'success'


if __name__ == '__main__':
    # host
    app.run(debug=True,host='0.0.0.0')
