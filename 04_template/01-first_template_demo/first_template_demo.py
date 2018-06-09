from flask import Flask,render_template

app = Flask(__name__,template_folder='C:/templates')

#DTL:Django Tmplate Languate
@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/list/')
def my_list():
    return render_template('posts/list.html')

if __name__ == '__main__':
    app.run(debug=True)
