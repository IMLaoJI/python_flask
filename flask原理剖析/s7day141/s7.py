from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    import pymysql
    CONN = pymysql.connect(host='127.0.0.1',
                           port=3306,
                           user='root',
                           password='123',
                           database='pooldb',
                           charset='utf8')

    cursor = CONN.cursor()
    cursor.execute('select * from tb1')
    result = cursor.fetchall()
    cursor.close()

    print(result)

    return "Hello World"

if __name__ == '__main__':
    app.run()