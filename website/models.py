from . import db
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from flask_login import UserMixin


class Cart(db.Model):
    id = Column(Integer, primary_key=True)
    data = Column(String(1000))
    user_id = Column(Integer, ForeignKey('user.user_id'))


class User(db.Model, UserMixin):
    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(16), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    date_of_birth = Column(Date, nullable=False)
    gender = Column(String(10), nullable=False)
    password = Column(String(150), nullable=False)
    cart = db.relationship('Cart')
