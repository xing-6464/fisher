from flask import jsonify, request, render_template
import json

from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.view_models.book import BookCollection
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
    books = BookCollection()

    # 参数验证成功
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()

        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q, page)

        books.fill(yushu_book, q)
        return json.dumps(books, default=lambda o: o.__dict__)
    else:
        return jsonify(form.errors)
    # 序列化
    # return json.dumps(result), 200, { 'content-type': 'application/json' }

@web.route('/test')
def test():
    r = {
        'name': '星光',
        'age': 18
    }

    return render_template('test2.html', data=r)
