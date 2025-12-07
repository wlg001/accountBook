"""
用户CRUD操作
"""
from typing import Optional
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.core.security import get_password_hash, verify_password


def get_user(db: Session, user_id: int) -> Optional[User]:
    """
    根据ID获取用户
    
    Args:
        db: 数据库会话
        user_id: 用户ID
    
    Returns:
        User: 用户对象，不存在返回None
    """
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_username(db: Session, username: str) -> Optional[User]:
    """
    根据用户名获取用户
    
    Args:
        db: 数据库会话
        username: 用户名
    
    Returns:
        User: 用户对象，不存在返回None
    """
    return db.query(User).filter(User.username == username).first()


def get_user_by_email(db: Session, email: str) -> Optional[User]:
    """
    根据邮箱获取用户
    
    Args:
        db: 数据库会话
        email: 邮箱
    
    Returns:
        User: 用户对象，不存在返回None
    """
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, user_create: UserCreate) -> User:
    """
    创建用户
    
    Args:
        db: 数据库会话
        user_create: 用户创建数据
    
    Returns:
        User: 创建的用户对象
    """
    # 加密密码
    hashed_password = get_password_hash(user_create.password)
    
    # 创建用户对象
    db_user = User(
        username=user_create.username,
        email=user_create.email,
        hashed_password=hashed_password,
        nickname=user_create.nickname,
    )
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return db_user


def update_user(db: Session, user_id: int, user_update: UserUpdate) -> Optional[User]:
    """
    更新用户信息
    
    Args:
        db: 数据库会话
        user_id: 用户ID
        user_update: 更新数据
    
    Returns:
        User: 更新后的用户对象，用户不存在返回None
    """
    db_user = get_user(db, user_id)
    if db_user is None:
        return None
    
    # 更新字段
    update_data = user_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_user, field, value)
    
    db.commit()
    db.refresh(db_user)
    
    return db_user


def authenticate_user(db: Session, username: str, password: str) -> Optional[User]:
    """
    验证用户
    
    Args:
        db: 数据库会话
        username: 用户名
        password: 密码
    
    Returns:
        User: 验证成功返回用户对象，失败返回None
    """
    user = get_user_by_username(db, username)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user


def change_password(db: Session, user_id: int, old_password: str, new_password: str) -> bool:
    """
    修改密码
    
    Args:
        db: 数据库会话
        user_id: 用户ID
        old_password: 旧密码
        new_password: 新密码
    
    Returns:
        bool: 修改成功返回True，失败返回False
    """
    user = get_user(db, user_id)
    if not user:
        return False
    
    # 验证旧密码
    if not verify_password(old_password, user.hashed_password):
        return False
    
    # 设置新密码
    user.hashed_password = get_password_hash(new_password)
    db.commit()
    
    return True

