from flask import jsonify, request

from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from . import web


@web.route('/book/search')
def search():
    """
        q: 普通关键字 或者 isbn
        page
        ?q=isbn?page=1
    """
    # 验证层
    form = SearchForm(request.args)
    # 参数验证成功
    if form.validate():

        q = form.q.data.strip()
        page = form.page.data

        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q, page)

        return jsonify(result)
    else:
        return jsonify(form.errors)
    # 序列化
    # return json.dumps(result), 200, { 'content-type': 'application/json' }
    