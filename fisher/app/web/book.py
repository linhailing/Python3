"""
book 书籍类
"""
from util import is_isbn_or_key
from douban_api import DOUBANAPI
from flask import jsonify
from app.web import web


@web.route('/hello')
def hello():
    return "hello world"


# 图书搜索
@web.route('/book/search/<q>/<page>')
def search(q, page):
    """
    q 搜索关键字
    page 页码
    """
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        data = DOUBANAPI.search_isbn(q)
    else:
        data = DOUBANAPI.search_keyword(q)
    return jsonify(data)

