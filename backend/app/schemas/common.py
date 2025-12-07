"""
通用Schema定义
"""
from typing import Generic, TypeVar, Optional
from pydantic import BaseModel

# 泛型类型变量
T = TypeVar('T')


class ApiResponse(BaseModel, Generic[T]):
    """
    API统一响应格式
    """
    code: int = 200
    message: str = "success"
    data: Optional[T] = None
    
    class Config:
        json_schema_extra = {
            "example": {
                "code": 200,
                "message": "success",
                "data": {}
            }
        }


class PaginatedResponse(BaseModel, Generic[T]):
    """
    分页响应格式
    """
    total: int
    page: int
    size: int
    items: list[T]
    
    class Config:
        json_schema_extra = {
            "example": {
                "total": 100,
                "page": 1,
                "size": 20,
                "items": []
            }
        }

