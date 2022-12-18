from flask import Flask

from app.models.base import db

def create_app():
    app = Flask(__name__) 
    app.config.from_object('app.secure')
    app.config.from_object('app.setting') 
    register_blueprint(app)
    
    db.init_app(app) 
    with app.app_context():
        db.create_all()
    return app

def register_blueprint(app):
    from app.web.book import web
    # 把蓝图注册到app对象上
    app.register_blueprint(web)
