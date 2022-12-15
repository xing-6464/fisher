from flask import jsonify

from helper import is_isbn_or_key
from yushu_book import YuShuBook
from . import web


@web.route('/book/search/<q>/<page>')
def search(q, page):
    """
        q: 普通关键字 或者 isbn
        page
    """
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)

    # 序列化
    return jsonify(result)
    # return json.dumps(result), 200, { 'content-type': 'application/json' }
    