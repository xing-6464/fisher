from flask import Flask

__author__ = '星光'

app = Flask(__name__)

# @app.route('/hello')
def hello():
    return 'Hello, QiYue'

app.add_url_rule('/hello', view_func=hello)

app.run(debug=True, port=9527)
