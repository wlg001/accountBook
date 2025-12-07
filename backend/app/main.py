"""
FastAPI应用主入口
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings

# 创建FastAPI应用实例
app = FastAPI(
    title=settings.APP_NAME,
    description="个人财务管理系统API",
    version=settings.APP_VERSION,
    docs_url="/docs",  # Swagger UI
    redoc_url="/redoc",  # ReDoc
)

# 配置CORS中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["Root"])
async def read_root():
    """
    根路径
    """
    return {
        "message": f"{settings.APP_NAME}服务运行中",
        "version": settings.APP_VERSION,
        "docs": "/docs",
        "redoc": "/redoc"
    }


@app.get("/health", tags=["Health"])
async def health_check():
    """
    健康检查
    """
    return {
        "status": "healthy",
        "environment": settings.ENVIRONMENT
    }


# 注册API路由
from app.api.v1 import auth

app.include_router(auth.router, prefix="/api/v1/auth", tags=["认证"])

# 后续会注册更多路由
# from app.api.v1 import categories, transactions, statistics
# app.include_router(categories.router, prefix="/api/v1/categories", tags=["分类"])
# app.include_router(transactions.router, prefix="/api/v1/transactions", tags=["账目"])
# app.include_router(statistics.router, prefix="/api/v1/statistics", tags=["统计"])

