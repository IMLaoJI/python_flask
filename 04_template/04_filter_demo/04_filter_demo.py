from flask import Flask,render_template
from datetime import datetime

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
    context = {
        'position': -9,
        'signature': '<script>alert("hello")</script>',
        'persons':['zhiliao','ketang'],
        'age': "18",
        'article': 'hello zhiliao world hello',
        'create_time': datetime(2017,10,20,16,19,0)
    }
    return render_template('index.html',**context)

@app.template_filter('cut')
def cut(value):
    value = value.replace("hello",'')
    return value

@app.template_filter('handle_time')
def handle_time(time):
    """
    time距离现在的时间间隔
    1. 如果时间间隔小于1分钟以内，那么就显示“刚刚”
    2. 如果是大于1分钟小于1小时，那么就显示“xx分钟前”
    3. 如果是大于1小时小于24小时，那么就显示“xx小时前”
    4. 如果是大于24小时小于30天以内，那么就显示“xx天前”
    5. 否则就是显示具体的时间 2017/10/20 16:15
    """
    if isinstance(time,datetime):
        now = datetime.now()
        timestamp = (now - time).total_seconds()
        if timestamp < 60:
            return "刚刚"
        elif timestamp>=60 and timestamp < 60*60:
            minutes = timestamp / 60
            return "%s分钟前" % int(minutes)
        elif timestamp >= 60*60 and timestamp < 60*60*24:
            hours = timestamp / (60*60)
            return '%s小时前' % int(hours)
        elif timestamp >= 60*60*24 and timestamp < 60*60*24*30:
            days = timestamp / (60*60*24)
            return "%s天前" % int(days)
        else:
            return time.strftime('%Y/%m/%d %H:%M')
    else:
        return time


if __name__ == '__main__':
    app.run(debug=True)
