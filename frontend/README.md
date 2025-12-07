# 记账本前端 (React + TypeScript + Vite)

## 快速开始

### 1. 安装依赖

```bash
npm install
```

### 2. 配置环境变量

```bash
cp .env.example .env
# 根据需要修改 .env 文件中的配置
```

### 3. 启动开发服务器

```bash
npm run dev
```

访问: http://localhost:5173

### 4. 构建生产版本

```bash
npm run build
```

### 5. 预览生产构建

```bash
npm run preview
```

## 项目结构

```
frontend/
├── src/
│   ├── assets/           # 静态资源
│   │   ├── images/       # 图片
│   │   └── styles/       # 样式
│   ├── components/       # 通用组件
│   │   ├── Layout/       # 布局组件
│   │   ├── Charts/       # 图表组件
│   │   └── Common/       # 通用组件
│   ├── pages/            # 页面组件
│   │   ├── Login/        # 登录页
│   │   ├── Register/     # 注册页
│   │   ├── Dashboard/    # 仪表盘
│   │   ├── Transactions/ # 账目管理
│   │   ├── Statistics/   # 统计分析
│   │   ├── Categories/   # 分类管理
│   │   └── Settings/     # 设置
│   ├── store/            # 状态管理 (Zustand)
│   ├── services/         # API服务
│   │   └── api.ts        # Axios配置
│   ├── types/            # TypeScript类型定义
│   ├── utils/            # 工具函数
│   │   └── constants.ts  # 常量定义
│   ├── routes/           # 路由配置
│   ├── App.tsx           # 根组件
│   ├── main.tsx          # 入口文件
│   └── vite-env.d.ts     # Vite类型声明
├── public/               # 公共资源
├── .env                  # 环境变量（不提交到Git）
├── .env.example          # 环境变量示例
├── .prettierrc           # Prettier配置
├── eslint.config.js      # ESLint配置
├── tsconfig.json         # TypeScript配置
├── vite.config.ts        # Vite配置
└── package.json          # 依赖配置
```

## 技术栈

### 核心框架
- **React 18.2+** - UI框架
- **TypeScript 5+** - 类型安全
- **Vite** - 构建工具

### UI组件库
- **Ant Design 5+** - 企业级UI组件
- **ECharts** - 数据可视化

### 状态管理
- **Zustand** - 轻量级状态管理

### 路由
- **React Router 6+** - 路由管理

### HTTP客户端
- **Axios** - HTTP请求

### 工具库
- **dayjs** - 日期处理

## 开发命令

```bash
# 安装依赖
npm install

# 启动开发服务器
npm run dev

# 构建生产版本
npm run build

# 预览生产构建
npm run preview

# 代码检查
npm run lint

# 代码格式化
npm run format
```

## 环境变量

在 `.env` 文件中配置以下变量：

```env
# API基础URL
VITE_API_BASE_URL=http://localhost:8000/api/v1

# 应用信息
VITE_APP_TITLE=记账本
VITE_APP_VERSION=1.0.0

# 环境
VITE_ENVIRONMENT=development
```

## 代码规范

- 使用 ESLint 进行代码检查
- 使用 Prettier 进行代码格式化
- 组件使用函数式组件 + Hooks
- 优先使用 TypeScript 类型定义
- 遵循 Ant Design 设计规范

## 浏览器支持

- Chrome >= 90
- Firefox >= 88
- Safari >= 14
- Edge >= 90

## 注意事项

1. 确保后端API服务已启动（默认端口8000）
2. 开发时自动代理API请求到后端
3. 生产环境需要配置Nginx代理
