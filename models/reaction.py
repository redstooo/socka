from enum import unique

from db import db

class ReactionModel(db.Model):
    __tablename__ = "reactions"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    element = db.Column(db.String(256), unique=True, nullable=False)
    state = db.Column(db.String(80), unique=False, nullable=True)
    desc = db.Column(db.String(256), unique=False, nullable=True)

    reactant_one_id = db.Column(db.Integer, db.ForeignKey("chemicals.id"), unique=False, nullable=False)
    reactant_two_id = db.Column(db.Integer, db.ForeignKey("chemicals.id"), unique=False, nullable=False)
