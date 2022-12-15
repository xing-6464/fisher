from flask import Flask

def create_app():
    app = Flask(__name__) # flask对象
    app.config.from_object('config') # 导入配置文件
    register_blueprint(app) # app上注册蓝图
    
    return app

def register_blueprint(app):
    from app.web.book import web
    # 把蓝图注册到app对象上
    app.register_blueprint(web)
