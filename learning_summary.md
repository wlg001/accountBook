# 记账本项目 - 学习笔记与知识总结

> 这是我的第一个前后端分离项目，记录开发过程中学到的知识点和经验总结。

**项目开始时间**: 2025-12-07  
**当前进度**: Sprint 0 完成（项目初始化）  
**最后更新**: 2025-12-07

---

## 📚 目录

- [项目概述](#项目概述)
- [技术栈学习](#技术栈学习)
- [Sprint 0: 项目初始化](#sprint-0-项目初始化)
- [开发规范与最佳实践](#开发规范与最佳实践)
- [常见问题与解决方案](#常见问题与解决方案)
- [学习资源](#学习资源)

---

## 🎯 项目概述

### 项目简介
一个前后端分离的个人记账本Web应用，用于学习现代Web开发技术栈。

### 技术架构
```
前端 (React)  ←→  后端 (FastAPI)  ←→  数据库 (PostgreSQL)
   ↓                    ↓                    ↓
 用户界面            业务逻辑              数据存储
```

### 学习目标
- ✅ 掌握前后端分离架构
- ✅ 学习React + TypeScript开发
- ✅ 学习FastAPI后端开发
- ✅ 理解RESTful API设计
- ✅ 掌握数据库设计
- ✅ 学习项目工程化实践

---

## 🛠️ 技术栈学习

### 后端技术栈

#### 1. FastAPI 框架

**什么是FastAPI？**
- 现代、快速（高性能）的Python Web框架
- 基于标准Python类型提示
- 自动生成API文档（Swagger UI）

**核心特性**：
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

**学到的知识点**：
- ✅ FastAPI应用创建和配置
- ✅ 路由定义和HTTP方法（GET、POST、PUT、DELETE）
- ✅ CORS中间件配置（跨域资源共享）
- ✅ 自动API文档生成（/docs 和 /redoc）

**为什么选择FastAPI？**
- 性能优秀（与NodeJS和Go相当）
- 开发效率高（减少40%的代码错误）
- 自动数据验证
- 内置文档生成

#### 2. Pydantic 数据验证

**什么是Pydantic？**
- Python数据验证库
- 使用Python类型提示进行数据验证

**示例**：
```python
from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str
    age: int
```

**学到的知识点**：
- ✅ 使用BaseModel定义数据模型
- ✅ 自动类型验证和转换
- ✅ Request/Response数据结构定义

#### 3. SQLAlchemy ORM

**什么是ORM？**
- ORM = Object-Relational Mapping（对象关系映射）
- 用Python对象操作数据库，不需要写SQL

**为什么使用ORM？**
- 代码更易读易维护
- 防止SQL注入
- 支持多种数据库切换

**学到的知识点**：
- ✅ 数据库连接配置
- ✅ 会话管理（SessionLocal）
- ✅ 依赖注入（get_db）

#### 4. 虚拟环境管理

**什么是虚拟环境？**
- 为每个项目创建独立的Python环境
- 避免不同项目的依赖冲突

**命令**：
```bash
# 创建虚拟环境
python3 -m venv venv

# 激活虚拟环境
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# 安装依赖
pip install -r requirements.txt
```

**学到的知识点**：
- ✅ 虚拟环境的创建和激活
- ✅ requirements.txt依赖管理
- ✅ pip包管理工具使用

#### 5. 环境变量配置

**为什么使用.env文件？**
- 敏感信息（密码、密钥）不提交到Git
- 不同环境（开发、生产）配置分离

**示例**：
```env
DATABASE_URL=postgresql://user:password@localhost/dbname
SECRET_KEY=your-secret-key
DEBUG=True
```

**学到的知识点**：
- ✅ .env和.env.example的区别
- ✅ python-dotenv加载环境变量
- ✅ pydantic-settings配置管理

---

### 前端技术栈

#### 1. React 框架

**什么是React？**
- Facebook开发的JavaScript UI库
- 组件化开发
- 虚拟DOM提高性能

**核心概念**：
```tsx
function App() {
  return (
    <div>
      <h1>Hello React</h1>
    </div>
  );
}
```

**学到的知识点**：
- ✅ 函数式组件
- ✅ JSX语法（在JS中写HTML）
- ✅ 组件化思想

#### 2. TypeScript

**什么是TypeScript？**
- JavaScript的超集，添加了类型系统
- 在编译时发现错误，而不是运行时

**示例**：
```typescript
// JavaScript（无类型）
function add(a, b) {
  return a + b;
}

// TypeScript（有类型）
function add(a: number, b: number): number {
  return a + b;
}
```

**学到的知识点**：
- ✅ 基础类型（string、number、boolean）
- ✅ 接口（interface）定义
- ✅ 类型推断
- ✅ tsconfig.json配置

**为什么使用TypeScript？**
- 代码更安全（类型检查）
- IDE智能提示更好
- 代码可维护性更高

#### 3. Vite 构建工具

**什么是Vite？**
- 下一代前端构建工具
- 开发时极快的热更新（HMR）

**对比Webpack**：
- Vite启动更快（秒级 vs 分钟级）
- 开发体验更好

**学到的知识点**：
- ✅ Vite项目创建（npm create vite@latest）
- ✅ 开发服务器启动（npm run dev）
- ✅ 生产构建（npm run build）
- ✅ 环境变量配置（VITE_前缀）

#### 4. Ant Design UI库

**什么是Ant Design？**
- 阿里巴巴开发的企业级UI组件库
- 开箱即用的高质量组件

**示例**：
```tsx
import { Button, Card, Form } from 'antd';

<Button type="primary">按钮</Button>
<Card title="卡片">内容</Card>
```

**学到的知识点**：
- ✅ 组件库的引入和使用
- ✅ ConfigProvider全局配置
- ✅ 主题定制（token配置）
- ✅ 中文语言包配置

#### 5. Axios HTTP客户端

**什么是Axios？**
- 基于Promise的HTTP客户端
- 可在浏览器和Node.js中使用

**核心功能**：
```typescript
// 创建实例
const api = axios.create({
  baseURL: 'http://localhost:8000/api',
});

// 请求拦截器（添加Token）
api.interceptors.request.use(config => {
  config.headers.Authorization = `Bearer ${token}`;
  return config;
});

// 响应拦截器（错误处理）
api.interceptors.response.use(
  response => response.data,
  error => {
    // 统一错误处理
  }
);
```

**学到的知识点**：
- ✅ Axios实例创建
- ✅ 请求拦截器和响应拦截器
- ✅ 统一错误处理
- ✅ Token自动添加

#### 6. Zustand 状态管理

**什么是状态管理？**
- 管理应用中多个组件共享的数据
- 避免Props层层传递（Props Drilling）

**为什么选择Zustand？**
- 比Redux简单
- 体积小（~1kb）
- 无样板代码

**示例**：
```typescript
import { create } from 'zustand';

const useStore = create((set) => ({
  user: null,
  setUser: (user) => set({ user }),
}));
```

**学到的知识点**：
- ✅ Store的创建
- ✅ 状态的读取和更新
- ✅ 全局状态管理思想

---

## 🚀 Sprint 0: 项目初始化

### Task 0.1: 项目基础结构创建

**完成时间**: 2025-12-07  
**用时**: ~10分钟

#### 学到的知识点

**1. Git版本控制基础**

```bash
# 初始化Git仓库
git init

# 添加文件到暂存区
git add .

# 提交到本地仓库
git commit -m "提交信息"

# 查看提交历史
git log --oneline
```

**Git提交规范**：
- `feat`: 新功能
- `fix`: Bug修复
- `docs`: 文档更新
- `chore`: 构建/工具相关

**为什么重要？**
- 代码版本管理
- 团队协作基础
- 代码回溯能力

**2. .gitignore文件**

**作用**：告诉Git哪些文件不需要提交

**常见忽略**：
```gitignore
# Python
__pycache__/
*.pyc
venv/
.env

# Node.js
node_modules/
.env

# IDE
.vscode/
.idea/
```

**为什么重要？**
- 敏感信息不泄露（.env）
- 减小仓库体积（node_modules）
- 避免环境冲突

**3. README.md文档**

**好的README包含**：
- 项目简介
- 技术栈
- 快速开始
- API文档
- 常见问题

**Markdown语法**：
```markdown
# 一级标题
## 二级标题

**粗体**
*斜体*

- 列表项
1. 有序列表

[链接](url)
![图片](url)
```

#### 关键命令总结

```bash
# Git相关
git init                    # 初始化仓库
git add -A                  # 添加所有文件
git commit -m "message"     # 提交
git status                  # 查看状态
git log --oneline          # 查看历史
```

---

### Task 0.2: 后端项目初始化

**完成时间**: 2025-12-07  
**用时**: ~20分钟

#### 学到的知识点

**1. Python虚拟环境**

**为什么需要虚拟环境？**
- 项目A需要Django 3.0，项目B需要Django 4.0
- 虚拟环境为每个项目创建独立的Python环境

**命令流程**：
```bash
# 1. 创建虚拟环境
python3 -m venv venv

# 2. 激活虚拟环境
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows

# 3. 安装依赖
pip install -r requirements.txt

# 4. 退出虚拟环境
deactivate
```

**2. FastAPI项目结构**

```
backend/
├── app/
│   ├── main.py          # 应用入口
│   ├── core/            # 核心配置
│   │   ├── config.py    # 配置管理
│   │   └── database.py  # 数据库配置
│   ├── api/             # API路由
│   ├── models/          # 数据库模型
│   ├── schemas/         # Pydantic模型
│   ├── crud/            # CRUD操作
│   └── services/        # 业务逻辑
├── tests/               # 测试
├── alembic/             # 数据库迁移
├── .env                 # 环境变量
└── requirements.txt     # 依赖列表
```

**为什么这样组织？**
- 代码分层清晰
- 易于维护和扩展
- 符合行业最佳实践

**3. CORS跨域配置**

**什么是CORS？**
- CORS = Cross-Origin Resource Sharing（跨域资源共享）
- 浏览器安全机制，限制跨域请求

**为什么需要配置CORS？**
```
前端: http://localhost:5173
后端: http://localhost:8000
↑ 不同端口 = 跨域
```

**配置方法**：
```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # 允许的源
    allow_credentials=True,                   # 允许携带凭证
    allow_methods=["*"],                      # 允许所有HTTP方法
    allow_headers=["*"],                      # 允许所有请求头
)
```

**4. 配置管理（Pydantic Settings）**

**为什么使用配置类？**
- 集中管理配置
- 自动加载.env文件
- 类型验证

**示例**：
```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "记账本API"
    DATABASE_URL: str
    SECRET_KEY: str
    
    class Config:
        env_file = ".env"

settings = Settings()
```

**5. uvicorn服务器**

**什么是uvicorn？**
- ASGI服务器（异步服务器网关接口）
- 用于运行FastAPI应用

**启动命令**：
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**参数说明**：
- `app.main:app`: 应用路径（模块:变量）
- `--reload`: 代码改动自动重启（仅开发环境）
- `--host 0.0.0.0`: 监听所有网络接口
- `--port 8000`: 端口号

#### 关键命令总结

```bash
# Python虚拟环境
python3 -m venv venv                    # 创建虚拟环境
source venv/bin/activate                # 激活虚拟环境
pip install -r requirements.txt         # 安装依赖

# FastAPI服务
uvicorn app.main:app --reload          # 启动开发服务器
```

#### 重要概念理解

**依赖注入（Dependency Injection）**：
```python
from fastapi import Depends

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    # db会自动注入
    return db.query(User).all()
```

**为什么使用依赖注入？**
- 代码解耦
- 易于测试
- 自动资源管理

---

### Task 0.3: 前端项目初始化

**完成时间**: 2025-12-07  
**用时**: ~25分钟

#### 学到的知识点

**1. Vite快速创建项目**

```bash
# 创建React + TypeScript项目
npm create vite@latest frontend -- --template react-ts

# 进入目录
cd frontend

# 安装依赖
npm install

# 启动开发服务器
npm run dev
```

**Vite的优势**：
- 启动速度极快（利用ES模块）
- 热更新快速（只更新改变的模块）
- 生产构建优化（Rollup）

**2. npm包管理**

**package.json**：项目配置文件
```json
{
  "name": "frontend",
  "version": "1.0.0",
  "dependencies": {    // 生产依赖
    "react": "^18.2.0"
  },
  "devDependencies": { // 开发依赖
    "vite": "^5.0.0"
  },
  "scripts": {         // 脚本命令
    "dev": "vite",
    "build": "vite build"
  }
}
```

**版本号说明**：
- `^18.2.0`: 兼容18.x.x版本
- `~18.2.0`: 兼容18.2.x版本
- `18.2.0`: 精确版本

**package-lock.json**：锁定依赖版本
- 确保团队使用相同版本
- 提高安装速度

**3. 前端项目结构**

```
frontend/
├── src/
│   ├── assets/          # 静态资源
│   ├── components/      # 通用组件
│   ├── pages/           # 页面组件
│   ├── store/           # 状态管理
│   ├── services/        # API服务
│   ├── types/           # TypeScript类型
│   ├── utils/           # 工具函数
│   ├── routes/          # 路由配置
│   ├── App.tsx          # 根组件
│   └── main.tsx         # 入口文件
├── public/              # 公共资源
├── .env                 # 环境变量
├── package.json         # 依赖配置
├── tsconfig.json        # TS配置
└── vite.config.ts       # Vite配置
```

**组织原则**：
- 按功能模块划分
- 相关文件放在一起
- 便于查找和维护

**4. TypeScript配置**

**tsconfig.json主要配置**：
```json
{
  "compilerOptions": {
    "target": "ES2020",           // 编译目标
    "module": "ESNext",           // 模块系统
    "jsx": "react-jsx",           // JSX处理
    "strict": true,               // 严格模式
    "moduleResolution": "bundler" // 模块解析
  }
}
```

**为什么需要配置？**
- 控制编译行为
- 启用类型检查
- 配置模块解析

**5. 环境变量（Vite）**

**Vite环境变量规则**：
- 必须以`VITE_`开头
- 在代码中使用`import.meta.env.VITE_XXX`

**示例**：
```env
# .env
VITE_API_BASE_URL=http://localhost:8000/api/v1
```

```typescript
// 使用
const apiUrl = import.meta.env.VITE_API_BASE_URL;
```

**6. ESLint和Prettier**

**ESLint**：代码质量检查
- 发现潜在错误
- 统一代码风格

**Prettier**：代码格式化
- 自动格式化代码
- 统一代码风格

**为什么两个都需要？**
- ESLint关注代码质量（逻辑错误）
- Prettier关注代码格式（空格、换行）

**配置示例**：
```json
// .prettierrc
{
  "semi": true,           // 使用分号
  "singleQuote": true,    // 使用单引号
  "printWidth": 100,      // 每行最大长度
  "tabWidth": 2           // 缩进空格数
}
```

#### 关键命令总结

```bash
# npm包管理
npm install                 # 安装所有依赖
npm install axios          # 安装生产依赖
npm install -D eslint      # 安装开发依赖
npm run dev                # 运行开发服务器
npm run build              # 构建生产版本

# 代码检查和格式化
npm run lint               # ESLint检查
npm run format             # Prettier格式化
```

#### 重要概念理解

**组件化开发**：
```tsx
// 按钮组件
function Button({ text, onClick }) {
  return <button onClick={onClick}>{text}</button>;
}

// 使用组件
function App() {
  return <Button text="点击" onClick={() => alert('clicked')} />;
}
```

**为什么组件化？**
- 代码复用
- 易于维护
- 关注点分离

**响应式设计**：
```css
/* 移动端 */
@media (max-width: 768px) {
  .container { width: 100%; }
}

/* 桌面端 */
@media (min-width: 768px) {
  .container { width: 1200px; }
}
```

---

### Task 0.4: 数据库环境搭建

**完成时间**: 2025-12-07  
**用时**: ~15分钟

#### 学到的知识点

**1. 数据库选择：SQLite vs PostgreSQL**

**为什么选择SQLite作为开发数据库？**
- ✅ 零配置：Python内置支持
- ✅ 单文件数据库：`accountbook.db`
- ✅ 快速上手：专注于业务逻辑
- ✅ 易于切换：SQLAlchemy抽象层

**什么时候切换到PostgreSQL？**
- 准备生产部署
- 需要高并发支持
- 需要高级特性（JSON字段、全文搜索等）
- 数据量超过100万条

**2. SQLite配置要点**

**连接字符串格式**：
```python
# SQLite（相对路径）
DATABASE_URL = "sqlite:///./accountbook.db"

# SQLite（绝对路径）
DATABASE_URL = "sqlite:////absolute/path/to/db.db"

# PostgreSQL
DATABASE_URL = "postgresql://user:password@host:port/dbname"
```

**SQLite特殊配置**：
```python
# check_same_thread=False 允许多线程访问
connect_args = {"check_same_thread": False}

engine = create_engine(
    "sqlite:///./accountbook.db",
    connect_args=connect_args
)
```

**为什么需要 `check_same_thread=False`？**
- SQLite默认只允许创建连接的线程访问
- FastAPI使用多线程处理请求
- 设置为False允许线程间共享连接

**3. SQLAlchemy 2.0 新语法**

**重要变化：text() 函数**

```python
# ❌ 旧语法（会报错）
result = db.execute("SELECT 1")

# ✅ 新语法（正确）
from sqlalchemy import text
result = db.execute(text("SELECT 1"))
```

**为什么改变？**
- 更明确地区分文本SQL和ORM查询
- 防止SQL注入
- 类型安全

**4. 数据库连接测试**

**测试脚本结构**：
```python
def test_database_connection():
    try:
        # 1. 创建会话
        db = SessionLocal()
        
        # 2. 执行测试查询
        result = db.execute(text("SELECT 1"))
        
        # 3. 验证结果
        assert result.scalar() == 1
        
        # 4. 关闭会话
        db.close()
        
        return True
    except Exception as e:
        print(f"错误: {e}")
        return False
```

**5. 数据库迁移策略**

**为什么使用ORM？**
- 数据库无关：切换数据库不改代码
- 类型安全：Python类型检查
- 防止SQL注入：参数化查询
- 易于维护：代码即文档

**SQLAlchemy的三层抽象**：
```
应用代码
   ↓
ORM层（Python类）
   ↓
SQL表达式层
   ↓
数据库连接层
   ↓
实际数据库（SQLite/PostgreSQL）
```

#### 关键命令总结

```bash
# 测试数据库连接
python tests/test_db_connection.py

# 查看SQLite数据库
sqlite3 accountbook.db
.tables           # 查看所有表
.schema users     # 查看表结构
.quit             # 退出

# 备份数据库
cp accountbook.db backup.db

# 切换到PostgreSQL（参考DATABASE_GUIDE.md）
```

#### 重要概念理解

**数据库连接池**：
- 预先创建多个数据库连接
- 请求时从池中获取连接
- 使用完后归还连接池
- 提高性能，减少连接开销

**会话（Session）**：
- 数据库操作的工作单元
- 管理事务（Transaction）
- 跟踪对象变化
- 自动提交或回滚

**依赖注入模式**：
```python
def get_db():
    db = SessionLocal()
    try:
        yield db    # 提供数据库会话
    finally:
        db.close()  # 确保会话关闭

# FastAPI路由中使用
@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()
```

**为什么使用依赖注入？**
- 自动管理资源（打开/关闭）
- 代码更清晰
- 易于测试（可以注入mock对象）

#### 学到的最佳实践

1. **开发用SQLite，生产用PostgreSQL**
   - 开发时快速迭代
   - 生产时稳定可靠

2. **使用ORM而不是原生SQL**
   - 数据库无关
   - 类型安全
   - 防止SQL注入

3. **环境变量管理敏感信息**
   - 数据库密码
   - API密钥
   - 不提交.env到Git

4. **总是测试数据库连接**
   - 早发现配置问题
   - 验证权限设置
   - 确保环境正确

#### 遇到的问题和解决方案

**问题1**: SQLAlchemy 2.0 text()错误
```
Textual SQL expression 'SELECT 1' should be explicitly declared as text('SELECT 1')
```

**解决**: 导入并使用text()函数
```python
from sqlalchemy import text
result = db.execute(text("SELECT 1"))
```

**学到**: SQLAlchemy 2.0引入了更严格的类型检查，提高了代码安全性。

---

## 📐 开发规范与最佳实践

### 1. 代码命名规范

#### Python（后端）
```python
# 文件名：小写 + 下划线
user_service.py

# 类名：大驼峰（PascalCase）
class UserService:
    pass

# 函数名、变量名：小写 + 下划线
def get_user_by_id(user_id: int):
    user_name = "张三"
```

#### TypeScript（前端）
```typescript
// 文件名：大驼峰（组件）或小驼峰（工具）
UserCard.tsx
userUtils.ts

// 组件名：大驼峰
function UserCard() {}

// 函数名、变量名：小驼峰
function getUserInfo() {
  const userName = "张三";
}

// 常量：全大写 + 下划线
const API_BASE_URL = "http://...";
```

### 2. Git提交规范

**格式**：`<type>(<scope>): <subject>`

**Type类型**：
- `feat`: 新功能
- `fix`: Bug修复
- `docs`: 文档更新
- `style`: 代码格式（不影响代码运行）
- `refactor`: 重构（既不是新功能也不是修复bug）
- `test`: 测试相关
- `chore`: 构建过程或辅助工具的变动

**示例**：
```bash
git commit -m "feat(auth): 实现用户登录功能"
git commit -m "fix(transaction): 修复金额计算错误"
git commit -m "docs(readme): 更新安装文档"
```

### 3. 目录结构最佳实践

**原则**：
- 按功能模块划分，而不是按文件类型
- 相关文件放在一起
- 保持目录层级简单（不超过3-4层）

**好的结构**：
```
src/
├── features/
│   ├── auth/
│   │   ├── Login.tsx
│   │   ├── authStore.ts
│   │   └── authAPI.ts
│   └── transactions/
│       ├── TransactionList.tsx
│       ├── transactionStore.ts
│       └── transactionAPI.ts
```

### 4. API设计规范（RESTful）

**HTTP方法**：
- `GET`: 获取资源
- `POST`: 创建资源
- `PUT`: 更新资源（完整更新）
- `PATCH`: 更新资源（部分更新）
- `DELETE`: 删除资源

**URL命名**：
```
GET    /api/v1/users          # 获取用户列表
GET    /api/v1/users/1        # 获取ID为1的用户
POST   /api/v1/users          # 创建用户
PUT    /api/v1/users/1        # 更新用户
DELETE /api/v1/users/1        # 删除用户
```

**响应格式统一**：
```json
{
  "code": 200,
  "message": "success",
  "data": { ... }
}
```

---

## 🐛 常见问题与解决方案

### 问题1: 端口已被占用

**错误信息**：
```
Error: Port 8000 is already in use
```

**解决方案**：
```bash
# 查找占用端口的进程
lsof -i :8000          # Mac/Linux
netstat -ano | findstr :8000  # Windows

# 杀死进程
kill -9 <PID>          # Mac/Linux
taskkill /PID <PID> /F # Windows
```

### 问题2: npm install很慢

**解决方案**：使用国内镜像
```bash
# 临时使用
npm install --registry=https://registry.npmmirror.com

# 永久配置
npm config set registry https://registry.npmmirror.com
```

### 问题3: Python导入模块失败

**错误信息**：
```
ModuleNotFoundError: No module named 'fastapi'
```

**原因**：虚拟环境未激活

**解决方案**：
```bash
source venv/bin/activate  # 激活虚拟环境
```

### 问题4: CORS跨域错误

**错误信息**：
```
Access to XMLHttpRequest has been blocked by CORS policy
```

**解决方案**：
1. 后端配置CORS中间件
2. 确认前端URL在allow_origins中
3. 检查allow_credentials设置

### 问题5: TypeScript类型错误

**错误信息**：
```
Type 'string' is not assignable to type 'number'
```

**解决方案**：
1. 检查变量类型定义
2. 使用类型断言：`value as number`
3. 使用类型守卫进行类型检查

---

## 📚 学习资源

### 官方文档

**后端相关**：
- [FastAPI官方文档](https://fastapi.tiangolo.com/) - 最权威的FastAPI学习资源
- [Pydantic文档](https://docs.pydantic.dev/) - 数据验证
- [SQLAlchemy文档](https://docs.sqlalchemy.org/) - ORM框架

**前端相关**：
- [React官方文档](https://react.dev/) - React学习起点
- [TypeScript官方文档](https://www.typescriptlang.org/docs/) - TS学习
- [Vite官方文档](https://vitejs.dev/) - 构建工具
- [Ant Design文档](https://ant.design/) - UI组件库

### 推荐教程

**视频教程**：
- B站：尚硅谷React教程
- B站：黑马程序员FastAPI教程

**文章教程**：
- 阮一峰的网络日志 - ES6入门
- MDN Web Docs - JavaScript参考

### 技术社区

- [Stack Overflow](https://stackoverflow.com/) - 技术问答
- [GitHub](https://github.com/) - 开源代码学习
- [掘金](https://juejin.cn/) - 中文技术社区
- [思否](https://segmentfault.com/) - 中文技术问答

---

## 🎯 下一步学习计划

### Sprint 0: 项目初始化 ✅ 已完成

- [x] Task 0.1: 项目基础结构创建
- [x] Task 0.2: 后端项目初始化
- [x] Task 0.3: 前端项目初始化
- [x] Task 0.4: 数据库环境搭建

**已掌握的核心技能**：
- ✅ Git版本控制
- ✅ Python虚拟环境
- ✅ FastAPI框架基础
- ✅ React + TypeScript开发
- ✅ SQLite数据库配置
- ✅ 项目工程化

### Sprint 1: 数据库与认证

**即将学习的知识点**：
- [ ] 数据库设计原则（主键、外键、索引）
- [ ] SQLAlchemy ORM模型定义
- [ ] Alembic数据库迁移
- [ ] JWT认证机制
- [ ] 密码加密（bcrypt）
- [ ] Token刷新策略
- [ ] React Router路由管理
- [ ] 表单处理（Ant Design Form）
- [ ] 受保护路由（路由守卫）

### Sprint 2-3: 核心业务功能

**即将学习的知识点**：
- [ ] CRUD操作实现
- [ ] 复杂查询（筛选、分页、排序）
- [ ] 表单验证
- [ ] 文件上传
- [ ] 状态管理进阶

### Sprint 4: 数据可视化

**即将学习的知识点**：
- [ ] ECharts图表配置
- [ ] 数据聚合和统计
- [ ] 性能优化

---

## 💡 学习心得

### Sprint 0 总结 ✅

**完成日期**: 2025-12-07  
**完成任务**: 4个  
**总用时**: ~70分钟  
**状态**: ✅ 100% 完成

**学到的最重要的5件事**：

1. **前后端分离架构**
   - 前端负责展示和交互（React）
   - 后端负责业务逻辑和数据（FastAPI）
   - 通过RESTful API通信
   - 数据库存储持久化数据（SQLite）
   
2. **项目工程化**
   - 使用Git版本控制（提交规范）
   - 环境变量管理（.env文件）
   - 代码规范和文档（README、设计文档）
   - 目录结构设计（分层清晰）
   
3. **开发工具链**
   - 虚拟环境（Python venv）
   - 包管理（pip、npm）
   - 开发服务器（uvicorn、vite）
   - 数据库工具（SQLite）

4. **ORM与数据库抽象**
   - SQLAlchemy提供数据库无关层
   - 开发用SQLite，生产可切换PostgreSQL
   - ORM的优势：类型安全、防SQL注入
   - 依赖注入管理数据库会话

5. **TypeScript类型系统**
   - 编译时类型检查
   - 接口定义和类型推断
   - 提高代码质量和可维护性

**遇到的挑战及解决**：
1. **CORS跨域问题** 
   - 问题：前端无法访问后端API
   - 解决：配置FastAPI的CORS中间件
   - 学到：理解浏览器同源策略

2. **TypeScript类型错误** 
   - 问题：类型不匹配导致编译失败
   - 解决：正确定义接口和类型
   - 学到：类型系统的重要性

3. **SQLAlchemy 2.0新语法** 
   - 问题：text()函数报错
   - 解决：使用text()包裹SQL字符串
   - 学到：新版本API变化需要关注

4. **数据库选择困惑**
   - 问题：PostgreSQL配置复杂
   - 解决：开发环境用SQLite
   - 学到：根据场景选择合适工具

**完成的里程碑**：
- ✅ 项目基础架构搭建完成
- ✅ 后端API框架可运行
- ✅ 前端React应用可访问
- ✅ 数据库连接测试通过
- ✅ Git版本控制建立
- ✅ 开发文档完善

**下一步改进**：
- 深入学习SQLAlchemy模型定义
- 掌握Alembic数据库迁移
- 学习JWT认证实现
- 加强TypeScript类型定义
- 学习React Hooks和状态管理

---

## 📊 学习统计

| Sprint | 任务数 | 完成时间 | 学到的核心概念数 |
|--------|--------|----------|------------------|
| Sprint 0 | 4 | ~70分钟 | 30+ |

**技术栈掌握度**（自评）：
- Python基础: ⭐⭐⭐⭐☆
- FastAPI: ⭐⭐⭐☆☆
- JavaScript: ⭐⭐⭐⭐☆
- React: ⭐⭐⭐☆☆
- TypeScript: ⭐⭐☆☆☆
- 数据库: ⭐⭐⭐☆☆  ← 提升！
- SQLAlchemy: ⭐⭐⭐☆☆  ← 新增！

---

## 📝 学习笔记模板

每完成一个Task，用以下模板更新：

```markdown
### Task X.X: 任务名称

**完成时间**: YYYY-MM-DD
**用时**: X分钟

#### 学到的知识点

1. **知识点1**
   - 概念解释
   - 为什么重要
   - 代码示例

2. **知识点2**
   ...

#### 关键命令总结

```bash
命令1  # 说明
命令2  # 说明
```

#### 重要概念理解

- 概念A：解释
- 概念B：解释

#### 遇到的问题和解决方案

**问题**：问题描述
**解决**：解决方案
**学到**：经验总结
```

---

**持续更新中...**

> 记住：学习是一个持续的过程，不要害怕犯错，每个错误都是学习的机会！💪

