from flask import Flask,flash,get_flashed_messages,request,redirect

app = Flask(__name__)
app.secret_key = 'asdfasdf'


@app.route('/index')
def index():
    # 从某个地方获取设置过的所有值，并清除。
    val = request.args.get('v')
    if val == 'oldboy':
        return 'Hello World!'
    flash('超时错误',category="x1")
    return "ssdsdsdfsd"
    # return redirect('/error')


@app.route('/error')
def error():
    """
    展示错误信息
    :return:
    """
    data = get_flashed_messages(category_filter=['x1'])
    if data:
        msg = data[0]
    else:
        msg = "..."
    return "错误信息：%s" %(msg,)


if __name__ == '__main__':
    app.run()