"""
账目相关Schema定义
"""
from datetime import datetime, date
from typing import Optional, Literal
from decimal import Decimal
from pydantic import BaseModel, Field, field_validator


class TransactionBase(BaseModel):
    """账目基础Schema"""
    amount: Decimal = Field(..., gt=0, description="金额（必须大于0，精确到分）")
    type: Literal["income", "expense"] = Field(..., description="类型")
    category_id: Optional[int] = Field(None, description="分类ID")
    transaction_date: date = Field(..., description="账目日期")
    description: Optional[str] = Field(None, max_length=500, description="备注")
    tags: Optional[str] = Field(None, max_length=255, description="标签（逗号分隔）")
    account_type: Optional[str] = Field(None, max_length=50, description="账户类型")
    
    @field_validator('amount')
    @classmethod
    def amount_positive(cls, v: Decimal) -> Decimal:
        """验证金额必须大于0"""
        if v <= 0:
            raise ValueError('金额必须大于0')
        # 限制最大12位（含小数点后2位）
        if v >= Decimal('10000000000'):  # 100亿
            raise ValueError('金额过大')
        return v


class TransactionCreate(TransactionBase):
    """创建账目Schema"""
    pass


class TransactionUpdate(BaseModel):
    """更新账目Schema"""
    amount: Optional[Decimal] = Field(None, gt=0, description="金额")
    category_id: Optional[int] = Field(None, description="分类ID")
    transaction_date: Optional[date] = Field(None, description="账目日期")
    description: Optional[str] = Field(None, max_length=500, description="备注")
    tags: Optional[str] = Field(None, max_length=255, description="标签")
    account_type: Optional[str] = Field(None, max_length=50, description="账户类型")


class TransactionQuery(BaseModel):
    """账目查询参数Schema"""
    type: Optional[Literal["income", "expense"]] = None
    category_id: Optional[int] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    keyword: Optional[str] = None  # 搜索备注关键词
    page: int = Field(1, ge=1, description="页码")
    size: int = Field(20, ge=1, le=100, description="每页数量")


class CategoryInTransaction(BaseModel):
    """账目中的分类信息"""
    id: int
    name: str
    icon: Optional[str] = None
    color: Optional[str] = None
    type: str
    
    class Config:
        from_attributes = True


class TransactionResponse(BaseModel):
    """账目响应Schema"""
    id: int
    user_id: int
    category_id: Optional[int] = None
    category: Optional[CategoryInTransaction] = None
    amount: Decimal
    type: str
    transaction_date: date
    description: Optional[str] = None
    tags: Optional[str] = None
    account_type: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True

