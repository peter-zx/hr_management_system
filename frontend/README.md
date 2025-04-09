# 前端 - 人力资源管理系统

这是使用 React 构建的前端部分，配合后端 Flask 服务进行数据交互。功能包括员工信息管理、文件上传、仪表盘展示等。

## 项目结构

- `client/`：React 应用主目录
  - 使用 [Create React App](https://create-react-app.dev/) 搭建
  - 所有源代码位于 `src/` 目录中

## 快速开始

```bash
cd frontend/client
npm install
npm start



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