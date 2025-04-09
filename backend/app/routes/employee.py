from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.employee import Employee
from app.schemas.employee_schema import employee_schema, employees_schema

employee_bp = Blueprint('employee', __name__)

@employee_bp.route("/", methods=["GET"])
def get_all_employees():
    employees = Employee.query.all()
    return jsonify(employees_schema.dump(employees))

@employee_bp.route("/<int:id>", methods=["GET"])
def get_employee(id):
    employee = Employee.query.get_or_404(id)
    return jsonify(employee_schema.dump(employee))

@employee_bp.route("/", methods=["POST"])
def create_employee():
    data = request.json
    new_employee = employee_schema.load(data, session=db.session)
    db.session.add(new_employee)
    db.session.commit()
    return jsonify(employee_schema.dump(new_employee)), 201

@employee_bp.route("/<int:id>", methods=["PUT"])
def update_employee(id):
    employee = Employee.query.get_or_404(id)
    data = request.json
    for key, value in data.items():
        setattr(employee, key, value)
    db.session.commit()
    return jsonify(employee_schema.dump(employee))

@employee_bp.route("/<int:id>", methods=["DELETE"])
def delete_employee(id):
    employee = Employee.query.get_or_404(id)
    db.session.delete(employee)
    db.session.commit()
    return jsonify({"message": "Deleted"}), 204
