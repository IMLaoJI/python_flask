#coding: utf8

from exts import db
from sbbs import app
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
from models import cmsmodels
from models import commonmodels
from models import frontmodels
from werkzeug.security import generate_password_hash
from sqlalchemy.orm.collections import InstrumentedList

CMSUser = cmsmodels.CMSUser
CMSRole = cmsmodels.CMSRole
CMSPermission = cmsmodels.CMSPermission

FrontUser = frontmodels.FrontUser

BoardModel = commonmodels.BoardModel
PostModel = commonmodels.PostModel

migrate = Migrate(app,db)
manager = Manager(app)

manager.add_command('db',MigrateCommand)

# @manager.option('-e','--email',dest='email')
# @manager.option('-u','--username',dest='username')
# @manager.option('-p','--password',dest='password')
# def create_cms_user(email,username,password):
#     user = CMSUser.query.filter_by(email=email).first()
#     if user:
#         print u'该邮箱已经存在！'
#         return
#     else:
#         user = CMSUser(email=email,username=username,password=password)
#         db.session.add(user)
#         db.session.commit()
#         print u'恭喜！CMS用户添加成功！'

@manager.option('-n','--name',dest='name')
@manager.option('-d','--desc',dest='desc')
@manager.option('-p','--permissions',dest='permissions')
def create_role(name,desc,permissions):
    role = CMSRole(name=name.encode('utf8'),desc=desc.encode('utf-8'),permissions=permissions)
    db.session.add(role)
    db.session.commit()
    print(u'恭喜！角色添加成功！')


@manager.option('-e','--email',dest='email')
@manager.option('-u','--username',dest='username')
@manager.option('-p','--password',dest='password')
@manager.option('-r','--role_name',dest='role')
def create_cms_user(email,username,password,role):
    user = CMSUser.query.filter_by(email=email).first()
    if user:
        print(u'邮箱已经存在！')
        return
    roleModel = CMSRole.query.filter_by(name=role.encode('utf-8')).first()
    if not roleModel:
        print(u'角色不存在！')
        return
    user = CMSUser(username=username,password=password,email=email)
    roleModel.users.append(user)
    db.session.commit()
    print(u'恭喜！cms用户添加成功！')

@manager.option('-t','--telephone',dest='telephone')
@manager.option('-u','--username',dest='username')
@manager.option('-p','--password',dest='password')
def create_front_user(telephone,username,password):
    user = FrontUser(telephone=telephone,username=username,password=password)
    db.session.add(user)
    db.session.commit()
    print(u'恭喜！添加成功!')

@manager.option('-c','--count',dest='count')
def create_test_articles(count):
    count = int(count)
    for x in range(count):
        title = '帖子标题%s' % (x+1)
        content = '帖子内容%s' % (x+1)
        post = PostModel(title=title,content=content)
        post.author = FrontUser.query.first()
        post.board = BoardModel.query.first()
        db.session.add(post)
        db.session.commit()
    print(u'添加成功！')

@manager.option('-t','--telephone',dest='telephone')
@manager.option('-p','--password',dest='password')
def reset_pwd(telephone,password):
    user = FrontUser.query.filter_by(telephone=telephone).first()
    if user:
        user.password = password
        db.session.commit()
        print('恭喜！密码修改成功！')



@manager.command
def test_permission():
    user = CMSUser.query.filter_by(email='970138074@qq.com').first()
    print(user.permissions())

@manager.command
def test_board():
    board = BoardModel.query.first()
    # list类型没有filter方法
    # Query.filter
    print(type(board.posts))


if __name__ == '__main__':
    manager.run()