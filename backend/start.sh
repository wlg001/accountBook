#!/bin/bash
# 后端服务启动脚本

echo "🚀 启动记账本后端服务..."

# 进入脚本所在目录
cd "$(dirname "$0")"

# 激活虚拟环境
if [ -d "venv" ]; then
    echo "✓ 激活虚拟环境"
    source venv/bin/activate
else
    echo "❌ 虚拟环境不存在，请先运行: python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt"
    exit 1
fi

# 检查依赖是否安装
if ! python -c "import fastapi" 2>/dev/null; then
    echo "❌ 依赖未安装，正在安装..."
    pip install -r requirements.txt
fi

# 启动服务
echo "✓ 启动FastAPI服务"
echo "📚 API文档: http://localhost:8000/docs"
echo "🔍 健康检查: http://localhost:8000/health"
echo ""
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

