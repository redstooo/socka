from db import db

class ReactionModel(db.Model):
    __tablename__ = "reactions"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000), unique=True, nullable=False)
    formula = db.Column(db.String(1000), unique=True, nullable=False)
    smiles = db.Column(db.String(256), unique=False, nullable=True)
    desc = db.Column(db.String(2000), unique=False, nullable=True)

    reactant_one_id = db.Column(db.Integer, db.ForeignKey("chemicals.id"), unique=False, nullable=False)
    reactant_two_id = db.Column(db.Integer, db.ForeignKey("chemicals.id"), unique=False, nullable=False)
