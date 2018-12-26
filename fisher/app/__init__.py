"""
统一启动flask
"""
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')
    app.config.from_object('app.secure')
    register_blueprints(app)
    return app


def register_blueprints(app):
    from app.web import web
    app.register_blueprint(web)
