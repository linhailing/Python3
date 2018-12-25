from flask import Flask
from util import is_isbn_or_key

app = Flask(__name__)
# 加载配置文件
app.config.from_object('config')


@app.route('/hello')
def hello():
    return "hello world"


# 图书搜索
@app.route('/book/search/<q>/<page>')
def search(q,page):
    """
    q 搜索关键字
    page 页码
    """
    isbn_or_key = is_isbn_or_key(q)
    print(isbn_or_key)
    return "search"

app.run(host=app.config['HOST'],debug=app.config['DEBUG'],port=app.config['PORT'])

