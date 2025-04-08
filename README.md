# 1. 进入你的项目目录（你已经做了）
cd D:\左坤20250219\ai_work\hr_management_system

# 2. 创建虚拟环境（你已经做了）
python -m venv venv

# 3. 激活虚拟环境（Windows PowerShell）
.\venv\Scripts\Activate

# 4. 安装依赖（等我发 requirements.txt 和后端代码给你）
pip install -r requirements.txt

# 5. 启动项目（等我发 run.py 给你）
python run.py


```
hr_management_system/
│
├── .gitignore                   # Git 提交时排除文件清单（如 venv, __pycache__）
├── LICENSE                      # 开源协议（可写 MIT / GPL 等）
├── README.md                    # 项目介绍说明文件
│
├── backend/                     # 后端目录（Flask 应用）
│   ├── README.md                # 后端说明文档（可写接口文档说明）
│   ├── requirements.txt         # Python 项目依赖
│   ├── run.py                   # 项目启动文件（初始化 App + 注册蓝图）
│   │
│   ├── app/                     # 主 Flask 应用目录
│   │   ├── __init__.py          # 初始化 Flask App 实例
│   │   ├── config.py            # Flask 配置文件（数据库地址、密钥等）
│   │   ├── extensions.py        # 初始化扩展（SQLAlchemy、JWT、Migrate）
│   │   │
│   │   ├── models/              # 数据库模型目录（SQLAlchemy ORM 模型）
│   │   │   ├── __init__.py
│   │   │   ├── user.py          # 用户模型（业务员/高管/资料员）
│   │   │   ├── employee.py      # 劳务人员模型
│   │   │   ├── assignment.py    # 分配记录（去往哪个公司）
│   │   │   ├── document.py      # 上传资料模型
│   │   │   ├── salary.py        # 薪资记录模型
│   │   │   └── company.py       # 外派公司模型（如百色、签文）
│   │   │
│   │   ├── schemas/             # Marshmallow 序列化验证（对应 models）
│   │   │   ├── user_schema.py
│   │   │   ├── employee_schema.py
│   │   │   ├── assignment_schema.py
│   │   │   ├── document_schema.py
│   │   │   ├── salary_schema.py
│   │   │   └── company_schema.py
│   │   │
│   │   ├── services/            # 业务逻辑处理
│   │   │   ├── auth_service.py
│   │   │   ├── employee_service.py
│   │   │   ├── document_service.py
│   │   │   ├── salary_service.py
│   │   │   └── upload_service.py   # 文件命名、路径、保存逻辑
│   │   │
│   │   ├── routes/              # API 路由模块（蓝图）
│   │   │   ├── auth.py
│   │   │   ├── employee.py
│   │   │   ├── assignment.py
│   │   │   ├── document.py
│   │   │   ├── salary.py
│   │   │   └── dashboard.py     # 大屏显示相关接口
│   │   │
│   │   ├── tasks/               # 后台定时任务（可配 APScheduler 或 Celery）
│   │   │   └── overdue_check.py # 自动检测证件到期、发送通知
│   │   │
│   │   ├── utils/               # 通用工具模块
│   │   │   ├── permissions.py   # 权限判断装饰器，如 @requires_role()
│   │   │   └── file_utils.py    # 文件大小限制、重命名、清洗等
│   │   │
│   │   └── static/uploads/      # 资料上传文件存放位置（证件/照片等）
│   │
│   ├── migrations/              # Alembic 数据迁移记录（初始化数据库结构）
│   └── tests/                   # 后端测试（pytest 或 unittest）
│       ├── test_employee.py
│       ├── test_auth.py
│       └── test_upload.py
│
├── frontend/
│   ├── README.md                # 前端说明
│   └── client/                  # 前端 React 应用
│       ├── .env.development     # 开发环境变量（API 地址等）
│       ├── .env.production      # 生产环境变量
│       ├── package.json         # React 项目依赖
│       ├── public/              # 公共静态资源（index.html）
│       ├── src/
│       │   ├── index.js         # 入口文件
│       │   ├── App.js           # 应用根组件
│       │   ├── assets/          # 样式、图片等
│       │   ├── components/      # UI组件库（功能模块）
│       │   │   ├── auth/        # 登录/注册表单
│       │   │   ├── employee/    # 劳务人员列表、表单、详情
│       │   │   ├── assignment/  # 分配信息组件
│       │   │   ├── document/    # 上传组件、资料展示
│       │   │   ├── dashboard/   # 大屏可视化组件（图表、卡片、视图切换）
│       │   │   └── common/      # 通用组件（Table, Modal, Button）
│       │   ├── pages/           # 页面级组件（路由对应页面）
│       │   │   ├── LoginPage.jsx
│       │   │   ├── DashboardPage.jsx
│       │   │   ├── UploadPage.jsx
│       │   │   └── EmployeePage.jsx
│       │   ├── store/           # 状态管理（Redux 或 Zustand）
│       │   │   ├── index.js
│       │   │   ├── actions/
│       │   │   ├── reducers/
│       │   │   └── selectors/
│       │   ├── hooks/           # 自定义 hooks，如 useAuth、useUpload
│       │   ├── utils/           # 工具函数（封装请求、数据格式化）
│       │   └── services/        # axios 封装 API 调用（如 employeeService.js）
│       └── tests/               # 前端测试（Jest + React Testing Library）
│           ├── Employee.test.js
│           └── Upload.test.js
│
├── docker-compose.yml           # （可选）Docker 一键启动配置
└── .env                         # 项目根环境变量配置
```