"""
用户模型
"""
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base


class User(Base):
    """
    用户表
    
    存储用户基本信息和认证信息
    """
    __tablename__ = "users"
    
    # 主键
    id = Column(Integer, primary_key=True, index=True, comment="用户ID")
    
    # 认证信息
    username = Column(
        String(50), 
        unique=True, 
        index=True, 
        nullable=False,
        comment="用户名（唯一）"
    )
    email = Column(
        String(100), 
        unique=True, 
        index=True, 
        nullable=False,
        comment="邮箱（唯一）"
    )
    hashed_password = Column(
        String(255), 
        nullable=False,
        comment="密码哈希值"
    )
    
    # 个人信息
    nickname = Column(String(50), comment="昵称")
    avatar_url = Column(String(255), comment="头像URL")
    
    # 状态
    is_active = Column(
        Boolean, 
        default=True, 
        nullable=False,
        comment="是否激活"
    )
    
    # 时间戳
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
        comment="创建时间"
    )
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        comment="更新时间"
    )
    
    # 关系定义
    # 一个用户有多个分类
    categories = relationship(
        "Category",
        back_populates="user",
        cascade="all, delete-orphan"
    )
    
    # 一个用户有多个账目
    transactions = relationship(
        "Transaction",
        back_populates="user",
        cascade="all, delete-orphan"
    )
    
    # 一个用户有多个预算（V2.0）
    budgets = relationship(
        "Budget",
        back_populates="user",
        cascade="all, delete-orphan"
    )
    
    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', email='{self.email}')>"
    
    def __str__(self):
        return self.username
