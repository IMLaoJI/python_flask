#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask, render_template, request, redirect
from wtforms import Form
from wtforms.fields import simple
from wtforms import validators
from wtforms import widgets

app = Flask(__name__, template_folder='templates')

app.debug = True


# 1.由于 metaclass=FormMeta，所以LoginForm是由FormMeta创建
# 2. 执行 FormMeta.__init__
#       LoginForm._unbound_fields = None
#       LoginForm._wtforms_meta = None
# 3. 解释字段：
#       name = simple.StringField(...)
#       pwd = simple.PasswordField(...)
#    结果：
#       LoginForm.name = UnboundField(simple.StringField,StringField的所有参数)
#       LoginForm.pwd = UnboundField(simple.PasswordField,PasswordField的所有参数)

class LoginForm(Form):
    # 字段（内部包含正则表达式）
    name = simple.StringField(
        label='用户名',
        validators=[
            validators.DataRequired(message='用户名不能为空.'),
            validators.Length(min=6, max=18, message='用户名长度必须大于%(min)d且小于%(max)d')
        ],
        widget=widgets.TextInput(), # 页面上显示的插件
        render_kw={'class': 'form-control'}
    )
    # 字段（内部包含正则表达式）
    pwd = simple.PasswordField(
        label='密码',
        validators=[
            validators.DataRequired(message='密码不能为空.'),
            validators.Length(min=8, message='用户名长度必须大于%(min)d'),
            validators.Regexp(regex="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,}",
                              message='密码至少8个字符，至少1个大写字母，1个小写字母，1个数字和1个特殊字符')

        ],
        widget=widgets.PasswordInput(),
        render_kw={'class': 'form-control'}
    )
    def validate_name(self,form):
        pass

"""
print(LoginForm.__dict__)
LoginForm ={
	'__module__': '__main__', 
	'name': <1 UnboundField(StringField, (), {'label': '用户名', 'validators': [<wtforms.validators.DataRequired object at 0x00000000037DAEB8>, <wtforms.validators.Length object at 0x000000000382B048>], 'widget': <wtforms.widgets.core.TextInput object at 0x000000000382B080>, 'render_kw': {'class': 'form-control'}})>, 
	'pwd': <2 UnboundField(PasswordField, (), {'label': '密码', 'validators': [<wtforms.validators.DataRequired object at 0x000000000382B0F0>, <wtforms.validators.Length object at 0x000000000382B128>, <wtforms.validators.Regexp object at 0x000000000382B160>], 'widget': <wtforms.widgets.core.PasswordInput object at 0x000000000382B208>, 'render_kw': {'class': 'form-control'}})>, 
	'__doc__': None, 
	'_unbound_fields': None, 
	'_wtforms_meta': None
}
"""

@app.route('/login', methods=['GET', 'POST'])
def login():
    # 实例LoginForm
    # 1. 执行FormMeta的__call__方法
    """
        class Meta(DefaultMeta,):
            pass

        LoginForm ={
            '__module__': '__main__',
            'name': <2 UnboundField(StringField, (), {'label': '用户名', 'validators': [<wtforms.validators.DataRequired object at 0x00000000037DAEB8>, <wtforms.validators.Length object at 0x000000000382B048>], 'widget': <wtforms.widgets.core.TextInput object at 0x000000000382B080>, 'render_kw': {'class': 'form-control'}})>,
            'pwd': <1 UnboundField(PasswordField, (), {'label': '密码', 'validators': [<wtforms.validators.DataRequired object at 0x000000000382B0F0>, <wtforms.validators.Length object at 0x000000000382B128>, <wtforms.validators.Regexp object at 0x000000000382B160>], 'widget': <wtforms.widgets.core.PasswordInput object at 0x000000000382B208>, 'render_kw': {'class': 'form-control'}})>,
            '__doc__': None,
            '_unbound_fields': [
                (name, UnboundField对象（1，simple.StringField，参数）)，
                (pwd, UnboundField对象（2，simple.PasswordField，参数）)，
            ],
            '_wtforms_meta': Meta

    }
    """
    # 2. 执行LoginForm的__new__方法
    #    pass
    # 3. 执行LoginForm的__init__方法
    """
     LoginForm ={
            '__module__': '__main__',
            'name': <2 UnboundField(StringField, (), {'label': '用户名', 'validators': [<wtforms.validators.DataRequired object at 0x00000000037DAEB8>, <wtforms.validators.Length object at 0x000000000382B048>], 'widget': <wtforms.widgets.core.TextInput object at 0x000000000382B080>, 'render_kw': {'class': 'form-control'}})>,
            'pwd': <1 UnboundField(PasswordField, (), {'label': '密码', 'validators': [<wtforms.validators.DataRequired object at 0x000000000382B0F0>, <wtforms.validators.Length object at 0x000000000382B128>, <wtforms.validators.Regexp object at 0x000000000382B160>], 'widget': <wtforms.widgets.core.PasswordInput object at 0x000000000382B208>, 'render_kw': {'class': 'form-control'}})>,
            '__doc__': None,
            '_unbound_fields': [
                (name, UnboundField对象（1，simple.StringField，参数）)，
                (pwd, UnboundField对象（2，simple.PasswordField，参数）)，
            ],
            '_wtforms_meta': Meta

        }
    form = {
        _fields: {
                name: StringField对象(),
                pwd: PasswordField对象(),
            }
        name:  StringField对象(widget=widgets.TextInput()),
        pwd:  PasswordField对象(widget=widgets.PasswordInput())
    
        }
    
    """
    if request.method == 'GET':

        form = LoginForm()
        # form._fields['name']
        # form.name = StringField对象()
        """
        1. StringField对象.__str__
        2. StringField对象.__call__
        3. meta.render_field(StringField对象,)
        4. StringField对象.widget(field, **render_kw)
        5. 插件.__call__()
        """
        print(form.name) #
        """
        0. Form.__iter__: 返回所有字段对象
            1. StringField对象.__str__
            2. StringField对象.__call__
            3. meta.render_field(StringField对象,)
            4. StringField对象.widget(field, **render_kw)
            5. 插件.__call__()
        """
        for item in form:
            # item是fields中的每一个字段
            print(item)

        return render_template('login.html',form=form)
    else:
        # 上述流程+
        # 从请求中获取每个值，再复制到到每个字段对象中
        """
         form = {
            _fields: {
                    name: StringField对象(data=你输入的用户名),
                    pwd: PasswordField对象(pwd=你输入的密码),
                }
            name:  StringField对象(widget=widgets.TextInput(data=你输入的用户名)),
            pwd:  PasswordField对象(widget=widgets.PasswordInput(pwd=你输入的密码))
        
            }
        """
        # 请求发过来的值
        form = LoginForm(formdata=request.form) # 值.getlist('name')

        # 实例：编辑
        # # 从数据库对象
        # form = LoginForm(obj='值') # 值.name/值.pwd
        #
        # # 字典 {}
        # form = LoginForm(data=request.form) # 值['name']

        # 1. 循环所有的字段
        # 2. 获取每个字段的钩子函数
        # 3. 为每个字段执行他的验证流程 字段.validate(钩子函数+内置验证规则)
        if form.validate():
            print(form.data)
        else:
            print(form.errors)


if __name__ == '__main__':
    app.run()