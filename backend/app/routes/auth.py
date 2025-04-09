from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.user import User
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(username=data.get("username")).first()
    if user and check_password_hash(user.password_hash, data.get("password")):
        return jsonify({"message": "Login successful", "role": user.role}), 200
    return jsonify({"message": "Invalid credentials"}), 401

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    if User.query.filter_by(username=data.get("username")).first():
        return jsonify({"message": "User already exists"}), 400

    hashed_password = generate_password_hash(data.get("password"))
    user = User(username=data.get("username"), password_hash=hashed_password, role=data.get("role"))
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User created"}), 201
