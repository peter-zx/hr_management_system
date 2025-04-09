from app.models.salary import Salary
from app.extensions import db

def create_salary(employee_id, amount, date_issued, remarks=""):
    salary = Salary(employee_id=employee_id, amount=amount, date_issued=date_issued, remarks=remarks)
    db.session.add(salary)
    db.session.commit()
    return salary

def get_salaries(employee_id=None):
    if employee_id:
        salaries = Salary.query.filter_by(employee_id=employee_id).all()
    else:
        salaries = Salary.query.all()
    return salaries

def delete_salary(salary_id):
    salary = Salary.query.get(salary_id)
    if salary:
        db.session.delete(salary)
        db.session.commit()
        return True
    return False
