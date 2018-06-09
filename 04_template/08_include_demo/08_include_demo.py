from flask import Flask,render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def hello_world():
    return render_template('index.html',username='zhiliao')

@app.route('/detail/')
def detail():
    return render_template('course_detail.html')


if __name__ == '__main__':
    app.run(debug=True)
