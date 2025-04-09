from flask import Flask
from .extensions import db, ma, cors
from .config import Config

# 导入蓝图
from .routes.auth import auth_bp
from .routes.employee import employee_bp
from .routes.document import document_bp
from .routes.assignment import assignment_bp
from .routes.salary import salary_bp
from .routes.dashboard import dashboard_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # 初始化扩展
    db.init_app(app)
    ma.init_app(app)
    cors.init_app(app)

    # 注册蓝图
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(employee_bp, url_prefix="/api/employee")
    app.register_blueprint(document_bp, url_prefix="/api/document")
    app.register_blueprint(assignment_bp, url_prefix="/api/assignment")
    app.register_blueprint(salary_bp, url_prefix="/api/salary")
    app.register_blueprint(dashboard_bp, url_prefix="/api/dashboard")

    return app
