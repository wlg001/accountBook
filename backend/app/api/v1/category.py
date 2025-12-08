"""
分类管理API
"""
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.api.deps import get_current_user
from app.crud import category as category_crud
from app.schemas.category import (
    CategoryCreate,
    CategoryUpdate,
    CategoryResponse,
)
from app.schemas.common import ApiResponse
from app.models.user import User

router = APIRouter()


@router.get("", response_model=ApiResponse[list[CategoryResponse]])
def get_categories(
    type: Optional[str] = Query(None, description="分类类型筛选（income/expense）"),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    获取分类列表
    
    - 获取当前用户的所有分类
    - 支持按类型筛选（income/expense）
    - 需要认证
    """
    # 验证类型参数
    if type and type not in ["income", "expense"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="类型参数必须是 'income' 或 'expense'"
        )
    
    # 获取分类列表
    categories = category_crud.get_categories(db, current_user.id, type=type)
    
    return ApiResponse(
        code=200,
        message="获取成功",
        data=[CategoryResponse.model_validate(cat) for cat in categories]
    )


@router.post("", response_model=ApiResponse[CategoryResponse], status_code=status.HTTP_201_CREATED)
def create_category(
    category_create: CategoryCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    创建分类
    
    - 创建新的用户分类
    - 需要认证
    """
    # 创建分类
    category = category_crud.create_category(db, current_user.id, category_create)
    
    return ApiResponse(
        code=201,
        message="创建成功",
        data=CategoryResponse.model_validate(category)
    )


@router.get("/{category_id}", response_model=ApiResponse[CategoryResponse])
def get_category(
    category_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    获取单个分类
    
    - 根据ID获取分类详情
    - 只能获取自己的分类
    - 需要认证
    """
    category = category_crud.get_category(db, category_id, current_user.id)
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="分类不存在或无权限访问"
        )
    
    return ApiResponse(
        code=200,
        message="获取成功",
        data=CategoryResponse.model_validate(category)
    )


@router.put("/{category_id}", response_model=ApiResponse[CategoryResponse])
def update_category(
    category_id: int,
    category_update: CategoryUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    更新分类
    
    - 更新分类信息（名称、图标、颜色、排序等）
    - 只能更新自己的分类
    - 需要认证
    """
    category = category_crud.update_category(db, category_id, current_user.id, category_update)
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="分类不存在或无权限访问"
        )
    
    return ApiResponse(
        code=200,
        message="更新成功",
        data=CategoryResponse.model_validate(category)
    )


@router.delete("/{category_id}", response_model=ApiResponse)
def delete_category(
    category_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    删除分类
    
    - 删除用户分类
    - 只能删除自己的分类
    - 删除时，关联账目的category_id会被设为NULL
    - 需要认证
    """
    # 检查分类是否存在
    category = category_crud.get_category(db, category_id, current_user.id)
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="分类不存在或无权限访问"
        )
    
    # 检查是否有关联账目（可选：给出警告）
    # 注意：由于外键约束，删除分类时，关联账目的category_id会自动设为NULL
    # 这里可以添加检查逻辑，但根据业务需求，我们允许删除有关联账目的分类
    
    # 删除分类
    deleted = category_crud.delete_category(db, category_id, current_user.id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="删除失败，可能是系统分类或存在其他限制"
        )
    
    return ApiResponse(
        code=200,
        message="删除成功",
        data=None
    )

