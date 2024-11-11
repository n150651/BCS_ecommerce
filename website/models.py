

from sqlalchemy import Column, ForeignKey, Integer, String, Date
from flask_login import UserMixin
from . import db


class Users(db.Model, UserMixin):
    id: int = db.Column(db.Integer, primary_key=True)
    username: str = db.Column(db.String(16), unique=True, nullable=False)
    email: str = db.Column(db.String(50), unique=True, nullable=False)
    dob: Date = db.Column(db.Date, nullable=False)
    gender: str = db.Column(db.String(10), nullable=False)
    password: str = db.Column(db.String(150), nullable=False)
