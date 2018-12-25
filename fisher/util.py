"""
工具类
"""


def is_isbn_or_key(word):
    """
    判断是否为isbn码
    isbn13：是13位数字
    isbn10：是10位数字或中间有"-"
    """
    res = 'key'
    if len(word) == 13 and word.isdigit():
        res = 'isbn'
    shout_word = word.replace('-','')
    if '-' in word and len(shout_word) == 10 and shout_word.isdigit():
        res = 'isbn'
    return res
