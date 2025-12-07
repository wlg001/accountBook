# 数据库模型设计文档

## 📊 ER图（实体关系图）

```
┌─────────────────┐
│     Users       │
│   (用户表)      │
├─────────────────┤
│ PK id           │
│ UK username     │
│ UK email        │
│    hashed_pwd   │
│    nickname     │
│    avatar_url   │
│    is_active    │
│    created_at   │
│    updated_at   │
└────────┬────────┘
         │
         │ 1:N (一个用户有多个分类)
         │
         ├──────────────────┐
         │                  │
         ▼                  ▼
┌─────────────────┐  ┌─────────────────┐
│   Categories    │  │  Transactions   │
│   (分类表)      │  │   (账目表)      │
├─────────────────┤  ├─────────────────┤
│ PK id           │  │ PK id           │
│ FK user_id      │  │ FK user_id      │
│    name         │  │ FK category_id  │
│    type         │  │    amount       │
│    icon         │  │    type         │
│    color        │  │    trans_date   │
│    is_system    │  │    description  │
│    sort_order   │  │    tags         │
│    created_at   │  │    account_type │
└────────┬────────┘  │    created_at   │
         │           │    updated_at   │
         │           └─────────────────┘
         │ 1:N
         │ (一个分类有多个账目)
         │
         └───────────────┐
                         │
                         ▼
                  ┌─────────────────┐
                  │    Budgets      │
                  │   (预算表)      │
                  ├─────────────────┤
                  │ PK id           │
                  │ FK user_id      │
                  │ FK category_id  │
                  │    amount       │
                  │    period_type  │
                  │    start_date   │
                  │    end_date     │
                  │    created_at   │
                  └─────────────────┘
```

**关系说明**：
- User → Categories: 1对多（一个用户有多个分类）
- User → Transactions: 1对多（一个用户有多个账目）
- User → Budgets: 1对多（一个用户有多个预算）
- Category → Transactions: 1对多（一个分类有多个账目）
- Category → Budgets: 1对多（一个分类有多个预算）

## 📋 表结构详解

### 1. users（用户表）

**用途**：存储用户基本信息和认证信息

| 字段名 | 类型 | 约束 | 说明 |
|--------|------|------|------|
| id | Integer | PK, Index | 主键，用户ID |
| username | String(50) | Unique, Index, Not Null | 用户名（唯一） |
| email | String(100) | Unique, Index, Not Null | 邮箱（唯一） |
| hashed_password | String(255) | Not Null | 密码哈希值 |
| nickname | String(50) | Nullable | 昵称 |
| avatar_url | String(255) | Nullable | 头像URL |
| is_active | Boolean | Not Null, Default=True | 是否激活 |
| created_at | DateTime | Not Null, Auto | 创建时间 |
| updated_at | DateTime | Auto | 更新时间 |

**索引**：
- 主键索引：id
- 唯一索引：username, email

**业务规则**：
- username和email必须唯一
- 密码使用bcrypt加密存储
- 删除用户时级联删除所有关联数据

---

### 2. categories（分类表）

**用途**：存储收入和支出的分类信息

| 字段名 | 类型 | 约束 | 说明 |
|--------|------|------|------|
| id | Integer | PK, Index | 主键，分类ID |
| user_id | Integer | FK, Index, Nullable | 用户ID（系统分类为NULL） |
| name | String(50) | Not Null | 分类名称 |
| type | String(10) | Not Null, Index | 类型（income/expense） |
| icon | String(50) | Nullable | 图标（Emoji） |
| color | String(20) | Nullable | 颜色代码 |
| is_system | Boolean | Not Null, Default=False | 是否系统预设 |
| sort_order | Integer | Default=0 | 排序顺序 |
| created_at | DateTime | Not Null, Auto | 创建时间 |

**外键**：
- user_id → users.id (CASCADE)

**索引**：
- 主键索引：id
- 外键索引：user_id
- 普通索引：type

**业务规则**：
- type只能是'income'或'expense'
- 系统预设分类user_id为NULL
- 用户注册时复制系统分类到用户账户
- 删除分类时，关联账目的category_id设为NULL

**预设分类示例**：
```python
支出分类：
- 🍜 餐饮
- 🚌 交通
- 🛍️ 购物
- 🎬 娱乐
- 🏥 医疗
- 📚 教育
- 🏠 住房
- 📦 其他

收入分类：
- 💰 工资
- 🎁 奖金
- 📈 投资
- 💼 兼职
- 💵 其他
```

---

### 3. transactions（账目表）

**用途**：存储用户的收入和支出记录

| 字段名 | 类型 | 约束 | 说明 |
|--------|------|------|------|
| id | Integer | PK, Index | 主键，账目ID |
| user_id | Integer | FK, Index, Not Null | 用户ID |
| category_id | Integer | FK, Index, Nullable | 分类ID |
| amount | Numeric(12,2) | Not Null | 金额 |
| type | String(10) | Not Null, Index | 类型（income/expense） |
| transaction_date | Date | Not Null, Index | 账目日期 |
| description | Text | Nullable | 备注说明 |
| tags | String(255) | Nullable | 标签（逗号分隔） |
| account_type | String(50) | Nullable | 账户类型（V2.0） |
| created_at | DateTime | Not Null, Auto | 创建时间 |
| updated_at | DateTime | Auto | 更新时间 |

**外键**：
- user_id → users.id (CASCADE)
- category_id → categories.id (SET NULL)

**索引**：
- 主键索引：id
- 外键索引：user_id, category_id
- 普通索引：type, transaction_date
- 复合索引：(user_id, transaction_date)
- 复合索引：(user_id, type)

**业务规则**：
- amount精确到分（小数点后2位）
- type只能是'income'或'expense'
- 删除分类时，账目保留但category_id设为NULL
- transaction_date可以是过去或未来的日期

**复合索引说明**：
```sql
-- 常用查询1：查询用户某个时间段的账目
SELECT * FROM transactions 
WHERE user_id = ? AND transaction_date BETWEEN ? AND ?;

-- 常用查询2：查询用户的收入或支出
SELECT * FROM transactions 
WHERE user_id = ? AND type = ?;
```

---

### 4. budgets（预算表）- V2.0

**用途**：存储用户的预算设置

| 字段名 | 类型 | 约束 | 说明 |
|--------|------|------|------|
| id | Integer | PK, Index | 主键，预算ID |
| user_id | Integer | FK, Index, Not Null | 用户ID |
| category_id | Integer | FK, Index, Nullable | 分类ID（NULL=总预算） |
| amount | Numeric(12,2) | Not Null | 预算金额 |
| period_type | String(20) | Not Null | 周期（monthly/yearly） |
| start_date | Date | Not Null | 开始日期 |
| end_date | Date | Not Null | 结束日期 |
| created_at | DateTime | Not Null, Auto | 创建时间 |

**外键**：
- user_id → users.id (CASCADE)
- category_id → categories.id (CASCADE)

**索引**：
- 主键索引：id
- 外键索引：user_id, category_id
- 复合索引：(user_id, start_date, end_date)

**业务规则**：
- category_id为NULL表示总预算
- period_type只能是'monthly'或'yearly'
- 同一用户同一分类同一时间段只能有一个预算

---

## 🔗 关系详解

### 1. User与Category（一对多）

```python
# User模型中
categories = relationship(
    "Category",
    back_populates="user",
    cascade="all, delete-orphan"
)

# Category模型中
user = relationship("User", back_populates="categories")
```

**cascade说明**：
- `all`: 所有操作都级联
- `delete-orphan`: 删除孤儿记录

**效果**：
- 删除用户 → 自动删除该用户的所有分类

### 2. User与Transaction（一对多）

```python
# User模型中
transactions = relationship(
    "Transaction",
    back_populates="user",
    cascade="all, delete-orphan"
)

# Transaction模型中
user = relationship("User", back_populates="transactions")
```

**效果**：
- 删除用户 → 自动删除该用户的所有账目

### 3. Category与Transaction（一对多）

```python
# Category模型中
transactions = relationship(
    "Transaction",
    back_populates="category",
    cascade="all, delete-orphan"
)

# Transaction模型中
category = relationship("Category", back_populates="transactions")
```

**注意**：
- 外键定义为 `ondelete="SET NULL"`
- 删除分类 → 账目保留，但category_id设为NULL
- 这样可以保留历史数据

---

## 💾 字段类型说明

### SQLAlchemy类型 vs 数据库类型

| SQLAlchemy类型 | SQLite类型 | PostgreSQL类型 | 说明 |
|----------------|-----------|---------------|------|
| Integer | INTEGER | INTEGER | 整数 |
| String(N) | VARCHAR(N) | VARCHAR(N) | 可变长字符串 |
| Text | TEXT | TEXT | 长文本 |
| Boolean | INTEGER | BOOLEAN | 布尔值（SQLite用0/1） |
| Numeric(M,D) | DECIMAL(M,D) | NUMERIC(M,D) | 精确数字 |
| Date | DATE | DATE | 日期 |
| DateTime | DATETIME | TIMESTAMP | 日期时间 |

### Numeric vs Float

**为什么使用Numeric(12,2)而不是Float？**

```python
# ❌ 错误：Float有精度问题
amount = Column(Float)  # 可能：100.30 → 100.29999999

# ✅ 正确：Numeric精确存储
amount = Column(Numeric(12, 2))  # 精确：100.30
```

**金额字段必须使用Numeric**：
- Numeric(12, 2)：总共12位，小数点后2位
- 最大值：9,999,999,999.99（99亿）
- 最小值：0.01（1分）

---

## 🔐 约束说明

### 1. 主键约束（Primary Key）

```python
id = Column(Integer, primary_key=True, index=True)
```

- 唯一标识每条记录
- 自动创建索引
- 不能为NULL

### 2. 唯一约束（Unique）

```python
username = Column(String(50), unique=True)
```

- 值必须唯一
- 自动创建唯一索引

### 3. 非空约束（Not Null）

```python
email = Column(String(100), nullable=False)
```

- 值不能为NULL
- nullable=False 等同于 NOT NULL

### 4. 外键约束（Foreign Key）

```python
user_id = Column(
    Integer,
    ForeignKey("users.id", ondelete="CASCADE")
)
```

- 引用另一个表的主键
- `ondelete`选项：
  - CASCADE: 级联删除
  - SET NULL: 设为NULL
  - RESTRICT: 禁止删除（默认）

### 5. 默认值约束（Default）

```python
is_active = Column(Boolean, default=True)
created_at = Column(DateTime, server_default=func.now())
```

- `default`: Python层面默认值
- `server_default`: 数据库层面默认值

---

## 📈 索引策略

### 何时创建索引？

1. **主键** - 自动索引 ✅
2. **外键** - 建议索引 ✅
3. **唯一字段** - 自动索引 ✅
4. **频繁查询字段** - 建议索引 ✅
5. **频繁排序字段** - 建议索引 ✅

### 复合索引

**场景**：经常一起查询的字段

```python
__table_args__ = (
    Index('idx_user_date', 'user_id', 'transaction_date'),
)
```

**适用查询**：
```sql
-- ✅ 使用复合索引
WHERE user_id = ? AND transaction_date = ?
WHERE user_id = ?

-- ❌ 不使用复合索引
WHERE transaction_date = ?
```

**索引顺序规则**：
- 最常用的字段放前面
- 区分度高的字段放前面

---

## 🎯 最佳实践

### 1. 时间戳字段

```python
created_at = Column(
    DateTime(timezone=True),      # 带时区
    server_default=func.now(),    # 数据库层面默认值
    nullable=False
)

updated_at = Column(
    DateTime(timezone=True),
    server_default=func.now(),
    onupdate=func.now()           # 更新时自动更新
)
```

### 2. 软删除（可选）

```python
# 如果需要软删除功能
is_deleted = Column(Boolean, default=False)
deleted_at = Column(DateTime, nullable=True)
```

### 3. 字段注释

```python
amount = Column(
    Numeric(12, 2),
    nullable=False,
    comment="金额"  # 添加注释
)
```

### 4. 关系命名

```python
# ✅ 好的命名（复数）
user.transactions  # 一个用户的多个账目

# ❌ 不好的命名
user.transaction  # 容易混淆
```

---

## 🧪 模型验证

### 测试创建记录

```python
from app.models import User, Category, Transaction

# 创建用户
user = User(
    username="testuser",
    email="test@example.com",
    hashed_password="hashed_pwd"
)

# 创建分类
category = Category(
    user_id=user.id,
    name="餐饮",
    type="expense",
    icon="🍜"
)

# 创建账目
transaction = Transaction(
    user_id=user.id,
    category_id=category.id,
    amount=35.50,
    type="expense",
    transaction_date="2025-12-07"
)
```

---

## 📚 参考资料

- [SQLAlchemy官方文档](https://docs.sqlalchemy.org/)
- [SQLAlchemy关系模式](https://docs.sqlalchemy.org/en/14/orm/relationships.html)
- [数据库设计规范](https://www.postgresql.org/docs/current/ddl.html)

