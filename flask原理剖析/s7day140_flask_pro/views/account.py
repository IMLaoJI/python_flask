from . import app

@app.route('/acc/login')
def login():
    return 'login'



@app.route('/acc/logout')
def logout():
    return 'logout'