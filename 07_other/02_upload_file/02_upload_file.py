from flask import Flask,request,render_template
import os
from werkzeug.utils import secure_filename
from flask import send_from_directory
from forms import UploadForm
from werkzeug.datastructures import CombinedMultiDict

app = Flask(__name__)

UPLOAD_PATH = os.path.join(os.path.dirname(__file__),'images')


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/upload/',methods=['GET','POST'])
def upload():
    if request.method == 'GET':
        return render_template('upload.html')
    else:
        form = UploadForm(CombinedMultiDict([request.form,request.files]))
        if form.validate():
            # 获取描述信息
            # desc = request.form.get("desc")
            # avatar = request.files.get("avatar")
            desc = form.desc.data
            avatar = form.avatar.data
            filename = secure_filename(avatar.filename)
            avatar.save(os.path.join(UPLOAD_PATH,filename))
            print(desc)
            return '文件上传成功'
        else:
            print(form.errors)
            return "fail"

@app.route('/images/<filename>/')
def get_image(filename):
    return send_from_directory(UPLOAD_PATH,filename)


if __name__ == '__main__':
    app.run(debug=True)
