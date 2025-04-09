from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.assignment import Assignment
from app.schemas.assignment_schema import assignment_schema, assignments_schema

assignment_bp = Blueprint('assignment', __name__)

@assignment_bp.route("/", methods=["GET"])
def get_all_assignments():
    assignments = Assignment.query.all()
    return jsonify(assignments_schema.dump(assignments))

@assignment_bp.route("/<int:id>", methods=["GET"])
def get_assignment(id):
    assignment = Assignment.query.get_or_404(id)
    return jsonify(assignment_schema.dump(assignment))

@assignment_bp.route("/", methods=["POST"])
def create_assignment():
    data = request.json
    new_assignment = assignment_schema.load(data, session=db.session)
    db.session.add(new_assignment)
    db.session.commit()
    return jsonify(assignment_schema.dump(new_assignment)), 201

@assignment_bp.route("/<int:id>", methods=["DELETE"])
def delete_assignment(id):
    assignment = Assignment.query.get_or_404(id)
    db.session.delete(assignment)
    db.session.commit()
    return jsonify({"message": "Deleted"}), 204
