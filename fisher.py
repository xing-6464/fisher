from flask import Flask


__author__ = '星光'

app = Flask(__name__)
# 导入配置文件
# 配置文件中的变量必须大写，否则读不到
app.config.from_object('config')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=9527)
