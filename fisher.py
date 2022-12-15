from flask import Flask, make_response

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
    # isbn isbn13 13个0到9的数字组成
    # isbn10 10个0到9数字组成，含有一些‘ - ’
    isbn_or_key = 'key'
    # 判断isbn13
    if len(q) == 13 and q.isdigit():
        isbn_or_key = 'isbn'
    
    short_q = q.replace('-', '')
    # 判断isbn10
    if '-' in q and short_q == 10 and short_q.isdigit():
        isbn_or_key = 'isbn'
    pass


app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=9527)
