"""
应用配置管理
"""
from pydantic_settings import BaseSettings
from typing import List
import json


class Settings(BaseSettings):
    """应用配置类"""
    
    # 应用信息
    APP_NAME: str = "记账本API"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True
    
    # 服务器配置
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    
    # 数据库配置
    DATABASE_URL: str
    
    # JWT配置
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 10080  # 7天
    
    # CORS配置
    CORS_ORIGINS: str = '["http://localhost:5173", "http://localhost:3000"]'
    
    @property
    def cors_origins_list(self) -> List[str]:
        """解析CORS origins为列表"""
        try:
            return json.loads(self.CORS_ORIGINS)
        except:
            return ["http://localhost:5173", "http://localhost:3000"]
    
    # 环境
    ENVIRONMENT: str = "development"
    
    class Config:
        env_file = ".env"
        case_sensitive = True


# 创建全局配置实例
settings = Settings()

