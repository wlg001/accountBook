# 记账本Web应用 - 产品设计文档

## 📋 一、产品经理视角 - 需求分析

### 1.1 产品定位
一款简洁易用的个人财务管理工具，帮助用户记录日常收支、分析消费习惯、合理规划预算。

### 1.2 目标用户
- **主要用户**：25-40岁，有理财意识的上班族
- **次要用户**：大学生、自由职业者、家庭主妇
- **用户痛点**：
  - 不清楚钱花在哪里
  - 月底总是超支
  - 没有直观的消费数据分析
  - 传统记账方式繁琐

### 1.3 核心功能（MVP）

#### 功能1：用户管理
- 用户注册/登录
- 个人信息管理
- 密码修改

#### 功能2：快速记账
- **收入记录**：工资、奖金、投资收益等
- **支出记录**：餐饮、交通、购物、娱乐等
- **必填字段**：金额、分类、日期
- **可选字段**：备注、标签、账户类型
- **快捷操作**：常用分类快速选择、金额计算器

#### 功能3：分类管理
- **预设分类**：
  - 支出：餐饮、交通、购物、娱乐、医疗、教育、住房、其他
  - 收入：工资、奖金、投资、兼职、其他
- **自定义分类**：用户可添加、编辑、删除分类
- **分类图标**：每个分类配有独特图标

#### 功能4：账目查询
- 按日期范围筛选
- 按分类筛选
- 按收支类型筛选
- 搜索备注关键词
- 账目列表展示（支持分页）

#### 功能5：数据统计
- **收支概览**：今日/本周/本月/本年的收支总额
- **分类统计**：饼图展示各分类占比
- **趋势分析**：折线图展示收支趋势
- **排行榜**：支出最多的分类TOP5

### 1.4 进阶功能（V2.0）

#### 功能6：预算管理
- 设置月度预算（总预算、分类预算）
- 预算执行进度条
- 超支提醒

#### 功能7：账户管理
- 多账户支持（现金、银行卡、支付宝、微信等）
- 账户余额显示
- 账户间转账

#### 功能8：定期账目
- 设置定期收支（如房租、工资）
- 自动记账提醒

#### 功能9：数据导出
- 导出Excel报表
- 导出PDF账单

#### 功能10：数据备份与恢复
- 云端自动备份
- 手动导入导出

---

## 🎨 二、设计师视角 - UI/UX设计

### 2.1 设计理念
- **简洁至上**：减少操作步骤，快速完成记账
- **数据可视化**：用图表直观呈现财务状况
- **友好反馈**：每个操作都有清晰的视觉反馈
- **移动优先**：响应式设计，适配各种设备

### 2.2 色彩方案

```
主色调：
- 主题色：#1890ff（蓝色）- 品牌色、按钮、链接
- 收入色：#52c41a（绿色）- 收入金额、收入图表
- 支出色：#ff4d4f（红色）- 支出金额、支出图表

辅助色：
- 背景色：#f0f2f5（浅灰）- 页面背景
- 卡片色：#ffffff（白色）- 卡片背景
- 文字色：#262626（深灰）- 主要文字
- 次要文字：#8c8c8c（中灰）- 次要信息
- 边框色：#d9d9d9（浅灰）- 分隔线

状态色：
- 成功：#52c41a（绿色）
- 警告：#faad14（橙色）
- 错误：#ff4d4f（红色）
- 信息：#1890ff（蓝色）
```

### 2.3 页面结构

#### 布局方案
```
┌─────────────────────────────────┐
│         顶部导航栏               │
├───────┬─────────────────────────┤
│       │                         │
│  侧   │      主内容区            │
│  边   │                         │
│  栏   │                         │
│       │                         │
└───────┴─────────────────────────┘
```

#### 导航结构
- **顶部导航**：Logo、用户头像、退出登录
- **侧边导航**：
  - 📊 仪表盘（Dashboard）
  - ➕ 快速记账
  - 📝 账目列表
  - 📈 统计分析
  - 🏷️ 分类管理
  - 💰 预算管理（V2.0）
  - ⚙️ 设置

### 2.4 关键页面设计

#### 页面1：仪表盘（Dashboard）
```
┌─────────────────────────────────────────┐
│  本月收支概览                            │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐   │
│  │ 收入    │ │ 支出    │ │ 结余    │   │
│  │ ¥8,000 │ │ ¥5,200 │ │ ¥2,800 │   │
│  └─────────┘ └─────────┘ └─────────┘   │
└─────────────────────────────────────────┘

┌─────────────────┐  ┌──────────────────┐
│ 支出分类占比     │  │ 近7日收支趋势    │
│  (饼图)         │  │  (折线图)        │
│                 │  │                  │
└─────────────────┘  └──────────────────┘

┌─────────────────────────────────────────┐
│  最近记录                                │
│  ┌────────────────────────────────────┐ │
│  │ 🍜 午餐  -¥35  2025-12-07         │ │
│  │ 🚌 地铁  -¥4   2025-12-07         │ │
│  │ 💰 工资  +¥8000  2025-12-05       │ │
│  └────────────────────────────────────┘ │
└─────────────────────────────────────────┘
```

#### 页面2：快速记账
```
┌─────────────────────────────────────────┐
│  记一笔                                  │
│                                         │
│  [ 支出 ]  [ 收入 ]  <-- 切换按钮       │
│                                         │
│  金额                                   │
│  ┌─────────────────────────────────┐   │
│  │  ¥ 0.00                         │   │
│  └─────────────────────────────────┘   │
│                                         │
│  计算器键盘                              │
│  ┌───┬───┬───┬───────┐               │
│  │ 1 │ 2 │ 3 │   +   │               │
│  ├───┼───┼───┼───────┤               │
│  │ 4 │ 5 │ 6 │   -   │               │
│  ├───┼───┼───┼───────┤               │
│  │ 7 │ 8 │ 9 │   ×   │               │
│  ├───┼───┼───┼───────┤               │
│  │ . │ 0 │ ⌫ │   =   │               │
│  └───┴───┴───┴───────┘               │
│                                         │
│  分类                                   │
│  [ 🍜餐饮 ] [ 🚌交通 ] [ 🛍️购物 ]      │
│  [ 🎬娱乐 ] [ 🏥医疗 ] [ 📚教育 ]      │
│                                         │
│  日期：2025-12-07  [选择]               │
│  备注：______________________           │
│                                         │
│          [ 保 存 ]                      │
└─────────────────────────────────────────┘
```

#### 页面3：账目列表
```
┌─────────────────────────────────────────┐
│  筛选：[本月▼] [全部分类▼] [🔍搜索]     │
├─────────────────────────────────────────┤
│  2025年12月  收入 ¥8,000  支出 ¥5,200   │
├─────────────────────────────────────────┤
│  12月07日 周六                  -¥39    │
│  ├─ 🍜 午餐        -¥35  备注：xxx     │
│  └─ 🚌 地铁        -¥4                 │
├─────────────────────────────────────────┤
│  12月06日 周五                  -¥128   │
│  ├─ 🛍️ 购物       -¥98  备注：xxx     │
│  └─ 🚌 打车        -¥30                │
├─────────────────────────────────────────┤
│  12月05日 周四                 +¥8000   │
│  └─ 💰 工资       +¥8000               │
└─────────────────────────────────────────┘
```

#### 页面4：统计分析
```
┌─────────────────────────────────────────┐
│  时间范围：[本月▼]                       │
├─────────────────────────────────────────┤
│  ┌─────────┐ ┌─────────┐ ┌─────────┐   │
│  │ 收入    │ │ 支出    │ │ 结余    │   │
│  │ ¥8,000 │ │ ¥5,200 │ │ ¥2,800 │   │
│  └─────────┘ └─────────┘ └─────────┘   │
├─────────────────────────────────────────┤
│  收支趋势                                │
│  (折线图：横轴日期，纵轴金额)            │
│                                         │
├─────────────────────────────────────────┤
│  支出分类占比                            │
│  (饼图)          (列表)                 │
│                  🍜 餐饮  ¥1,200 (23%) │
│                  🚌 交通  ¥800  (15%)  │
│                  🛍️ 购物  ¥2,000 (38%)│
└─────────────────────────────────────────┘
```

### 2.5 交互设计

#### 动画效果
- 页面切换：淡入淡出（300ms）
- 按钮点击：轻微缩放反馈
- 数据加载：骨架屏 + 加载动画
- 图表渲染：渐进式动画

#### 操作反馈
- 成功提示：绿色Toast，2秒后自动消失
- 错误提示：红色Toast，3秒后自动消失
- 加载状态：Spin组件
- 确认操作：Modal弹窗二次确认

#### 响应式适配
- **桌面端（>1200px）**：侧边栏常驻 + 多列布局
- **平板端（768-1200px）**：可折叠侧边栏 + 双列布局
- **移动端（<768px）**：底部导航栏 + 单列布局

---

## 🏗️ 三、架构师视角 - 技术架构

### 3.1 技术栈选型

#### 后端技术栈
```
核心框架：FastAPI 0.104+
- 高性能异步框架
- 自动生成API文档（Swagger UI）
- 类型提示支持

数据库：PostgreSQL 15+ / MySQL 8.0+
- 推荐PostgreSQL（更强大的数据类型支持）

ORM：SQLAlchemy 2.0+
- 声明式模型定义
- 异步支持（async/await）

数据验证：Pydantic 2.0+
- 请求/响应数据验证
- 自动生成JSON Schema

认证：JWT（JSON Web Token）
- python-jose：JWT生成与验证
- passlib：密码加密

数据库迁移：Alembic
- 版本化数据库迁移

其他依赖：
- uvicorn：ASGI服务器
- python-multipart：文件上传支持
- python-dotenv：环境变量管理
```

#### 前端技术栈
```
核心框架：React 18+
- Hooks优先
- 函数式组件

语言：TypeScript 5+
- 类型安全
- 更好的IDE支持

UI组件库：Ant Design 5+ (antd)
- 企业级UI组件
- 开箱即用的图表组件

状态管理：Zustand / Redux Toolkit
- 推荐Zustand（更轻量简洁）

路由：React Router 6+
- 声明式路由

HTTP客户端：Axios
- 请求拦截器（添加Token）
- 响应拦截器（统一错误处理）

图表库：Apache ECharts / Recharts
- 推荐ECharts（功能更强大）

工具链：
- Vite：构建工具（快速热更新）
- ESLint + Prettier：代码规范
- Tailwind CSS：可选的原子化CSS
```

### 3.2 系统架构

#### 整体架构图
```
┌─────────────────────────────────────────────┐
│                  用户端                      │
│            (浏览器 / 移动端)                 │
└──────────────────┬──────────────────────────┘
                   │ HTTPS
                   │
┌──────────────────▼──────────────────────────┐
│               前端应用层                      │
│          (React + TypeScript)                │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  │
│  │ 页面组件  │  │ 状态管理  │  │ API封装   │  │
│  └──────────┘  └──────────┘  └──────────┘  │
└──────────────────┬──────────────────────────┘
                   │ RESTful API / JSON
                   │
┌──────────────────▼──────────────────────────┐
│               后端应用层                      │
│              (FastAPI)                       │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  │
│  │ 路由层    │  │ 业务逻辑  │  │ 认证中间件 │  │
│  └──────────┘  └──────────┘  └──────────┘  │
├─────────────────────────────────────────────┤
│               数据访问层                      │
│           (SQLAlchemy ORM)                   │
│  ┌──────────┐  ┌──────────┐                 │
│  │ Models   │  │ CRUD操作  │                 │
│  └──────────┘  └──────────┘                 │
└──────────────────┬──────────────────────────┘
                   │ SQL
                   │
┌──────────────────▼──────────────────────────┐
│              数据存储层                       │
│          (PostgreSQL / MySQL)                │
└─────────────────────────────────────────────┘
```

### 3.3 数据库设计

#### ER图概述
```
┌──────────┐      ┌──────────┐      ┌──────────┐
│  Users   │──┬──→│Transactions│←───→│Categories│
│  用户表   │  │   │  账目表    │      │  分类表   │
└──────────┘  │   └──────────┘      └──────────┘
              │
              │   ┌──────────┐
              └──→│ Budgets  │
                  │  预算表   │
                  └──────────┘
```

#### 表结构设计

**1. users（用户表）**
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    nickname VARCHAR(50),
    avatar_url VARCHAR(255),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

索引：
- idx_users_username (username)
- idx_users_email (email)
```

**2. categories（分类表）**
```sql
CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    name VARCHAR(50) NOT NULL,
    type VARCHAR(10) NOT NULL,  -- 'income' 或 'expense'
    icon VARCHAR(50),  -- 图标名称
    color VARCHAR(20),  -- 颜色代码
    is_system BOOLEAN DEFAULT FALSE,  -- 是否系统预设
    sort_order INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    UNIQUE(user_id, name, type)
);

索引：
- idx_categories_user_id (user_id)
- idx_categories_type (type)
```

**3. transactions（账目表）**
```sql
CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    category_id INTEGER REFERENCES categories(id) ON DELETE SET NULL,
    amount DECIMAL(12, 2) NOT NULL,  -- 金额（精确到分）
    type VARCHAR(10) NOT NULL,  -- 'income' 或 'expense'
    transaction_date DATE NOT NULL,  -- 账目日期
    description TEXT,  -- 备注
    tags VARCHAR(255),  -- 标签（逗号分隔）
    account_type VARCHAR(50),  -- 账户类型（现金/银行卡/支付宝等）V2.0
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

索引：
- idx_transactions_user_id (user_id)
- idx_transactions_date (transaction_date)
- idx_transactions_category (category_id)
- idx_transactions_type (type)
- idx_transactions_user_date (user_id, transaction_date) -- 组合索引
```

**4. budgets（预算表）** - V2.0
```sql
CREATE TABLE budgets (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    category_id INTEGER REFERENCES categories(id) ON DELETE CASCADE,
    amount DECIMAL(12, 2) NOT NULL,  -- 预算金额
    period_type VARCHAR(20) NOT NULL,  -- 'monthly' 或 'yearly'
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    UNIQUE(user_id, category_id, start_date)
);

索引：
- idx_budgets_user_id (user_id)
- idx_budgets_period (start_date, end_date)
```

### 3.4 API设计

#### API规范
- **基础URL**：`http://localhost:8000/api/v1`
- **认证方式**：Bearer Token（JWT）
- **请求格式**：JSON
- **响应格式**：JSON

#### 统一响应格式
```json
成功响应：
{
  "code": 200,
  "message": "success",
  "data": { ... }
}

错误响应：
{
  "code": 400/401/403/404/500,
  "message": "错误描述",
  "detail": "详细错误信息"
}
```

#### API端点列表

**认证相关**
```
POST   /api/v1/auth/register          # 用户注册
POST   /api/v1/auth/login             # 用户登录
POST   /api/v1/auth/logout            # 用户登出
GET    /api/v1/auth/me                # 获取当前用户信息
PUT    /api/v1/auth/me                # 更新用户信息
POST   /api/v1/auth/change-password   # 修改密码
```

**分类管理**
```
GET    /api/v1/categories             # 获取分类列表
POST   /api/v1/categories             # 创建分类
GET    /api/v1/categories/{id}        # 获取分类详情
PUT    /api/v1/categories/{id}        # 更新分类
DELETE /api/v1/categories/{id}        # 删除分类
```

**账目管理**
```
GET    /api/v1/transactions           # 获取账目列表（支持分页、筛选）
POST   /api/v1/transactions           # 创建账目
GET    /api/v1/transactions/{id}      # 获取账目详情
PUT    /api/v1/transactions/{id}      # 更新账目
DELETE /api/v1/transactions/{id}      # 删除账目
```

**统计分析**
```
GET    /api/v1/statistics/overview    # 收支概览
GET    /api/v1/statistics/category    # 分类统计
GET    /api/v1/statistics/trend       # 趋势分析
GET    /api/v1/statistics/ranking     # 排行榜
```

**预算管理**（V2.0）
```
GET    /api/v1/budgets                # 获取预算列表
POST   /api/v1/budgets                # 创建预算
PUT    /api/v1/budgets/{id}           # 更新预算
DELETE /api/v1/budgets/{id}           # 删除预算
GET    /api/v1/budgets/progress       # 预算执行进度
```

#### API详细示例

**示例1：获取账目列表**
```http
GET /api/v1/transactions?page=1&size=20&type=expense&category_id=1&start_date=2025-12-01&end_date=2025-12-31
Authorization: Bearer <token>

Response:
{
  "code": 200,
  "message": "success",
  "data": {
    "total": 45,
    "page": 1,
    "size": 20,
    "items": [
      {
        "id": 1,
        "amount": 35.00,
        "type": "expense",
        "category": {
          "id": 1,
          "name": "餐饮",
          "icon": "🍜"
        },
        "transaction_date": "2025-12-07",
        "description": "午餐",
        "created_at": "2025-12-07T12:30:00"
      }
    ]
  }
}
```

**示例2：创建账目**
```http
POST /api/v1/transactions
Authorization: Bearer <token>
Content-Type: application/json

{
  "amount": 35.00,
  "type": "expense",
  "category_id": 1,
  "transaction_date": "2025-12-07",
  "description": "午餐"
}

Response:
{
  "code": 200,
  "message": "创建成功",
  "data": {
    "id": 1,
    "amount": 35.00,
    "type": "expense",
    "category_id": 1,
    "transaction_date": "2025-12-07",
    "description": "午餐",
    "created_at": "2025-12-07T12:30:00"
  }
}
```

**示例3：获取统计概览**
```http
GET /api/v1/statistics/overview?start_date=2025-12-01&end_date=2025-12-31
Authorization: Bearer <token>

Response:
{
  "code": 200,
  "message": "success",
  "data": {
    "income": 8000.00,
    "expense": 5200.00,
    "balance": 2800.00,
    "transaction_count": 45
  }
}
```

### 3.5 前端架构

#### 目录结构
```
frontend/
├── public/
│   ├── index.html
│   └── favicon.ico
├── src/
│   ├── assets/              # 静态资源
│   │   ├── images/
│   │   └── styles/
│   ├── components/          # 通用组件
│   │   ├── Layout/
│   │   │   ├── Header.tsx
│   │   │   ├── Sidebar.tsx
│   │   │   └── Layout.tsx
│   │   ├── Charts/
│   │   │   ├── PieChart.tsx
│   │   │   └── LineChart.tsx
│   │   └── Common/
│   │       ├── Button.tsx
│   │       └── Input.tsx
│   ├── pages/               # 页面组件
│   │   ├── Login/
│   │   ├── Register/
│   │   ├── Dashboard/
│   │   ├── Transactions/
│   │   │   ├── List.tsx
│   │   │   ├── Create.tsx
│   │   │   └── Edit.tsx
│   │   ├── Statistics/
│   │   ├── Categories/
│   │   └── Settings/
│   ├── store/               # 状态管理
│   │   ├── authStore.ts
│   │   ├── transactionStore.ts
│   │   └── categoryStore.ts
│   ├── services/            # API服务
│   │   ├── api.ts           # Axios配置
│   │   ├── auth.ts
│   │   ├── transaction.ts
│   │   └── category.ts
│   ├── types/               # TypeScript类型定义
│   │   ├── user.ts
│   │   ├── transaction.ts
│   │   └── category.ts
│   ├── utils/               # 工具函数
│   │   ├── format.ts        # 格式化工具
│   │   ├── validate.ts      # 验证工具
│   │   └── constants.ts     # 常量定义
│   ├── routes/              # 路由配置
│   │   └── index.tsx
│   ├── App.tsx
│   └── main.tsx
├── package.json
├── tsconfig.json
├── vite.config.ts
└── .env
```

#### 状态管理（Zustand示例）
```typescript
// store/authStore.ts
import { create } from 'zustand';

interface AuthState {
  user: User | null;
  token: string | null;
  login: (username: string, password: string) => Promise<void>;
  logout: () => void;
}

export const useAuthStore = create<AuthState>((set) => ({
  user: null,
  token: localStorage.getItem('token'),
  login: async (username, password) => {
    const response = await authAPI.login(username, password);
    localStorage.setItem('token', response.token);
    set({ user: response.user, token: response.token });
  },
  logout: () => {
    localStorage.removeItem('token');
    set({ user: null, token: null });
  },
}));
```

### 3.6 后端架构

#### 目录结构
```
backend/
├── app/
│   ├── api/                 # API路由
│   │   ├── v1/
│   │   │   ├── __init__.py
│   │   │   ├── auth.py
│   │   │   ├── categories.py
│   │   │   ├── transactions.py
│   │   │   └── statistics.py
│   │   └── deps.py          # 依赖项（如获取当前用户）
│   ├── core/                # 核心配置
│   │   ├── config.py        # 配置管理
│   │   ├── security.py      # 安全相关（JWT、密码加密）
│   │   └── database.py      # 数据库连接
│   ├── models/              # SQLAlchemy模型
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── category.py
│   │   ├── transaction.py
│   │   └── budget.py
│   ├── schemas/             # Pydantic模型（请求/响应）
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── category.py
│   │   ├── transaction.py
│   │   └── common.py
│   ├── crud/                # CRUD操作
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── category.py
│   │   └── transaction.py
│   ├── services/            # 业务逻辑
│   │   ├── __init__.py
│   │   ├── auth_service.py
│   │   └── statistics_service.py
│   ├── utils/               # 工具函数
│   │   └── helpers.py
│   └── main.py              # 应用入口
├── alembic/                 # 数据库迁移
│   ├── versions/
│   └── env.py
├── tests/                   # 测试
│   ├── api/
│   └── services/
├── requirements.txt
├── .env
├── .env.example
└── alembic.ini
```

#### FastAPI应用结构示例
```python
# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1 import auth, categories, transactions, statistics
from app.core.config import settings

app = FastAPI(
    title="记账本API",
    description="个人财务管理系统",
    version="1.0.0"
)

# CORS配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite默认端口
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册路由
app.include_router(auth.router, prefix="/api/v1/auth", tags=["认证"])
app.include_router(categories.router, prefix="/api/v1/categories", tags=["分类"])
app.include_router(transactions.router, prefix="/api/v1/transactions", tags=["账目"])
app.include_router(statistics.router, prefix="/api/v1/statistics", tags=["统计"])

@app.get("/")
def read_root():
    return {"message": "记账本API服务运行中"}
```

### 3.7 安全设计

#### 认证流程
1. 用户登录 → 后端验证用户名密码
2. 验证成功 → 生成JWT Token（包含user_id、过期时间）
3. 前端存储Token → localStorage
4. 后续请求 → 请求头携带`Authorization: Bearer <token>`
5. 后端验证Token → 解析user_id → 执行业务逻辑

#### 密码安全
- 使用`passlib`的`bcrypt`算法加密密码
- 密码强度要求：至少8位，包含字母和数字

#### API安全
- 所有API（除登录注册）都需要JWT认证
- 请求频率限制（防止暴力破解）
- SQL注入防护（使用ORM参数化查询）
- XSS防护（前端输入过滤）

### 3.8 部署方案

#### 开发环境
```
前端：npm run dev (Vite开发服务器，端口5173)
后端：uvicorn app.main:app --reload (端口8000)
数据库：本地PostgreSQL/MySQL
```

#### 生产环境（示例）
```
服务器：阿里云/腾讯云 ECS
前端：Nginx托管静态文件
后端：Gunicorn + Uvicorn Workers
数据库：云数据库RDS
HTTPS：Let's Encrypt证书
域名：example.com

架构：
   用户
    ↓
  Nginx (443) ← HTTPS
    ↓
  ├─ 静态文件 (前端)
  └─ 反向代理 (/api) → Gunicorn (8000) → FastAPI
                          ↓
                      PostgreSQL (5432)
```

#### Docker部署（推荐）
```yaml
# docker-compose.yml
version: '3.8'

services:
  db:
    image: postgres:15
    environment:
      POSTGRES_DB: accountbook
      POSTGRES_USER: admin
      POSTGRES_PASSWORD: password
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  backend:
    build: ./backend
    command: uvicorn app.main:app --host 0.0.0.0 --port 8000
    volumes:
      - ./backend:/app
    ports:
      - "8000:8000"
    depends_on:
      - db
    environment:
      DATABASE_URL: postgresql://admin:password@db:5432/accountbook

  frontend:
    build: ./frontend
    ports:
      - "80:80"
    depends_on:
      - backend

volumes:
  postgres_data:
```

---

## 📊 四、开发计划

### 4.1 MVP版本（2-3周）

**第一周：基础架构 + 用户认证**
- Day 1-2：项目初始化、环境搭建、数据库设计
- Day 3-4：后端用户注册/登录API
- Day 5-6：前端登录注册页面
- Day 7：JWT认证中间件、路由守卫

**第二周：核心功能 - 记账**
- Day 8-9：后端分类管理API、账目管理API
- Day 10-11：前端快速记账页面
- Day 12-13：前端账目列表页面
- Day 14：分类管理页面

**第三周：统计分析 + 优化**
- Day 15-16：后端统计API（收支概览、分类统计、趋势分析）
- Day 17-18：前端Dashboard页面、图表集成
- Day 19-20：前端统计分析页面
- Day 21：测试、Bug修复、优化

### 4.2 V2.0版本（2周）
- 预算管理功能
- 多账户支持
- 数据导出功能
- 移动端优化

---

## 🔧 五、技术难点与解决方案

### 5.1 高性能查询
**问题**：统计查询涉及大量数据聚合
**解决方案**：
- 使用数据库索引优化查询
- 复杂统计使用数据库视图
- 考虑使用Redis缓存热点数据（V2.0）

### 5.2 日期时区处理
**问题**：前后端日期格式不一致
**解决方案**：
- 后端统一使用UTC时间存储
- 前端根据用户时区显示
- API传输使用ISO 8601格式

### 5.3 前端状态管理
**问题**：多页面共享状态（如用户信息、分类列表）
**解决方案**：
- 使用Zustand全局状态管理
- 关键数据本地缓存（localStorage）
- 页面间通信使用事件总线

### 5.4 数据可视化性能
**问题**：大量数据渲染卡顿
**解决方案**：
- 图表按需加载
- 数据分页加载
- 使用虚拟滚动（react-window）

---

## 📝 六、待确认问题

在开始开发前，请确认以下问题：

1. **数据库选择**：PostgreSQL 还是 MySQL？（推荐PostgreSQL）
2. **UI组件库**：Ant Design 还是 Material-UI？（推荐Ant Design）
3. **图表库**：ECharts 还是 Recharts？（推荐ECharts）
4. **是否需要多用户支持**：当前设计支持多用户独立数据
5. **是否需要移动端App**：当前设计为响应式Web，后续可考虑React Native
6. **部署方式**：本地部署、云服务器、Docker？

---

## 🎯 七、成功指标

### 功能指标
- ✅ 用户可以在30秒内完成一笔记账
- ✅ 支持至少10个分类
- ✅ 统计页面加载时间 < 2秒
- ✅ 移动端适配良好

### 技术指标
- ✅ API响应时间 < 200ms（P95）
- ✅ 前端首屏加载时间 < 3秒
- ✅ 代码测试覆盖率 > 70%
- ✅ 零重大安全漏洞

---

## 📚 八、参考资料

### 文档
- FastAPI官方文档：https://fastapi.tiangolo.com/
- React官方文档：https://react.dev/
- Ant Design文档：https://ant.design/
- SQLAlchemy文档：https://docs.sqlalchemy.org/

### 类似产品
- 随手记
- 钱迹
- MoneyWiz

---

**文档版本**：v1.0  
**创建日期**：2025-12-07  
**最后更新**：2025-12-07  
**维护者**：开发团队

