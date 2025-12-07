# 💰 记账本 Web 应用

一款简洁易用的个人财务管理工具，帮助你记录日常收支、分析消费习惯、合理规划预算。

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![React](https://img.shields.io/badge/react-18.2+-61dafb.svg)
![FastAPI](https://img.shields.io/badge/fastapi-0.104+-009688.svg)

## ✨ 功能特性

### 核心功能 (MVP)
- ✅ **用户管理**: 注册、登录、个人信息管理
- ✅ **快速记账**: 支持收入/支出快速录入，带计算器键盘
- ✅ **分类管理**: 预设分类 + 自定义分类，支持图标和颜色
- ✅ **账目查询**: 多条件筛选、分页展示、编辑删除
- ✅ **数据统计**: 收支概览、分类统计、趋势分析、排行榜

### 进阶功能 (V2.0 - 开发中)
- 🚧 **预算管理**: 月度预算设置、执行进度、超支提醒
- 🚧 **多账户管理**: 现金、银行卡、支付宝、微信等
- 🚧 **定期账目**: 自动记账提醒（如房租、工资）
- 🚧 **数据导出**: Excel报表、PDF账单
- 🚧 **数据备份**: 云端备份、导入导出

## 🎨 界面预览

> 开发中，敬请期待...

## 🛠️ 技术栈

### 后端
- **框架**: FastAPI 0.104+
- **数据库**: PostgreSQL 15+ / MySQL 8.0+
- **ORM**: SQLAlchemy 2.0+
- **认证**: JWT (JSON Web Token)
- **数据验证**: Pydantic 2.0+
- **数据库迁移**: Alembic
- **服务器**: Uvicorn

### 前端
- **框架**: React 18+ (Hooks)
- **语言**: TypeScript 5+
- **UI组件库**: Ant Design 5+
- **状态管理**: Zustand
- **路由**: React Router 6+
- **HTTP客户端**: Axios
- **图表库**: Apache ECharts
- **构建工具**: Vite

## 📦 快速开始

### 前置要求

- Python 3.10+
- Node.js 18+
- PostgreSQL 15+ 或 MySQL 8.0+
- Git

### 1. 克隆项目

```bash
git clone https://github.com/yourusername/accountBook.git
cd accountBook
```

### 2. 后端设置

```bash
# 进入后端目录
cd backend

# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt

# 配置环境变量
cp .env.example .env
# 编辑 .env 文件，配置数据库连接等信息

# 执行数据库迁移
alembic upgrade head

# 启动后端服务
uvicorn app.main:app --reload
```

后端服务将运行在 `http://localhost:8000`

API文档地址: `http://localhost:8000/docs`

### 3. 前端设置

```bash
# 进入前端目录
cd frontend

# 安装依赖
npm install
# 或使用 yarn
yarn install
# 或使用 pnpm
pnpm install

# 配置环境变量
cp .env.example .env
# 编辑 .env 文件（如需修改API地址）

# 启动开发服务器
npm run dev
```

前端服务将运行在 `http://localhost:5173`

## 🐳 Docker 部署

```bash
# 使用 Docker Compose 一键启动
docker-compose up -d

# 查看运行状态
docker-compose ps

# 停止服务
docker-compose down
```

服务将运行在:
- 前端: `http://localhost:80`
- 后端: `http://localhost:8000`
- 数据库: `localhost:5432`

## 📁 项目结构

```
accountBook/
├── backend/                 # 后端项目
│   ├── app/
│   │   ├── api/            # API路由
│   │   ├── core/           # 核心配置
│   │   ├── models/         # 数据库模型
│   │   ├── schemas/        # Pydantic模型
│   │   ├── crud/           # CRUD操作
│   │   ├── services/       # 业务逻辑
│   │   └── main.py         # 应用入口
│   ├── alembic/            # 数据库迁移
│   ├── tests/              # 测试
│   └── requirements.txt    # Python依赖
├── frontend/                # 前端项目
│   ├── src/
│   │   ├── assets/         # 静态资源
│   │   ├── components/     # 通用组件
│   │   ├── pages/          # 页面组件
│   │   ├── store/          # 状态管理
│   │   ├── services/       # API服务
│   │   ├── types/          # TypeScript类型
│   │   ├── utils/          # 工具函数
│   │   └── routes/         # 路由配置
│   └── package.json        # Node.js依赖
├── design.md               # 产品设计文档
├── plan.md                 # 开发任务计划
├── docker-compose.yml      # Docker编排文件
└── README.md               # 项目说明
```

## 📖 API 文档

启动后端服务后，访问以下地址查看 API 文档：

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### 主要 API 端点

#### 认证
- `POST /api/v1/auth/register` - 用户注册
- `POST /api/v1/auth/login` - 用户登录
- `GET /api/v1/auth/me` - 获取当前用户信息
- `PUT /api/v1/auth/me` - 更新用户信息
- `POST /api/v1/auth/change-password` - 修改密码

#### 分类
- `GET /api/v1/categories` - 获取分类列表
- `POST /api/v1/categories` - 创建分类
- `PUT /api/v1/categories/{id}` - 更新分类
- `DELETE /api/v1/categories/{id}` - 删除分类

#### 账目
- `GET /api/v1/transactions` - 获取账目列表
- `POST /api/v1/transactions` - 创建账目
- `GET /api/v1/transactions/{id}` - 获取账目详情
- `PUT /api/v1/transactions/{id}` - 更新账目
- `DELETE /api/v1/transactions/{id}` - 删除账目

#### 统计
- `GET /api/v1/statistics/overview` - 收支概览
- `GET /api/v1/statistics/category` - 分类统计
- `GET /api/v1/statistics/trend` - 趋势分析
- `GET /api/v1/statistics/ranking` - 排行榜

## 🧪 测试

### 后端测试

```bash
cd backend
pytest
# 查看测试覆盖率
pytest --cov=app tests/
```

### 前端测试

```bash
cd frontend
npm run test
```

## 🚀 部署

### 生产环境部署建议

1. **数据库**: 使用云数据库服务（如阿里云RDS、AWS RDS）
2. **后端**: 使用 Gunicorn + Uvicorn Workers
3. **前端**: 构建静态文件，使用 Nginx 托管
4. **HTTPS**: 使用 Let's Encrypt 免费证书
5. **域名**: 配置域名解析

详细部署文档请参考: [部署指南](./docs/deployment.md)

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

在提交 PR 前，请确保：
1. 代码符合项目规范
2. 添加了必要的测试
3. 更新了相关文档

### 开发规范

#### Git 提交规范
```
feat: 新功能
fix: Bug修复
docs: 文档更新
style: 代码格式调整
refactor: 重构
test: 测试相关
chore: 构建/工具相关
```

示例:
```bash
git commit -m "feat(auth): 实现用户登录功能"
git commit -m "fix(transaction): 修复金额计算错误"
```

## 📝 开发路线图

- [x] 项目初始化
- [x] 产品设计文档
- [x] 开发任务计划
- [ ] Sprint 0: 项目基础搭建
- [ ] Sprint 1: 用户认证
- [ ] Sprint 2: 分类管理
- [ ] Sprint 3: 账目管理
- [ ] Sprint 4: 统计分析
- [ ] Sprint 5: UI优化
- [ ] Sprint 6: 测试与优化
- [ ] Sprint 7: 部署与文档
- [ ] V2.0: 进阶功能

## ❓ 常见问题

### 数据库连接失败？
- 检查数据库服务是否启动
- 检查 `.env` 文件中的数据库配置是否正确
- 检查数据库用户权限

### 前端无法连接后端？
- 检查后端服务是否启动
- 检查 CORS 配置是否正确
- 检查前端 `.env` 文件中的 API 地址

### Token 认证失败？
- 检查 Token 是否过期
- 检查请求头是否正确携带 Token
- 检查后端 JWT 密钥配置

## 📄 许可证

本项目采用 [MIT 许可证](LICENSE)

## 👥 作者

- 开发者: [Your Name]
- 邮箱: your.email@example.com
- GitHub: [@yourusername](https://github.com/yourusername)

## 🙏 致谢

- [FastAPI](https://fastapi.tiangolo.com/) - 现代、高性能的 Python Web 框架
- [React](https://react.dev/) - 用于构建用户界面的 JavaScript 库
- [Ant Design](https://ant.design/) - 企业级 UI 设计语言和 React 组件库
- [ECharts](https://echarts.apache.org/) - 强大的数据可视化库

## 📞 支持

如有问题或建议，欢迎通过以下方式联系：

- 提交 [Issue](https://github.com/yourusername/accountBook/issues)
- 发送邮件: your.email@example.com
- 项目讨论群: [加入讨论]

---

⭐ 如果这个项目对你有帮助，欢迎给个 Star！

