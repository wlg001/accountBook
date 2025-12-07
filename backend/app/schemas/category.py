"""
分类相关Schema定义
"""
from datetime import datetime
from typing import Optional, Literal
from pydantic import BaseModel, Field


class CategoryBase(BaseModel):
    """分类基础Schema"""
    name: str = Field(..., min_length=1, max_length=50, description="分类名称")
    type: Literal["income", "expense"] = Field(..., description="分类类型")
    icon: Optional[str] = Field(None, max_length=50, description="图标")
    color: Optional[str] = Field(None, max_length=20, description="颜色代码")
    sort_order: Optional[int] = Field(0, description="排序顺序")


class CategoryCreate(CategoryBase):
    """创建分类Schema"""
    pass


class CategoryUpdate(BaseModel):
    """更新分类Schema"""
    name: Optional[str] = Field(None, min_length=1, max_length=50, description="分类名称")
    icon: Optional[str] = Field(None, max_length=50, description="图标")
    color: Optional[str] = Field(None, max_length=20, description="颜色代码")
    sort_order: Optional[int] = Field(None, description="排序顺序")


class CategoryResponse(CategoryBase):
    """分类响应Schema"""
    id: int
    user_id: Optional[int] = None
    is_system: bool
    created_at: datetime
    
    class Config:
        from_attributes = True

