from app.extensions import ma
from app.models.salary import Salary

class SalarySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Salary
        include_fk = True
        load_instance = True

salary_schema = SalarySchema()
salaries_schema = SalarySchema(many=True)
