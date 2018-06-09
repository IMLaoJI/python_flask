from . import app

@app.route('/order')
def order():
    return 'order'