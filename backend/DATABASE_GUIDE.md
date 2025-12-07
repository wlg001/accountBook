# 数据库配置指南

## 当前配置

**开发环境**: SQLite  
**数据库文件**: `accountbook.db`  
**优点**: 简单、快速、无需安装

## 为什么使用SQLite（开发环境）？

1. ✅ **零配置**: Python内置支持，无需安装额外软件
2. ✅ **轻量级**: 单文件数据库，易于备份和移动
3. ✅ **快速**: 对于小型项目和开发非常快
4. ✅ **学习友好**: 专注于业务逻辑，而不是数据库配置

## 切换到PostgreSQL（生产环境）

当你准备部署到生产环境，或者需要PostgreSQL的高级特性时，可以轻松切换。

### 步骤1: 安装PostgreSQL

#### 方式A: Docker（推荐）

```bash
# 拉取PostgreSQL镜像
docker pull postgres:15

# 运行PostgreSQL容器
docker run --name accountbook-db \
  -e POSTGRES_USER=accountbook_user \
  -e POSTGRES_PASSWORD=your_password \
  -e POSTGRES_DB=accountbook \
  -p 5432:5432 \
  -d postgres:15

# 验证运行状态
docker ps
```

#### 方式B: 本地安装

**Ubuntu/Debian**:
```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
```

**Mac (Homebrew)**:
```bash
brew install postgresql@15
brew services start postgresql@15
```

**Windows**:
下载并安装：https://www.postgresql.org/download/windows/

### 步骤2: 创建数据库和用户

```bash
# 连接到PostgreSQL
psql -U postgres

# 在psql中执行
CREATE DATABASE accountbook;
CREATE USER accountbook_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE accountbook TO accountbook_user;
\q
```

### 步骤3: 安装Python驱动

```bash
# 激活虚拟环境
source venv/bin/activate

# 安装psycopg2
pip install psycopg2-binary==2.9.9

# 更新requirements.txt
pip freeze > requirements.txt
```

### 步骤4: 更新环境变量

编辑 `.env` 文件：

```env
# 注释掉SQLite
# DATABASE_URL=sqlite:///./accountbook.db

# 启用PostgreSQL
DATABASE_URL=postgresql://accountbook_user:your_password@localhost:5432/accountbook
```

### 步骤5: 迁移数据（可选）

如果你在SQLite中已经有数据：

```bash
# 方法1: 使用数据迁移工具
pip install sqlalchemy-migrate

# 方法2: 导出/导入（推荐重新初始化数据库）
# 重新运行数据库迁移
alembic upgrade head
```

### 步骤6: 测试连接

```bash
# 运行测试脚本
python tests/test_db_connection.py
```

## SQLite vs PostgreSQL 对比

| 特性 | SQLite | PostgreSQL |
|------|--------|------------|
| 安装 | 无需安装 | 需要安装 |
| 配置 | 零配置 | 需要配置用户和权限 |
| 性能 | 小数据量快 | 大数据量快 |
| 并发 | 有限制 | 优秀 |
| 数据类型 | 基础类型 | 丰富的类型（JSON、数组等） |
| 适用场景 | 开发、测试、小项目 | 生产、大项目、高并发 |

## 常见问题

### Q: SQLite数据会丢失吗？
A: 不会，SQLite是真正的关系数据库，数据持久化在 `accountbook.db` 文件中。

### Q: 什么时候应该切换到PostgreSQL？
A: 以下情况建议切换：
- 准备部署到生产环境
- 需要多用户同时访问
- 数据量超过100万条记录
- 需要PostgreSQL特有功能（如全文搜索、JSON字段）

### Q: 切换数据库会影响代码吗？
A: 不会！这就是使用SQLAlchemy ORM的优势，切换数据库只需修改连接字符串。

### Q: 数据库文件在哪里？
A: SQLite数据库文件在 `backend/accountbook.db`

## 数据库管理工具

### SQLite工具
- **DB Browser for SQLite**: https://sqlitebrowser.org/
- **DBeaver**: https://dbeaver.io/
- **命令行**: `sqlite3 accountbook.db`

### PostgreSQL工具
- **pgAdmin**: https://www.pgadmin.org/
- **DBeaver**: https://dbeaver.io/
- **DataGrip**: https://www.jetbrains.com/datagrip/

## 备份与恢复

### SQLite
```bash
# 备份
cp accountbook.db accountbook_backup.db

# 恢复
cp accountbook_backup.db accountbook.db
```

### PostgreSQL
```bash
# 备份
pg_dump -U accountbook_user accountbook > backup.sql

# 恢复
psql -U accountbook_user accountbook < backup.sql
```

## 性能优化建议

### SQLite
- 使用索引加速查询
- 定期执行 VACUUM 清理
- 开启 WAL 模式提高并发

### PostgreSQL
- 合理设置连接池大小
- 创建适当的索引
- 定期执行 ANALYZE 更新统计信息
- 使用 EXPLAIN 分析慢查询

---

**推荐**: 开发阶段使用SQLite，生产部署使用PostgreSQL。

