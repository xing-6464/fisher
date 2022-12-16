from flask import Flask

from app.models.book import db

def create_app():
    app = Flask(__name__) # flask对象
    app.config.from_object('app.secure') # 导入配置文件
    app.config.from_object('app.setting') # 导入配置文件
    register_blueprint(app) # app上注册蓝图
    
    db.init_app(app) # 使用插件
    db.create_all()
    return app

def register_blueprint(app):
    from app.web.book import web
    # 把蓝图注册到app对象上
    app.register_blueprint(web)
