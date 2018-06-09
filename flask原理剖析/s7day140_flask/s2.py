from flask import Flask,flash,get_flashed_messages

app = Flask(__name__)
app.secret_key = 'asdfasdf'
@app.route('/get')
def get():
    # 从某个地方获取设置过的所有值，并清除。
    data = get_flashed_messages()
    print(data)
    return 'Hello World!'


@app.route('/set')
def set():
    # 向某个地方设置一个值
    flash('阿斯蒂芬')

    return 'Hello World!'


if __name__ == '__main__':
    app.run()