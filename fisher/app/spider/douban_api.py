# 调用豆瓣api
from app.libs.https import HTTPS
from flask import current_app
from app.libs.util import limit


class DOUBANAPI:
    isbn_url = 'https://api.douban.com/v2/book/isbn/{}'
    keyword_url = 'https://api.douban.com/v2/book/search?q={}&count={}&start={}'

    @classmethod
    def search_isbn(cls, isbn):
        """
        isbn
        :param isbn:
        :return:
        """
        url = cls.isbn_url.format(isbn)
        return HTTPS.get(url)

    @classmethod
    def search_keyword(cls, keyword, page):
        url = cls.keyword_url.format(keyword, current_app.config['PAGESIZE'], limit(current_app.config['PAGESIZE'], page))
        return HTTPS.get(url)

