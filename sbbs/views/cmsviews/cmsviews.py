#coding: utf8

import flask
from flask import Blueprint
from flask.views import MethodView
from models.cmsmodels import CMSUser,CMSRole
from models.frontmodels import FrontUser
from models.commonmodels import BoardModel,PostModel,HighlightPostModel
from exts import db,mail
from forms.cmsforms import CMSLoginForm,CMSResetpwdForm,CMSResetmailForm,CMSAddUserForm,CMSBlackListForm,CMSBlackFrontUserForm,CMSEditBoardForm,CMSHightlightPostForm
import constants
from decorators.cmsdecorators import login_required,superadmin_required
from utils import xtjson,xtcache,xtmail
import string
import random
from models.modelhelpers import PostModelHelper
from models.cmsmodels import CMSPermission
from functools import reduce
from models.commonmodels import BannerModel

bp = Blueprint('cms',__name__,subdomain='cms')


@bp.route('/')
@login_required
def index():
    return flask.render_template('cms/cms_index.html')

class CMSLoginView(MethodView):

    def get(self,message=None):
        return flask.render_template('cms/login.html',message=message)

    def post(self):
        form = CMSLoginForm(flask.request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            remember = form.remember.data
            user = CMSUser.query.filter_by(email=email).first()
            if user and user.check_password(password):
                # 判断当前用户是否被拉黑，如果被拉黑，跳转到没有权限的提示页面
                if not user.is_active:
                    return flask.abort(401)
                # session
                flask.session[constants.CMS_SESSION_ID] = user.id
                if remember:
                    flask.session.permanent = True
                else:
                    flask.session.permanent = False
                return flask.redirect(flask.url_for('cms.index'))
            else:
                return self.get(message=u'邮箱或密码错误！')
        else:
            message = form.get_error()
            return self.get(message=message)

bp.add_url_rule('/login/',view_func=CMSLoginView.as_view('login'))

@bp.route('/logout/')
@login_required
def logout():
    flask.session.pop(constants.CMS_SESSION_ID)
    return flask.redirect(flask.url_for('cms.login'))

@bp.route('/profile/')
@login_required
def profile():
    return flask.render_template('cms/cms_profile.html')

@bp.route('/resetpwd/',methods=['GET','POST'])
@login_required
def resetpwd():
    if flask.request.method == 'GET':
        return flask.render_template('cms/cms_resetpwd.html')
    else:
        form = CMSResetpwdForm(flask.request.form)
        if form.validate():
            oldpwd = form.oldpwd.data
            newpwd = form.newpwd.data
            if flask.g.cms_user.check_password(oldpwd):
                flask.g.cms_user.password = newpwd
                db.session.commit()
                return xtjson.json_result()
            else:
                return xtjson.json_params_error(u'密码错误！')
        else:
            message = form.get_error()
            return xtjson.json_params_error(message)

@bp.route('/resetmail/',methods=['GET','POST'])
@login_required
def resetmail():
    if flask.request.method == 'GET':
        return flask.render_template('cms/cms_resetmail.html')
    else:
        form = CMSResetmailForm(flask.request.form)
        if form.validate():
            email = form.email.data
            if flask.g.cms_user.email == email:
                return xtjson.json_params_error(message=u'新邮箱与老邮箱一致，无需修改！')
            flask.g.cms_user.email = email
            db.session.commit()
            return xtjson.json_result()
        else:
            return xtjson.json_params_error(message=form.get_error())

@bp.route('/mail_captcha/')
def mail_captcha():
    # /mail_captcha/xxx@qq.com/
    # /mail_captcha/?email=xxx@qq.com
    email = flask.request.args.get('email')

    if xtcache.get(email):
        return xtjson.json_params_error(u'该邮箱已经发送验证码了！')

    source = list(string.ascii_letters)
    for x in range(0,10):
        source.append(str(x))
    captcha_list = random.sample(source,4)
    captcha = ''.join(captcha_list)


    if xtmail.send_mail(subject=u'知了课堂Python学院邮件验证码',receivers=email,body=u'邮箱验证码是：'+captcha):
        # 1. 为了下次可以验证邮箱和验证码
        # 2. 为了防止用户不断的刷这个接口
        xtcache.set(email, captcha)
        return xtjson.json_result()
    else:
        return xtjson.json_server_error()

@bp.route('/cmsroles/')
@login_required
@superadmin_required
def cmsroles():
    roles = CMSRole.query.all()
    return flask.render_template('cms/cms_roles.html',roles=roles)

@bp.route('/add_role/',methods=['GET','POST'])
@login_required
@superadmin_required
def add_role():
    if flask.request.method == 'GET':
        permissions = CMSPermission.PERMISSION_MAP
        return flask.render_template('cms/cms_addrole.html',permissions=permissions)
    else:
        name = flask.request.form.get('name')
        desc = flask.request.form.get('desc')
        permissions = flask.request.form.getlist('permissions[]')
        all_permission = 0
        for x in permissions:
            all_permission |= int(x)
        role = CMSRole(name=name,desc=desc,permissions=all_permission)
        db.session.add(role)
        db.session.commit()
        return xtjson.json_result()

@bp.route('/delete_role/',methods=['POST'])
@login_required
@superadmin_required
def delete_role():
    role_id = flask.request.form.get('role_id')
    role = CMSRole.query.filter_by(id=role_id).first()
    if role.users:
        return xtjson.json_params_error(message=u'该分组下有多位用户，不能删除！')
    else:
        db.session.delete(role)
        db.session.commit()
        return xtjson.json_result()

@bp.route('/edit_role/',methods=['POST','GET'])
@login_required
@superadmin_required
def edit_role():
    if flask.request.method == 'GET':
        role_id = flask.request.args.get('role_id')
        role = CMSRole.query.filter_by(id=role_id).first()
        permissions = CMSPermission.PERMISSION_MAP
        context = {
            'role': role,
            'permissions': permissions
        }
        return flask.render_template('cms/cms_addrole.html',**context)
    else:
        role_id = flask.request.form.get('role_id')
        name = flask.request.form.get('name')
        desc = flask.request.form.get('desc')
        permissions = flask.request.form.get('permissions[]')
        role = CMSRole.query.filter_by(id=role_id).first()
        role.name = name
        role.desc = desc
        role.permissions = reduce(lambda x,y:int(x)|int(y),permissions)
        db.session.commit()
        return xtjson.json_result()

@bp.route('/banners/')
@login_required
def banners():
    banners = BannerModel.query.all()
    context = {
        'banners': banners
    }
    return flask.render_template('')


@bp.route('/cmsusers/')
@login_required
def cmsusers():
    users = CMSUser.query.all()
    context = {
        'users': users
    }
    return flask.render_template('cms/cms_cmsusers.html',**context)

@bp.route('/add_cmsuser/',methods=['GET','POST'])
@login_required
def add_cmsuser():
    if flask.request.method == 'GET':
        roles = CMSRole.query.all()
        context = {
            'roles': roles
        }
        return flask.render_template('cms/cms_addcmsuser.html',**context)
    else:
        form = CMSAddUserForm(flask.request.form)
        if form.validate():
            email = form.email.data
            username = form.username.data
            password = form.password.data
            roles = flask.request.form.getlist('roles[]')
            if not roles:
                return xtjson.json_params_error(message=u'必须指定最少一个分组！')
            user = CMSUser(email=email,username=username,password=password)
            for role_id in roles:
                role = CMSRole.query.get(role_id)
                role.users.append(user)
                # 如果是通过user.roles.append(role)
                # 那么还需要通过db.session.add(user)添加用户到session中
                # 这是因为user还没有添加到数据库中
            db.session.commit()
            return xtjson.json_result()
        else:
            return xtjson.json_params_error(message=form.get_error())

@bp.route('/edit_cmsuser/',methods=['GET','POST'])
@login_required
@superadmin_required
def edit_cmsuser():
    # /edit_cmsuser/?user_id=xxx
    # /edit_cmsuser/xxx/
    if flask.request.method == 'GET':
        user_id = flask.request.args.get('user_id')
        if not user_id:
            flask.abort(404)
        user = CMSUser.query.get(user_id)
        roles = CMSRole.query.all()
        current_roles = [role.id for role in user.roles]
        context = {
            'user': user,
            'roles': roles,
            'current_roles': current_roles# 存储当前用户所有的角色id
        }
        return flask.render_template('cms/cms_editcmsuser.html',**context)
    else:
        user_id = flask.request.form.get('user_id')
        roles = flask.request.form.getlist('roles[]')
        if not user_id:
            return xtjson.json_params_error(message=u'没有指定id！')
        if not roles:
            return xtjson.json_params_error(message=u'必须指定一个组！')

        user = CMSUser.query.get(user_id)
        # 清掉之前的角色信息
        user.roles[:] = []
        # 添加新的角色
        for role_id in roles:
            role_model = CMSRole.query.get(role_id)
            user.roles.append(role_model)
        db.session.commit()
        return xtjson.json_result()

@bp.route('/black_list/',methods=['POST'])
@login_required
@superadmin_required
def black_list():
    form = CMSBlackListForm(flask.request.form)
    if form.validate():
        user_id = form.user_id.data
        if user_id == flask.g.cms_user.id:
            return xtjson.json_params_error(message=u'不能拉黑自己！')
        is_black = form.is_black.data
        user = CMSUser.query.get(user_id)
        user.is_active = not is_black
        db.session.commit()
        return xtjson.json_result()
    else:
        return xtjson.json_params_error(message=form.get_error())

@bp.route('/front_users/')
@login_required
def front_users():
    sort = flask.request.args.get('sort')
    # 1:  按加入时间排序
    # 2： 按发表帖子数量排序
    # 3： 按评论数量排序
    front_users = None
    # 如果没有sort，默认按时间排序
    if not sort or sort == '1':
        front_users = FrontUser.query.order_by(FrontUser.join_time.desc()).all()
    else:
        front_users = FrontUser.query.all()
    context = {
        'front_users': front_users,
        'current_sort': sort
    }
    return flask.render_template('cms/cms_frontusers.html',**context)

@bp.route('/edit_frontuser/')
@login_required
def edit_frontuser():
    user_id = flask.request.args.get('id')
    if not user_id:
        flask.abort(404)

    user = FrontUser.query.get(user_id)
    if not user:
        flask.abort(404)

    return flask.render_template('cms/cms_editfrontuser.html',current_user=user)

@bp.route('/black_front_user/',methods=['POST'])
def black_front_user():
    form = CMSBlackFrontUserForm(flask.request.form)
    if form.validate():
        user_id = form.user_id.data
        is_black =form.is_black.data
        user = FrontUser.query.get(user_id)
        if not user:
            flask.abort(404)

        user.is_active = not is_black
        db.session.commit()
        return xtjson.json_result()
    else:
        return xtjson.json_params_error(message=form.get_error())

@bp.route('/boards/')
@login_required
def boards():
    all_boards = BoardModel.query.all()
    context = {
        'boards':all_boards
    }
    return flask.render_template('cms/cms_boards.html',**context)

@bp.route('/add_board/',methods=['POST'])
@login_required
def add_board():
    name = flask.request.form.get('name')
    # 判断是否有name这个参数
    if not name:
        return xtjson.json_params_error(message=u'必须指定板块的名称！')

    # 2. 判断这个名字在数据库中是否存在
    board = BoardModel.query.filter_by(name=name).first()
    if board:
        return xtjson.json_params_error(message=u'该板块已经存在，不能重复添加！')

    # 3. 创建板块模型
    board = BoardModel(name=name)
    board.author = flask.g.cms_user
    db.session.add(board)
    db.session.commit()
    return xtjson.json_result()

@bp.route('/edit_board/',methods=['POST'])
@login_required
def edit_board():
    form = CMSEditBoardForm(flask.request.form)
    if form.validate():
        board_id = form.board_id.data
        name = form.name.data
        board = BoardModel.query.get(board_id)
        board.name = name
        db.session.commit()
        return xtjson.json_result()
    else:
        return xtjson.json_params_error(message=form.get_error())

@bp.route('/delete_board/',methods=['POST'])
@login_required
def delete_board():
    board_id = flask.request.form.get('board_id')
    if not board_id:
        return xtjson.json_params_error(message=u'没有指定板块id！')

    board = BoardModel.query.filter_by(id=board_id).first()
    if not board:
        return xtjson.json_params_error(message=u'该板块不存在，删除失败！')

    # 判断这个板块下的帖子数是否大于0，如果大于0就不让删除
    # if board.posts.count() > 0:
    #     return xtjson.json_params_error(message=u'该板块下的帖子数大于0，不能删除！')
    db.session.delete(board)
    db.session.commit()
    return xtjson.json_result()

@bp.route('/posts/')
@login_required
def posts():
    # 查询字符串的形式
    sort_type = flask.request.args.get('sort',1,type=int)
    board_id = flask.request.args.get('board',0,type=int)
    page = flask.request.args.get('page',1,type=int)

    context = PostModelHelper.post_list(page,sort_type,board_id)
    return flask.render_template('cms/cms_posts.html',**context)

@bp.route('/highlight/',methods=['POST'])
def highlight():
    form = CMSHightlightPostForm(flask.request.form)
    if form.validate():
        post_id = form.post_id.data
        is_hightlight = form.is_highlight.data
        post_model = PostModel.query.get(post_id)
        if is_hightlight:
            if post_model.highlight:
                return xtjson.json_params_error(message=u'该帖子已经加精！')
            highlight_model = HighlightPostModel()
            post_model.highlight = highlight_model
            db.session.commit()
            return xtjson.json_result()
        else:
            if not post_model.highlight:
                return xtjson.json_params_error(message=u'该帖子没有加精！')
            db.session.delete(post_model.highlight)
            db.session.commit()
            return xtjson.json_result()
    else:
        return xtjson.json_params_error(message=form.get_error())

@bp.route('/remove_post/',methods=['POST'])
def remove_post():
    post_id = flask.request.form.get('post_id')
    if not post_id:
        return xtjson.json_params_error(message=u'必须输入帖子id！')
    post_model = PostModel.query.get(post_id)
    post_model.is_removed = True
    db.session.commit()
    return xtjson.json_result()

@bp.context_processor
def cms_context_processor():
    id = flask.session.get(constants.CMS_SESSION_ID)
    if id:
        user = CMSUser.query.get(id)
        return {'cms_user':user}
    else:
        return {}

@bp.before_request
def cms_before_request():
    id = flask.session.get(constants.CMS_SESSION_ID)
    if id:
        user = CMSUser.query.get(id)
        flask.g.cms_user = user

@bp.errorhandler(404)
def cms_not_found(error):
    if flask.request.is_xhr:
        return xtjson.json_params_error()
    else:
        return flask.render_template('cms/cms_404.html'),404

@bp.errorhandler(401)
def cms_auth_forbidden(error):
    if flask.request.is_xhr:
        return xtjson.json_unauth_error()
    else:
        return flask.render_template('cms/cms_401.html'),401
