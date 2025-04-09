from flask import Blueprint, jsonify
from app.extensions import db
from app.models.employee import Employee
from app.models.assignment import Assignment
from app.models.salary import Salary
from sqlalchemy import func

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route("/summary", methods=["GET"])
def summary():
    total_employees = db.session.query(func.count(Employee.id)).scalar()
    total_assignments = db.session.query(func.count(Assignment.id)).scalar()
    total_salary = db.session.query(func.sum(Salary.amount)).scalar()

    return jsonify({
        "total_employees": total_employees,
        "total_assignments": total_assignments,
        "total_salary": total_salary or 0
    })
