# 记账本后端 (FastAPI)

## 快速开始

### 1. 创建虚拟环境并激活

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# 或 Windows: venv\Scripts\activate
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 配置环境变量

```bash
cp .env.example .env
# 编辑 .env 文件，配置数据库连接等信息
```

**注意**: 默认使用SQLite数据库，无需额外配置。如需切换到PostgreSQL，请参考 [DATABASE_GUIDE.md](./DATABASE_GUIDE.md)

### 3.5 测试数据库连接

```bash
python tests/test_db_connection.py
```

### 4. 启动服务

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 5. 访问API文档

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc
- 健康检查: http://localhost:8000/health

## 项目结构

```
backend/
├── app/
│   ├── api/              # API路由
│   │   └── v1/           # API v1版本
│   ├── core/             # 核心配置
│   │   ├── config.py     # 应用配置
│   │   └── database.py   # 数据库配置
│   ├── models/           # SQLAlchemy模型
│   ├── schemas/          # Pydantic模型
│   ├── crud/             # CRUD操作
│   ├── services/         # 业务逻辑
│   ├── utils/            # 工具函数
│   └── main.py           # 应用入口
├── alembic/              # 数据库迁移
├── tests/                # 测试
├── .env                  # 环境变量（不提交到Git）
├── .env.example          # 环境变量示例
└── requirements.txt      # Python依赖
```

## 开发命令

```bash
# 启动开发服务器（自动重载）
uvicorn app.main:app --reload

# 运行测试
pytest

# 查看测试覆盖率
pytest --cov=app tests/

# 数据库迁移
alembic revision --autogenerate -m "描述"
alembic upgrade head
```

## 技术栈

- FastAPI 0.104+
- SQLAlchemy 2.0+
- PostgreSQL 15+
- Pydantic 2.0+
- Alembic
- JWT认证

