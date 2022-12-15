from flask import Flask

from helper import is_isbn_or_key

__author__ = '星光'

app = Flask(__name__)
# 导入配置文件
# 配置文件中的变量必须大写，否则读不到
app.config.from_object('config')

@app.route('/book/search/<q>/<page>')
def search(q, page):
    """
        q: 普通关键字 或者 isbn
        page
    """
    isbn_or_key = is_isbn_or_key(q)


app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=9527)
