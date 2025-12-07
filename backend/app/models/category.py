"""
分类模型
"""
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base


class Category(Base):
    """
    分类表
    
    存储收入和支出的分类信息
    支持系统预设分类和用户自定义分类
    """
    __tablename__ = "categories"
    
    # 主键
    id = Column(Integer, primary_key=True, index=True, comment="分类ID")
    
    # 外键：关联用户（系统分类user_id为NULL）
    user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=True,  # 系统分类为NULL
        index=True,
        comment="用户ID（系统分类为NULL）"
    )
    
    # 分类信息
    name = Column(
        String(50),
        nullable=False,
        comment="分类名称"
    )
    type = Column(
        String(10),
        nullable=False,
        index=True,
        comment="分类类型（income/expense）"
    )
    icon = Column(String(50), comment="图标（Emoji或图标名称）")
    color = Column(String(20), comment="颜色代码（如#FF6B6B）")
    
    # 系统分类标识
    is_system = Column(
        Boolean,
        default=False,
        nullable=False,
        comment="是否为系统预设分类"
    )
    
    # 排序
    sort_order = Column(
        Integer,
        default=0,
        comment="排序顺序"
    )
    
    # 时间戳
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
        comment="创建时间"
    )
    
    # 关系定义
    # 多对一：多个分类属于一个用户
    user = relationship("User", back_populates="categories")
    
    # 一对多：一个分类有多个账目
    transactions = relationship(
        "Transaction",
        back_populates="category",
        cascade="all, delete-orphan"
    )
    
    # 一对多：一个分类有多个预算（V2.0）
    budgets = relationship(
        "Budget",
        back_populates="category",
        cascade="all, delete-orphan"
    )
    
    def __repr__(self):
        return f"<Category(id={self.id}, name='{self.name}', type='{self.type}')>"
    
    def __str__(self):
        return f"{self.icon} {self.name}"
