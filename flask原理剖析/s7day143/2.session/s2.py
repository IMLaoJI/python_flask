from flask import Flask,session


app = Flask(__name__)
app.secret_key = 'suijksdfsd'

#
# from redis import Redis
# from flask_session import RedisSessionInterface
# conn = Redis()
# app.session_interface = RedisSessionInterface(conn,key_prefix='__',use_signer=False,permanent=True)


# from redis import Redis
# from flask.ext.session import Session
# app.config['SESSION_TYPE'] = 'redis'
# app.config['SESSION_REDIS'] = Redis(host='192.168.0.94',port='6379')
# Session(app)



@app.route('/')
def index():
    session['xxx'] = 123
    return 'Index'


if __name__ == '__main__':

    app.run()