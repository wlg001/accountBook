"""
账目模型
"""
from sqlalchemy import Column, Integer, String, Numeric, Date, DateTime, ForeignKey, Text, Index
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.core.database import Base


class Transaction(Base):
    """
    账目表
    
    存储用户的收入和支出记录
    """
    __tablename__ = "transactions"
    
    # 主键
    id = Column(Integer, primary_key=True, index=True, comment="账目ID")
    
    # 外键：关联用户
    user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
        comment="用户ID"
    )
    
    # 外键：关联分类（可为空，允许删除分类后账目保留）
    category_id = Column(
        Integer,
        ForeignKey("categories.id", ondelete="SET NULL"),
        nullable=True,
        index=True,
        comment="分类ID"
    )
    
    # 金额信息
    amount = Column(
        Numeric(12, 2),  # 总共12位，小数点后2位（最大9999999999.99）
        nullable=False,
        comment="金额"
    )
    type = Column(
        String(10),
        nullable=False,
        index=True,
        comment="类型（income/expense）"
    )
    
    # 账目信息
    transaction_date = Column(
        Date,
        nullable=False,
        index=True,
        comment="账目日期"
    )
    description = Column(Text, comment="备注说明")
    tags = Column(String(255), comment="标签（逗号分隔）")
    
    # 账户类型（V2.0功能，当前可选）
    account_type = Column(
        String(50),
        comment="账户类型（现金/银行卡/支付宝/微信等）"
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
        onupdate=func.now(),
        nullable=True,
        comment="更新时间（创建时为NULL，更新时自动设置）"
    )
    
    # 关系定义
    # 多对一：多个账目属于一个用户
    user = relationship("User", back_populates="transactions")
    
    # 多对一：多个账目属于一个分类
    category = relationship("Category", back_populates="transactions")
    
    # 复合索引：用户ID + 日期（常用查询组合）
    __table_args__ = (
        Index('idx_user_date', 'user_id', 'transaction_date'),
        Index('idx_user_type', 'user_id', 'type'),
    )
    
    def __repr__(self):
        return f"<Transaction(id={self.id}, type='{self.type}', amount={self.amount}, date={self.transaction_date})>"
    
    def __str__(self):
        sign = "+" if self.type == "income" else "-"
        return f"{sign}¥{self.amount} - {self.transaction_date}"
