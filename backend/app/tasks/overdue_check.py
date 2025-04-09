import datetime
from app.models.employee import Employee
from app.extensions import db
from flask import current_app

def check_overdue_id_cards():
    today = datetime.date.today()
    employees = Employee.query.filter(Employee.id_expiration_date <= today).all()

    overdue_employees = []
    for employee in employees:
        overdue_employees.append({
            "name": employee.name,
            "id_number": employee.id_number,
            "expiration_date": employee.id_expiration_date
        })

    # 如果有到期的员工，可以在此发送邮件、通知等
    if overdue_employees:
        current_app.logger.info(f"Found overdue ID cards: {overdue_employees}")
    
    return overdue_employees
