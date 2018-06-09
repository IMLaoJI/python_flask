from flask import Flask, views, url_for

app = Flask(import_name=__name__)
app.config['SERVER_NAME'] = 'oldboyedu.com:5000'


@app.route("/", subdomain="admin")
def static_index():
    """Flask supports static subdomains
    This is available at static.your-domain.tld"""
    return "xxxxxx.your-domain.tld"


@app.route("/dynamic", subdomain="<username>")
def username_index(username):
    """Dynamic subdomains are also supported
    Try going to user1.your-domain.tld/dynamic"""
    return username + ".your-domain.tld"


if __name__ == '__main__':
    app.run()