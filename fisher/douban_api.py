# 调用豆瓣api
from  https import HTTPS


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
    def search_keyword(cls, keyword, count=15, start=0):
        url = cls.keyword_url.format(keyword, count, start)
        return HTTPS.get(url)

