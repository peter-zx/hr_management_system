from functools import wraps
from flask import request, jsonify
from app.models.user import User

# 检查用户是否是管理员
def is_admin(user):
    return user.role == "admin"

# 权限装饰器：仅允许管理员访问
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        user = get_current_user()  # 假设你已经有一个获取当前用户的函数
        if not user or not is_admin(user):
            return jsonify({"message": "Permission denied"}), 403
        return f(*args, **kwargs)
    return decorated_function

# 获取当前登录的用户（示例，需根据你的登录机制修改）
def get_current_user():
    # 假设用户信息保存在 session 中，替换为实际的实现
    username = request.cookies.get("username")
    if username:
        return User.query.filter_by(username=username).first()
    return None
