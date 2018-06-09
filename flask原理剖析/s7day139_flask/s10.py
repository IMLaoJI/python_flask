from flask import Flask,render_template,Markup,jsonify,make_response
app = Flask(__name__)


def func1(arg):
    return Markup("<input type='text' value='%s' />" %(arg,))

@app.route('/')
def index():
    # return jsonify({'k1':'v1'})
    # return render_template('s10index.html',ff = func1)
    # response =  make_response("asdfasdf")
    # response.set_cookie
    # return response
    pass


if __name__ == '__main__':
    app.run()