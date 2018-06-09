#coding: utf8

from wtforms import StringField,BooleanField,ValidationError,IntegerField
from wtforms.validators import InputRequired,Length,Email,EqualTo
from .baseforms import BaseForm
from utils import xtcache
from models.commonmodels import BoardModel


class CMSLoginForm(BaseForm):
    email = StringField(validators=[InputRequired(message=u'必须输入邮箱！'),Email(message=u'邮箱格式不满足！')])
    password = StringField(validators=[InputRequired(message=u'必须输入密码！'),Length(6,20,message=u'密码长度必须在6-20个字符之间！')])
    remember = BooleanField()


class CMSResetpwdForm(BaseForm):
    oldpwd = StringField(validators=[InputRequired(message=u'必须输入密码！'),Length(6,20)])
    newpwd = StringField(validators=[InputRequired(message=u'必须输入新密码！'),Length(6,20)])
    newpwd_repeat = StringField(validators=[EqualTo('newpwd',message=u'两次密码必须一致！')])

class CMSResetmailForm(BaseForm):
    email = StringField(validators=[InputRequired(message=u'必须输入邮箱！'), Email(message=u'邮箱格式不满足！')])
    captcha = StringField(validators=[InputRequired(message=u'必须输入验证码！')])

    def validate_captcha(self,field):
        email = self.email.data
        captcha = field.data
        captcha_cache = xtcache.get(email)
        if not captcha_cache or captcha_cache.lower() != captcha:
            raise ValidationError(message=u'验证码错误！')
        return True

class CMSAddUserForm(BaseForm):
    email = StringField(validators=[InputRequired(message=u'必须输入邮箱！'), Email(message=u'邮箱格式不满足！')])
    username = StringField(validators=[InputRequired(message=u'必须输入用户名！')])
    password = StringField(validators=[InputRequired(message=u'必须输入密码！'), Length(6, 20, message=u'密码长度必须在6-20个字符之间！')])


class CMSBlackListForm(BaseForm):
    user_id = IntegerField(validators=[InputRequired(message=u'必须传入id！')])
    is_black = IntegerField(validators=[InputRequired(message=u'必须指定是否加入黑名单！')])

class CMSBlackFrontUserForm(BaseForm):
    user_id = StringField(validators=[InputRequired(message=u'必须传入id！')])
    is_black = IntegerField(validators=[InputRequired(message=u'必须指定是否加入黑名单！')])


class CMSEditBoardForm(BaseForm):
    board_id = IntegerField(validators=[InputRequired(message=u'必须输入板块id！')])
    name = StringField(validators=[InputRequired(message=u'必须输入板块名称！')])

    def validate_board_id(self,field):
        board_id = field.data
        board = BoardModel.query.filter_by(id=board_id).first()
        if not board:
            raise ValidationError(message=u'该板块不能存在！')
        return True

    def validate_name(self,field):
        name = field.data
        board = BoardModel.query.filter_by(name=name).first()
        if board:
            raise ValidationError(message=u'该名称已经存在，不能修改！')
        return True


class CMSHightlightPostForm(BaseForm):
    post_id = IntegerField(validators=[InputRequired(message=u'必须传入帖子id！')])
    is_highlight = BooleanField(validators=[InputRequired(message=u'必须输入行为！')])



