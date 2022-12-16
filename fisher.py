from app import create_app

__author__ = '星光'

app = create_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=9527, threading=True)
