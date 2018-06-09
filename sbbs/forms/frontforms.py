#coding: utf8

from wtforms import StringField,BooleanField,ValidationError,IntegerField
from wtforms.validators import InputRequired,Length,Email,EqualTo,URL
from .baseforms import BaseForm
from utils import xtcache

class GraphCaptchaForm(BaseForm):
    graph_captcha = StringField(validators=[InputRequired(message=u'必须输入图形验证码！')])

    def validate_graph_captcha(self,field):
        graph_captcha = field.data
        cache_captcha = xtcache.get(graph_captcha.lower())
        if not cache_captcha or cache_captcha.lower() != graph_captcha.lower():
            raise ValidationError(message=u'图形验证码错误！')
        return True

class FrontRegistForm(BaseForm):
    telephone = StringField(validators=[InputRequired(message=u'必须输入手机号码！'),Length(11,11,message=u'手机号码格式不对！')])
    sms_captcha = StringField(validators=[InputRequired(message=u'必须输入短信验证码！')])
    username = StringField(validators=[InputRequired(message=u'必须输入用户名！')])
    password = StringField(validators=[InputRequired(message=u'必须输入密码！'), Length(6, 20, message=u'密码长度必须在6-20个字符之间！')])
    password_repeat = StringField(validators=[EqualTo('password')])
    graph_captcha = StringField(validators=[InputRequired(message=u'必须输入图形验证码！')])

    def validate_sms_captcha(self,field):
        sms_captcha = field.data
        telephone = self.telephone.data
        cache_captcha = xtcache.get(telephone)
        if not cache_captcha or cache_captcha.lower() != sms_captcha.lower():
            raise ValidationError(message=u'短信验证码错误!')
        return True

    def validate_graph_captcha(self,field):
        graph_captcha = field.data
        cache_captcha = xtcache.get(graph_captcha.lower())
        if not cache_captcha or cache_captcha.lower() != graph_captcha.lower():
            raise ValidationError(message=u'图形验证码错误！')
        return True

class FrontLoginForm(GraphCaptchaForm):
    telephone = StringField(validators=[InputRequired(message=u'必须输入手机号码！'), Length(11, 11, message=u'手机号码格式不对！')])
    password = StringField(validators=[InputRequired(message=u'必须输入密码！'), Length(6, 20, message=u'密码长度必须在6-20个字符之间！')])
    remember = IntegerField()

class AddPostForm(GraphCaptchaForm):
    title = StringField(validators=[InputRequired(message=u'必须输入标题！')])
    content = StringField(validators=[InputRequired(message=u'必须输入内容！')])
    board_id = IntegerField(validators=[InputRequired(message=u'必须输入板块id！')])

class AddCommentForm(BaseForm):
    post_id = IntegerField(validators=[InputRequired(message=u'必须输入帖子id！')])
    content = StringField(validators=[InputRequired(message=u'必须输入内容！')])
    comment_id = IntegerField()

class StarPostForm(BaseForm):
    post_id = IntegerField(validators=[InputRequired(message=u'必须输入帖子id！')])
    is_star = BooleanField(validators=[InputRequired(message=u'必须输入赞的行为！')])

class SettingsForm(BaseForm):
    username = StringField(validators=[InputRequired(message=u'必须输入用户名！')])
    realname = StringField()
    qq = StringField()
    avatar = StringField(validators=[URL(message=u'头像格式不对！')])
    signature = StringField()
