from . import app

@app.route('/user')
def user():
    return 'user'