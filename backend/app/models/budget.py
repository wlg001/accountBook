"""
预算模型（V2.0功能）
"""
from sqlalchemy import Column, Integer, Numeric, String, Date, DateTime, ForeignKey, Index
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base


class Budget(Base):
    """
    预算表（V2.0功能）
    
    存储用户的预算设置
    支持总预算和分类预算
    """
    __tablename__ = "budgets"
    
    # 主键
    id = Column(Integer, primary_key=True, index=True, comment="预算ID")
    
    # 外键：关联用户
    user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
        comment="用户ID"
    )
    
    # 外键：关联分类（可为NULL表示总预算）
    category_id = Column(
        Integer,
        ForeignKey("categories.id", ondelete="CASCADE"),
        nullable=True,
        index=True,
        comment="分类ID（NULL表示总预算）"
    )
    
    # 预算金额
    amount = Column(
        Numeric(12, 2),
        nullable=False,
        comment="预算金额"
    )
    
    # 预算周期
    period_type = Column(
        String(20),
        nullable=False,
        comment="周期类型（monthly/yearly）"
    )
    
    # 预算时间范围
    start_date = Column(
        Date,
        nullable=False,
        comment="开始日期"
    )
    end_date = Column(
        Date,
        nullable=False,
        comment="结束日期"
    )
    
    # 时间戳
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
        comment="创建时间"
    )
    
    # 关系定义
    # 多对一：多个预算属于一个用户
    user = relationship("User", back_populates="budgets")
    
    # 多对一：多个预算属于一个分类
    category = relationship("Category", back_populates="budgets")
    
    # 复合索引：用户ID + 时间范围
    __table_args__ = (
        Index('idx_user_period', 'user_id', 'start_date', 'end_date'),
    )
    
    def __repr__(self):
        return f"<Budget(id={self.id}, amount={self.amount}, period='{self.period_type}')>"
    
    def __str__(self):
        return f"预算: ¥{self.amount} ({self.start_date} - {self.end_date})"
