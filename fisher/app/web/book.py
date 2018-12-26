"""
book 书籍类
"""
from app.libs.util import is_isbn_or_key
from app.spider.douban_api import DOUBANAPI
from flask import jsonify, request
from app.web import web
from app.forms.book import BookSearch


@web.route('/hello')
def hello():
    return "hello world"


# 图书搜索
@web.route('/book/search')
def search():
    """
    q 搜索关键字
    page 页码
    ?q=''&page=1
    """
    # 使用wtforms验证数据
    form = BookSearch(request.args)
    if form.validate():
        q = form.q.data
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            data = DOUBANAPI.search_isbn(q)
        else:
            data = DOUBANAPI.search_keyword(q, page)
        return jsonify(data)
    else:
        return jsonify(form.errors)

