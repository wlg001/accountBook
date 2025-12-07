#!/bin/bash
# 前端服务启动脚本

echo "🚀 启动记账本前端服务..."

# 进入脚本所在目录
cd "$(dirname "$0")"

# 检查node_modules是否存在
if [ ! -d "node_modules" ]; then
    echo "❌ 依赖未安装，正在安装..."
    npm install
fi

# 检查.env文件
if [ ! -f ".env" ]; then
    echo "⚠️  .env文件不存在，从.env.example复制..."
    cp .env.example .env
fi

# 启动服务
echo "✓ 启动Vite开发服务器"
echo "📱 访问地址: http://localhost:5173"
echo ""
npm run dev

