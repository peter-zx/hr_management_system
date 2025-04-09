from app.extensions import db

class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'), nullable=False)
    filename = db.Column(db.String(200), nullable=False)
    file_type = db.Column(db.String(50))  # 例如：身份证、合同等
    upload_time = db.Column(db.DateTime, server_default=db.func.now())

    employee = db.relationship('Employee', backref='documents')
