"""
Creation of database models, one for users and one for journaling notes
"""

from . import db  # from current package, import db object
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    # allows users to have access to all their notes
    notes = db.relationship("Note")


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    notes = db.Column(db.String(15000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    quote = db.Column(db.String(500))
    quote_author = db.Column(db.String(100))
    quote_category = db.Column(db.String(100))
    # every note has one user associated with it
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
