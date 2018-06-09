from flask import Flask,render_template,request,redirect,session,url_for
app = Flask(__name__)
app.debug = True
app.secret_key = 'siuljskdjfs'

USERS = {
    1:{'name':'张桂坤','age':18,'gender':'男','text':"当眼泪掉下来的时候，是真的累了， 其实人生就是这样: 你有你的烦，我有我的难，人人都有无声的泪，人人都有难言的苦。 忘不了的昨天，忙不完的今天，想不到的明天，走不完的人生，过不完的坎坷，越不过的无奈，听不完的谎言，看不透的人心放不下的牵挂，经历不完的酸甜苦辣，这就是人生，这就是生活。"},
    2:{'name':'主城','age':28,'gender':'男','text':"高中的时候有一个同学家里穷，每顿饭都是膜膜加点水，有时候吃点咸菜，我们六科老师每天下课都叫他去办公室回答问题背诵课文，然后说太晚啦一起吃个饭，后来他考上了人大，拿到通知书的时候给每个老师磕了一个头"},
    3:{'name':'服城','age':18,'gender':'女','text':"高中的时候有一个同学家里穷，每顿饭都是膜膜加点水，有时候吃点咸菜，我们六科老师每天下课都叫他去办公室回答问题背诵课文，然后说太晚啦一起吃个饭，后来他考上了人大，拿到通知书的时候给每个老师磕了一个头"},
}

@app.route('/detail/<int:nid>',methods=['GET'])
def detail(nid):
    user = session.get('user_info')
    if not user:
        return redirect('/login')

    info = USERS.get(nid)
    return render_template('detail.html',info=info)


@app.route('/index',methods=['GET'])
def index():
    user = session.get('user_info')
    if not user:
        # return redirect('/login')
        url = url_for('l1')
        return redirect(url)
    return render_template('index.html',user_dict=USERS)


@app.route('/login',methods=['GET','POST'],endpoint='l1')
def login():
    if request.method == "GET":
        return render_template('login.html')
    else:
        # request.query_string
        user = request.form.get('user')
        pwd = request.form.get('pwd')
        if user == 'alex' and pwd == '123':
            session['user_info'] = user
            return redirect('http://www.luffycity.com')
        return render_template('login.html',error='用户名或密码错误')

if __name__ == '__main__':
    app.run()