from . import db
from flask_login import UserMixin

class user(db.Model, UserMixin):
    Uid = db.Column(db.Integer, primary_key=True)
    Uemail = db.Column(db.String(100), unique=True)
    Fname = db.Column(db.String(100))
    Lname = db.Column(db.String(100))
    Ucountry = db.Column(db.String(100))
