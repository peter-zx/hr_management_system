from app.models.employee import Employee
from app.extensions import db

def create_employee(data):
    employee = Employee(
        name=data['name'],
        id_number=data['id_number'],
        entry_date=data.get('entry_date'),
        id_expiration_date=data.get('id_expiration_date'),
        phone=data.get('phone'),
        gender=data.get('gender'),
        birth_date=data.get('birth_date'),
        address=data.get('address'),
        bank_account=data.get('bank_account')
    )
    db.session.add(employee)
    db.session.commit()
    return employee

def update_employee(employee_id, data):
    employee = Employee.query.get_or_404(employee_id)
    for key, value in data.items():
        setattr(employee, key, value)
    db.session.commit()
    return employee

def delete_employee(employee_id):
    employee = Employee.query.get_or_404(employee_id)
    db.session.delete(employee)
    db.session.commit()
    return employee
