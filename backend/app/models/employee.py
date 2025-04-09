from app.extensions import db

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    id_number = db.Column(db.String(18), unique=True, nullable=False)
    entry_date = db.Column(db.Date)
    id_expiration_date = db.Column(db.Date)  # 身份证有效期，用于预警
    phone = db.Column(db.String(20))
    gender = db.Column(db.String(10))
    birth_date = db.Column(db.Date)
    address = db.Column(db.String(200))
    bank_account = db.Column(db.String(100))
