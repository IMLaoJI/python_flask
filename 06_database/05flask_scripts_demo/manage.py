#encoding: utf-8

from flask_script import Manager
from zhiliao import app,BackendUser,db
from db_script import db_manager

manager = Manager(app)
manager.add_command("db",db_manager)

@manager.command
def greet():
    print('你好')

# @manager.option("-u","--username",dest="username")
# @manager.option("-a","--age",dest="age")
# def add_user(username,age):
#     print("您输入的用户名是：%s，年龄是：%s" % (username,age))

@manager.option("-u","--username",dest="username")
@manager.option("-e","--email",dest="email")
def add_user(username,email):
    user = BackendUser(username=username,email=email)
    db.session.add(user)
    db.session.commit()


if __name__ == '__main__':
    manager.run()