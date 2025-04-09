from app.extensions import ma
from app.models.employee import Employee

class EmployeeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Employee
        load_instance = True

employee_schema = EmployeeSchema()
employees_schema = EmployeeSchema(many=True)
