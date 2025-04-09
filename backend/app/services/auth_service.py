from app.models.user import User
from werkzeug.security import generate_password_hash, check_password_hash
from app.extensions import db

def register_user(username, password, role):
    if User.query.filter_by(username=username).first():
        raise ValueError("User already exists")
    
    hashed_password = generate_password_hash(password)
    user = User(username=username, password_hash=hashed_password, role=role)
    db.session.add(user)
    db.session.commit()
    return user

def authenticate_user(username, password):
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password_hash, password):
        return user
    return None
