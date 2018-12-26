"""
user 用户模块
"""
from app.web import web


@web.route('/user/login')
def login():
    print('user login')
    return "user login"

