from app.extensions import db

class Salary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date_issued = db.Column(db.Date, nullable=False)
    remarks = db.Column(db.String(200))

    employee = db.relationship('Employee', backref='salaries')
