from flask import Flask
from db_helper import SQLHelper


app = Flask(__name__)

@app.route("/")
def hello():
    result = SQLHelper.fetch_one('select * from xxx',[])
    print(result)
    return "Hello World"

if __name__ == '__main__':
    app.run()