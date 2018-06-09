
class InputText(object):

    def __str__(self):
        return '<input type="text" />'

class InputEmail(object):

    def __str__(self):
        return '<input type="mail" />'


class StringField(object):
    def __init__(self,wg,reg):
        self.wg = wg
        self.reg = reg

    def __str__(self):
        return str(self.wg)

    def valid(self,val):
        import re
        return re.match(self.reg,val)

class LoginForm(object):
    xyy = StringField(wg=InputText(),reg='\d+')
    lw = StringField(wg=InputEmail(),reg='\w+')

    def __str__(self,form):
        self.form = "用户发来的所有数据{xyy:'df',lw:'sdf'}"

    def validate(self):
        fields = {'xyy':self.xyy,'lw':self.lw}
        for name,field in fields.items():
            # name是 xyy、。lw
            # field:  StringField(wg=InputText(),reg='\d+') / StringField(wg=InputEmail(),reg='\w+')
             # 'df'
            field.valid(self.form[name])


#
# wp = LoginForm()
# print(wp.xyy)
# print(wp.lw)

wp = LoginForm(formdata=request.form)
wp.validate()
