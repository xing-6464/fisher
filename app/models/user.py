from sqlalchemy import Column, Integer, String, Float
from werkzeug.security import generate_password_hash

from app.models.base import Base

class User(Base):
    # __tablename__ = ''

    id = Column(Integer, primary_key=True, autoincrement=True)
    nickname = Column(String(24), nullable=False)
    phone_number = Column(String(18), unique=True)
    _password = Column('password', String(64))
    email = Column(String(50), unique=True, nullable=False)
    confirmed = Column(Float, default=False)
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    receive_cunter = Column(Integer, default=0)
    wx_open_id = Column(String(50))
    wx_name = Column(String(32))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

