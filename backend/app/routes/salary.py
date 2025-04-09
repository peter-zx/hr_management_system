from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.salary import Salary
from app.schemas.salary_schema import salary_schema, salaries_schema

salary_bp = Blueprint('salary', __name__)

@salary_bp.route("/", methods=["GET"])
def get_all_salaries():
    salaries = Salary.query.all()
    return jsonify(salaries_schema.dump(salaries))

@salary_bp.route("/<int:id>", methods=["GET"])
def get_salary(id):
    salary = Salary.query.get_or_404(id)
    return jsonify(salary_schema.dump(salary))

@salary_bp.route("/", methods=["POST"])
def create_salary():
    data = request.json
    new_salary = salary_schema.load(data, session=db.session)
    db.session.add(new_salary)
    db.session.commit()
    return jsonify(salary_schema.dump(new_salary)), 201

@salary_bp.route("/<int:id>", methods=["DELETE"])
def delete_salary(id):
    salary = Salary.query.get_or_404(id)
    db.session.delete(salary)
    db.session.commit()
    return jsonify({"message": "Deleted"}), 204
