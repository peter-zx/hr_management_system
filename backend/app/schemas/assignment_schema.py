from app.extensions import ma
from app.models.assignment import Assignment

class AssignmentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Assignment
        include_fk = True
        load_instance = True

assignment_schema = AssignmentSchema()
assignments_schema = AssignmentSchema(many=True)
