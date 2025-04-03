from flask import request, jsonify
from flask.views import MethodView
from flask_smorest import Blueprint
from sqlalchemy.exc import IntegrityError

from db import db
from models import ReactionModel, ChemicalModel

blp = Blueprint("Reactions", "reaction", description="Operations on reactions")

from sqlalchemy.orm import class_mapper


def model_to_dict(model):
    """
    Convert an SQLAlchemy model instance to a dictionary.

    :param model: SQLAlchemy model instance
    :return: Dictionary representation of the model
    """
    if not model:
        return None

    return {column.key: getattr(model, column.key) for column in class_mapper(model.__class__).columns}

@blp.route("/reaction")
class GetReactions(MethodView):
    def get(self):
        reactions = ReactionModel.query.all()

        reakcie = []
        for reaction in reactions:
            reakcie.append(model_to_dict(reaction))

        return {"Reactions...":  reakcie}

@blp.route("/reaction")
class GetReactions(MethodView):
    def post(self):

        try:
            reaction_name = request.json["name"]
            reactant_one_name = request.json["reactant_one_name"]
            reactant_two_name = request.json["reactant_two_name"]

            reactant_one = ChemicalModel.query.filter(ChemicalModel.name==reactant_one_name).first()
            reactant_two = ChemicalModel.query.filter(ChemicalModel.name==reactant_two_name).first()



            reaction = ReactionModel()
            reaction.name = reaction_name
            reaction.formula = request.json["formula"]
            reaction.smiles = request.json["smiles"]
            reaction.desc = request.json["desc"]
            reaction.reactant_one_id = reactant_one.id
            reaction.reactant_two_id = reactant_two.id
            db.session.add(reaction)
            db.session.commit()
            return {"Pridané: ": reaction.name}, 201
        except IntegrityError:
            db.session.rollback()
            return {"error": "duplikát"}, 400



@blp.route("/reaction/<string:name>")
class GetChemicals(MethodView):
    def get(self, name):
        reakcia = ReactionModel.query.filter(ReactionModel.name==name).first()

        return {"reakcia": model_to_dict(reakcia)}, 200


@blp.route("/reaction/<int:id>")
class GetChemicals(MethodView):
    def get(self, id):
        reakcia = ReactionModel.query.filter(ReactionModel.id==id).first()

        return {"reakcia": model_to_dict(reakcia)}, 200