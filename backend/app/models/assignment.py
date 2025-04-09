from app.extensions import db

class Assignment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
    assigned_date = db.Column(db.Date, nullable=False)

    employee = db.relationship('Employee', backref='assignments')
    company = db.relationship('Company', backref='assignments')
