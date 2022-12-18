from flask import Flask
from flask_login import LoginManager

from app.models.base import db
from app.models.user import User

login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

def create_app():
    app = Flask(__name__) 
    app.config.from_object('app.secure')
    app.config.from_object('app.setting') 
    register_blueprint(app)
    
    db.init_app(app) 
    login_manager.init_app(app)
    with app.app_context():
        db.create_all()
    return app

def register_blueprint(app):
    from app.web import web
    # 把蓝图注册到app对象上
    app.register_blueprint(web)
