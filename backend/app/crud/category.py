"""
分类CRUD操作
"""
from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.category import Category
from app.schemas.category import CategoryCreate, CategoryUpdate


def create_category(db: Session, user_id: int, category_create: CategoryCreate) -> Category:
    """
    创建分类
    
    Args:
        db: 数据库会话
        user_id: 用户ID
        category_create: 分类创建数据
    
    Returns:
        Category: 创建的分类对象
    """
    db_category = Category(
        user_id=user_id,
        name=category_create.name,
        type=category_create.type,
        icon=category_create.icon,
        color=category_create.color,
        is_system=False,  # 用户创建的分类不是系统分类
        sort_order=category_create.sort_order or 0,
    )
    
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    
    return db_category


def get_categories(
    db: Session,
    user_id: int,
    type: Optional[str] = None
) -> List[Category]:
    """
    获取用户分类列表
    
    Args:
        db: 数据库会话
        user_id: 用户ID
        type: 分类类型筛选（income/expense），None表示获取所有类型
    
    Returns:
        List[Category]: 分类列表
    """
    query = db.query(Category).filter(Category.user_id == user_id)
    
    # 按类型筛选
    if type:
        query = query.filter(Category.type == type)
    
    # 按排序顺序和创建时间排序
    return query.order_by(Category.sort_order, Category.created_at).all()


def get_category(db: Session, category_id: int, user_id: int) -> Optional[Category]:
    """
    根据ID获取分类（确保是用户的分类）
    
    Args:
        db: 数据库会话
        category_id: 分类ID
        user_id: 用户ID（用于权限验证）
    
    Returns:
        Category: 分类对象，不存在或不属于该用户返回None
    """
    return db.query(Category).filter(
        Category.id == category_id,
        Category.user_id == user_id
    ).first()


def update_category(
    db: Session,
    category_id: int,
    user_id: int,
    category_update: CategoryUpdate
) -> Optional[Category]:
    """
    更新分类
    
    Args:
        db: 数据库会话
        category_id: 分类ID
        user_id: 用户ID（用于权限验证）
        category_update: 更新数据
    
    Returns:
        Category: 更新后的分类对象，分类不存在或不属于该用户返回None
    """
    db_category = get_category(db, category_id, user_id)
    if db_category is None:
        return None
    
    # 更新字段
    update_data = category_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_category, field, value)
    
    db.commit()
    db.refresh(db_category)
    
    return db_category


def delete_category(db: Session, category_id: int, user_id: int) -> bool:
    """
    删除分类
    
    注意：删除分类时，该分类下的账目不删除，但category_id会被设为NULL
    这是通过数据库外键的ondelete行为实现的
    
    Args:
        db: 数据库会话
        category_id: 分类ID
        user_id: 用户ID（用于权限验证）
    
    Returns:
        bool: 删除成功返回True，分类不存在或不属于该用户返回False
    """
    db_category = get_category(db, category_id, user_id)
    if db_category is None:
        return False
    
    # 检查是否有账目使用此分类
    # 注意：由于外键约束，删除分类时，关联的账目的category_id会被设为NULL
    # 但我们需要先检查，因为如果用户想删除系统分类，应该不允许
    if db_category.is_system:
        # 不允许删除系统分类
        return False
    
    db.delete(db_category)
    db.commit()
    
    return True


def copy_system_categories_to_user(db: Session, user_id: int) -> None:
    """
    复制系统分类到用户账户
    
    用户第一次注册时，自动复制系统分类到用户账户
    这样用户可以基于系统分类进行自定义
    
    Args:
        db: 数据库会话
        user_id: 用户ID
    """
    # 检查用户是否已经有分类了
    existing_count = db.query(Category).filter(Category.user_id == user_id).count()
    if existing_count > 0:
        # 用户已有分类，不重复复制
        return
    
    # 获取所有系统分类
    system_categories = db.query(Category).filter(
        Category.is_system == True
    ).all()
    
    # 复制系统分类到用户账户
    for sys_cat in system_categories:
        user_category = Category(
            user_id=user_id,
            name=sys_cat.name,
            type=sys_cat.type,
            icon=sys_cat.icon,
            color=sys_cat.color,
            is_system=False,  # 用户分类不是系统分类
            sort_order=sys_cat.sort_order,
        )
        db.add(user_category)
    
    db.commit()

