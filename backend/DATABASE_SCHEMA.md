# 数据库设计文档

## 📊 ER图（实体关系图）

```
┌─────────────────┐
│     Users       │
│  (用户表)        │
├─────────────────┤
│ PK  id          │
│ UK  username    │
│ UK  email       │
│     password    │
│     nickname    │
│     avatar_url  │
│     is_active   │
│     created_at  │
│     updated_at  │
└────────┬────────┘
         │
         │ 1:N (一对多)
         ├──────────────────────────┐
         │                          │
         │                          │
┌────────▼────────┐        ┌───────▼─────────┐
│   Categories    │        │  Transactions   │
│   (分类表)       │        │   (账目表)       │
├─────────────────┤        ├─────────────────┤
│ PK  id          │        │ PK  id          │
│ FK  user_id     │◄───┐   │ FK  user_id     │
│     name        │    │   │ FK  category_id │───┐
│     type        │    │   │     amount      │   │
│     icon        │    │   │     type        │   │
│     color       │    │   │     date        │   │
│     is_system   │    │   │     description │   │
│     sort_order  │    │   │     tags        │   │
│     created_at  │    │   │     account_type│   │
└────────┬────────┘    │   │     created_at  │   │
         │             │   │     updated_at  │   │
         │ 1:N         │   └─────────────────┘   │
         │             │            │             │
         │             └────────────┘             │
         │                   N:1                  │
         │                                        │
         │ 1:N (预算功能，V2.0)                    │
         │                                        │
┌────────▼────────┐                              │
│    Budgets      │                              │
│   (预算表)       │                              │
├─────────────────┤                              │
│ PK  id          │                              │
│ FK  user_id     │──────────────────────────────┘
│ FK  category_id │
│     amount      │
│     period_type │
│     start_date  │
│     end_date    │
│     created_at  │
└─────────────────┘
```

## 📋 表结构详解

### 1. users（用户表）

**用途**: 存储用户账户信息

| 字段名 | 类型 | 约束 | 说明 |
|--------|------|------|------|
| id | INTEGER | PK, AUTO_INCREMENT | 用户ID（主键） |
| username | VARCHAR(50) | UNIQUE, NOT NULL | 用户名（登录用） |
| email | VARCHAR(100) | UNIQUE, NOT NULL | 邮箱 |
| hashed_password | VARCHAR(255) | NOT NULL | 加密后的密码 |
| nickname | VARCHAR(50) | NULL | 昵称 |
| avatar_url | VARCHAR(255) | NULL | 头像URL |
| is_active | BOOLEAN | NOT NULL, DEFAULT TRUE | 账户是否激活 |
| created_at | DATETIME | NOT NULL | 创建时间 |
| updated_at | DATETIME | NOT NULL | 更新时间 |

**索引**:
- PRIMARY KEY: `id`
- UNIQUE INDEX: `username`
- UNIQUE INDEX: `email`

**关系**:
- 一个用户可以有多个分类（1:N）
- 一个用户可以有多个账目（1:N）
- 一个用户可以有多个预算（1:N）

---

### 2. categories（分类表）

**用途**: 存储收支分类（如餐饮、交通等）

| 字段名 | 类型 | 约束 | 说明 |
|--------|------|------|------|
| id | INTEGER | PK, AUTO_INCREMENT | 分类ID（主键） |
| user_id | INTEGER | FK, NULL | 用户ID（NULL=系统分类） |
| name | VARCHAR(50) | NOT NULL | 分类名称 |
| type | VARCHAR(10) | NOT NULL | income/expense |
| icon | VARCHAR(50) | NULL | 图标（Emoji或图标名） |
| color | VARCHAR(20) | NULL | 颜色代码（#FF0000） |
| is_system | BOOLEAN | NOT NULL, DEFAULT FALSE | 是否系统预设 |
| sort_order | INTEGER | NOT NULL, DEFAULT 0 | 排序顺序 |
| created_at | DATETIME | NOT NULL | 创建时间 |

**索引**:
- PRIMARY KEY: `id`
- INDEX: `user_id`
- INDEX: `type`
- UNIQUE INDEX: `(user_id, name, type)` - 同一用户不能有重名的同类型分类

**关系**:
- 属于一个用户（N:1）
- 一个分类可以有多个账目（1:N）
- 一个分类可以有多个预算（1:N）

**外键**:
- `user_id` → `users.id` (ON DELETE CASCADE)

**业务规则**:
- `user_id` 为 NULL 表示系统预设分类
- `type` 只能是 'income' 或 'expense'
- 同一用户的同类型分类名称不能重复

---

### 3. transactions（账目表）

**用途**: 存储用户的收支记录

| 字段名 | 类型 | 约束 | 说明 |
|--------|------|------|------|
| id | INTEGER | PK, AUTO_INCREMENT | 账目ID（主键） |
| user_id | INTEGER | FK, NOT NULL | 用户ID |
| category_id | INTEGER | FK, NULL | 分类ID |
| amount | DECIMAL(12,2) | NOT NULL | 金额（精确到分） |
| type | VARCHAR(10) | NOT NULL | income/expense |
| transaction_date | DATE | NOT NULL | 账目日期 |
| description | TEXT | NULL | 备注说明 |
| tags | VARCHAR(255) | NULL | 标签（逗号分隔） |
| account_type | VARCHAR(50) | NULL | 账户类型（V2.0） |
| created_at | DATETIME | NOT NULL | 创建时间 |
| updated_at | DATETIME | NOT NULL | 更新时间 |

**索引**:
- PRIMARY KEY: `id`
- INDEX: `user_id`
- INDEX: `category_id`
- INDEX: `type`
- INDEX: `transaction_date`
- COMPOSITE INDEX: `(user_id, transaction_date)` - 常用查询组合
- COMPOSITE INDEX: `(user_id, type)` - 常用筛选组合
- COMPOSITE INDEX: `(user_id, category_id)` - 常用筛选组合

**关系**:
- 属于一个用户（N:1）
- 属于一个分类（N:1）

**外键**:
- `user_id` → `users.id` (ON DELETE CASCADE)
- `category_id` → `categories.id` (ON DELETE SET NULL)

**业务规则**:
- `amount` 精确到小数点后2位（分）
- `type` 只能是 'income' 或 'expense'
- `transaction_date` 是记账日期，不是创建日期
- 分类被删除时，`category_id` 设为 NULL（保留账目记录）

---

### 4. budgets（预算表）- V2.0

**用途**: 存储用户的预算设置

| 字段名 | 类型 | 约束 | 说明 |
|--------|------|------|------|
| id | INTEGER | PK, AUTO_INCREMENT | 预算ID（主键） |
| user_id | INTEGER | FK, NOT NULL | 用户ID |
| category_id | INTEGER | FK, NULL | 分类ID（NULL=总预算） |
| amount | DECIMAL(12,2) | NOT NULL | 预算金额 |
| period_type | VARCHAR(20) | NOT NULL | monthly/yearly |
| start_date | DATE | NOT NULL | 开始日期 |
| end_date | DATE | NOT NULL | 结束日期 |
| created_at | DATETIME | NOT NULL | 创建时间 |

**索引**:
- PRIMARY KEY: `id`
- INDEX: `user_id`
- INDEX: `category_id`
- UNIQUE INDEX: `(user_id, category_id, start_date)` - 同一分类同一时期唯一
- COMPOSITE INDEX: `(user_id, start_date, end_date)` - 常用查询

**关系**:
- 属于一个用户（N:1）
- 属于一个分类（N:1）

**外键**:
- `user_id` → `users.id` (ON DELETE CASCADE)
- `category_id` → `categories.id` (ON DELETE CASCADE)

**业务规则**:
- `category_id` 为 NULL 表示总预算
- `period_type` 只能是 'monthly' 或 'yearly'
- 同一用户的同一分类在同一时间段只能有一个预算

---

## 🔗 表关系说明

### 用户与分类（1:N）
- 一个用户可以创建多个分类
- 删除用户时，级联删除其所有分类

### 用户与账目（1:N）
- 一个用户可以有多条账目记录
- 删除用户时，级联删除其所有账目

### 分类与账目（1:N）
- 一个分类可以包含多条账目
- 删除分类时，账目的 `category_id` 设为 NULL（保留账目）

### 用户与预算（1:N）- V2.0
- 一个用户可以设置多个预算
- 删除用户时，级联删除其所有预算

### 分类与预算（1:N）- V2.0
- 一个分类可以有多个预算（不同时间段）
- 删除分类时，级联删除其预算

---

## 📐 设计原则

### 1. 数据完整性
- **主键**: 每个表都有自增主键
- **外键**: 正确设置外键关系和级联规则
- **唯一约束**: 防止重复数据（用户名、邮箱等）
- **非空约束**: 确保关键字段不为空

### 2. 索引优化
- **单列索引**: 经常查询的字段（user_id、type、date）
- **组合索引**: 常用查询组合（user_id + date）
- **唯一索引**: 业务唯一性约束

### 3. 数据类型选择
- **金额**: DECIMAL(12,2) - 精确到分，避免浮点误差
- **日期**: DATE - 账目日期
- **时间戳**: DATETIME - 记录创建/更新时间
- **文本**: VARCHAR vs TEXT - 根据长度选择

### 4. 级联操作
- **CASCADE**: 删除用户时删除其数据
- **SET NULL**: 删除分类时保留账目记录
- **RESTRICT**: 防止误删除

### 5. 软删除 vs 硬删除
- **用户**: 使用 `is_active` 标记（软删除）
- **账目**: 硬删除（可以彻底删除）
- **分类**: 硬删除，但账目保留（SET NULL）

---

## 🔍 常用查询场景

### 1. 获取用户本月账目
```sql
SELECT * FROM transactions
WHERE user_id = ? 
  AND transaction_date >= '2025-12-01'
  AND transaction_date < '2026-01-01'
ORDER BY transaction_date DESC;
```
**使用索引**: `idx_transaction_user_date`

### 2. 按分类统计支出
```sql
SELECT 
    c.name,
    SUM(t.amount) as total
FROM transactions t
JOIN categories c ON t.category_id = c.id
WHERE t.user_id = ?
  AND t.type = 'expense'
  AND t.transaction_date >= '2025-12-01'
GROUP BY c.id, c.name
ORDER BY total DESC;
```
**使用索引**: `idx_transaction_user_category`, `idx_transaction_user_date`

### 3. 获取用户的收支概览
```sql
SELECT 
    type,
    SUM(amount) as total,
    COUNT(*) as count
FROM transactions
WHERE user_id = ?
  AND transaction_date >= '2025-12-01'
  AND transaction_date < '2026-01-01'
GROUP BY type;
```
**使用索引**: `idx_transaction_user_type`, `idx_transaction_user_date`

---

## 📊 数据示例

### Users
```
id | username | email           | nickname | is_active
---+----------+-----------------+----------+----------
1  | zhangsan | zhang@email.com | 张三     | true
2  | lisi     | li@email.com    | 李四     | true
```

### Categories
```
id | user_id | name   | type    | icon | color   | is_system
---+---------+--------+---------+------+---------+-----------
1  | NULL    | 餐饮   | expense | 🍜   | #FF6B6B | true
2  | NULL    | 交通   | expense | 🚌   | #4ECDC4 | true
3  | 1       | 零食   | expense | 🍿   | #FFE66D | false
```

### Transactions
```
id | user_id | category_id | amount | type    | date       | description
---+---------+-------------+--------+---------+------------+-------------
1  | 1       | 1           | 35.00  | expense | 2025-12-07 | 午餐
2  | 1       | 2           | 4.00   | expense | 2025-12-07 | 地铁
3  | 1       | NULL        | 8000.00| income  | 2025-12-05 | 工资
```

---

## 🚀 未来扩展

### V2.0 可能的扩展

1. **账户表（accounts）**
   - 支持多账户管理
   - 账户余额追踪
   - 账户间转账

2. **定期账目表（recurring_transactions）**
   - 定期收支模板
   - 自动记账

3. **标签表（tags）**
   - 独立的标签管理
   - 多对多关系

4. **附件表（attachments）**
   - 票据照片
   - 文件上传

---

**文档版本**: v1.0  
**创建日期**: 2025-12-07  
**最后更新**: 2025-12-07  
**维护者**: 开发团队

