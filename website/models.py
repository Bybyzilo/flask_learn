from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Colum(db.Integer, primary_key=True)
    data = db.Colum(db.String(10000))
    date = db.Colum(db.DateTime(timezone=True), default=func.now())
    user_id = db.Colum(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Colum(db.Integeer, primary_key=True)
    email = db.Colum(db.String(150), unic=True)
    password = db.Colum(db.String(150))
    first_name = db.Colun(db.String(150))
    notes = db.relationship('Note')