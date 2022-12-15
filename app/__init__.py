from flask import Flask

def create_app():
    app = Flask(__name__)
    # 导入配置文件
    # 配置文件中的变量必须大写，否则读不到
    app.config.from_object('config')

    return app
