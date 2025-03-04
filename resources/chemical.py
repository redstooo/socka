from flask.views import MethodView
from flask import request
from flask_smorest import Blueprint
from sqlalchemy.exc import IntegrityError

from models import ChemicalModel
from db import db
blp = Blueprint("Chemicals", "chemical", description="Operations on chemicals")

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

@blp.route("/chemical")
class GetChemicals(MethodView):
    def get(self):
        chemicals = ChemicalModel.query.all()
        for chemical in chemicals:
            print(chemical.id)
        chemikalie = []
        for chemical in chemicals:
            chemikalie.append(model_to_dict(chemical))
        return {"Chemicals...": chemikalie}

@blp.route("/chemical")
class GetChemicals(MethodView):
    def post(self):
        try:
            chemical = ChemicalModel()
            chemical.name = request.json["name"]
            db.session.add(chemical)
            db.session.commit()
            return {"Pridané: ": chemical.name}, 201
        except IntegrityError:
            db.session.rollback()
            return {"error": "duplikát"}, 400


@blp.route("/chemical/<string:name>")
class GetChemicals(MethodView):
    def get(self, name):
        chemikalia = ChemicalModel.query.filter(ChemicalModel.name==name).first()

        return {"chemikalia": model_to_dict(chemikalia)}, 200


@blp.route("/chemical/<int:id>")
class GetChemicals(MethodView):
    def get(self, id):
        chemikalia = ChemicalModel.query.filter(ChemicalModel.id==id).first()

        return {"chemikalia": model_to_dict(chemikalia)}, 200