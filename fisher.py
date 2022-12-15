from flask import Flask, make_response

__author__ = '星光'

app = Flask(__name__)
# 导入配置文件
# 配置文件中的变量必须大写，否则读不到
app.config.from_object('config')

@app.route('/hello')
def hello():
    # status code 200, 404, 301
    # content-type http headers
    # content-type = text/html
    # Response
    headers = {
        'content-type': 'text/plain'
    }
    # response = make_response('<html></html>', 404)
    # response.headers = headers
    return '<html></html>', 404, headers

app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=9527)
