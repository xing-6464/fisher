from flask import Blueprint

# 创建蓝图
web = Blueprint('web', __name__)

from app.web import book
from app.web import user
