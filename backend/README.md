├── backend/                     
# 后端目录（Flask 应用）
│   ├── README.md                
# 后端说明文档（可写接口文档说明）
│   ├── requirements.txt         
# Python 项目依赖
│   ├── run.py                   
# 项目启动文件（初始化 App + 注册蓝图）
│   │
│   ├── app/                     
# 主 Flask 应用目录
│   │   ├── __init__.py          
# 初始化 Flask App 实例
│   │   ├── config.py            
# Flask 配置文件（数据库地址、密钥等）
│   │   ├── extensions.py        
# 初始化扩展（SQLAlchemy、JWT、Migrate）
│   │   │
│   │   ├── models/              
# 数据库模型目录（SQLAlchemy ORM 模型）
│   │   │   ├── __init__.py
│   │   │   ├── user.py          
# 用户模型（业务员/高管/资料员）
│   │   │   ├── employee.py      
# 劳务人员模型
│   │   │   ├── assignment.py    
# 分配记录（去往哪个公司）
│   │   │   ├── document.py      
# 上传资料模型
│   │   │   ├── salary.py        
# 薪资记录模型
│   │   │   └── company.py       
# 外派公司模型（如百色、签文）
│   │   │
│   │   ├── schemas/             
# Marshmallow 序列化验证（对应 models）
│   │   │   ├── user_schema.py
│   │   │   ├── employee_schema.py
│   │   │   ├── assignment_schema.py
│   │   │   ├── document_schema.py
│   │   │   ├── salary_schema.py
│   │   │   └── company_schema.py
│   │   │
│   │   ├── services/            
# 业务逻辑处理
│   │   │   ├── auth_service.py
│   │   │   ├── employee_service.py
│   │   │   ├── document_service.py
│   │   │   ├── salary_service.py
│   │   │   └── upload_service.py   
# 文件命名、路径、保存逻辑
│   │   │
│   │   ├── routes/              
# API 路由模块（蓝图）
│   │   │   ├── auth.py
│   │   │   ├── employee.py
│   │   │   ├── assignment.py
│   │   │   ├── document.py
│   │   │   ├── salary.py
│   │   │   └── dashboard.py     
# 大屏显示相关接口
│   │   │
│   │   ├── tasks/               
# 后台定时任务（可配 APScheduler 或 Celery）
│   │   │   └── overdue_check.py 
# 自动检测证件到期、发送通知
│   │   │
│   │   ├── utils/               
# 通用工具模块
│   │   │   ├── permissions.py   
# 权限判断装饰器，如 @requires_role()
│   │   │   └── file_utils.py    
# 文件大小限制、重命名、清洗等
│   │   │
│   │   └── static/uploads/      
# 资料上传文件存放位置（证件/照片等）
│   │
│   ├── migrations/              
# Alembic 数据迁移记录（初始化数据库结构）
│   └── tests/                   
# 后端测试（pytest 或 unittest）
│       ├── test_employee.py
│       ├── test_auth.py
│       └── test_upload.py