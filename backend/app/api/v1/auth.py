"""
用户认证API
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.security import create_access_token
from app.api.deps import get_current_user
from app.crud import user as user_crud
from app.schemas.user import (
    UserCreate,
    UserLogin,
    UserResponse,
    LoginResponse,
    UserUpdate,
    ChangePassword,
)
from app.schemas.common import ApiResponse
from app.models.user import User

router = APIRouter()


@router.post("/register", response_model=ApiResponse[UserResponse], status_code=status.HTTP_201_CREATED)
def register(user_create: UserCreate, db: Session = Depends(get_db)):
    """
    用户注册
    
    - 检查用户名和邮箱是否已存在
    - 创建新用户
    - 返回用户信息
    """
    # 检查用户名是否已存在
    existing_user = user_crud.get_user_by_username(db, user_create.username)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="用户名已存在"
        )
    
    # 检查邮箱是否已存在
    existing_email = user_crud.get_user_by_email(db, user_create.email)
    if existing_email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="邮箱已被注册"
        )
    
    # 创建用户
    user = user_crud.create_user(db, user_create)
    
    return ApiResponse(
        code=201,
        message="注册成功",
        data=UserResponse.model_validate(user)
    )


@router.post("/login", response_model=ApiResponse[LoginResponse])
def login(user_login: UserLogin, db: Session = Depends(get_db)):
    """
    用户登录
    
    - 验证用户名和密码
    - 生成JWT Token
    - 返回Token和用户信息
    """
    # 验证用户
    user = user_crud.authenticate_user(db, user_login.username, user_login.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="用户名或密码错误",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # 检查用户是否激活
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="用户已被禁用"
        )
    
    # 创建Token
    access_token = create_access_token({"sub": user.id})
    
    return ApiResponse(
        code=200,
        message="登录成功",
        data=LoginResponse(
            access_token=access_token,
            token_type="bearer",
            user=UserResponse.model_validate(user)
        )
    )


@router.get("/me", response_model=ApiResponse[UserResponse])
def get_current_user_info(current_user: User = Depends(get_current_user)):
    """
    获取当前用户信息
    
    需要认证
    """
    return ApiResponse(
        code=200,
        message="获取成功",
        data=UserResponse.model_validate(current_user)
    )


@router.put("/me", response_model=ApiResponse[UserResponse])
def update_current_user_info(
    user_update: UserUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    更新当前用户信息
    
    需要认证
    """
    # 如果要更新邮箱，检查是否已被使用
    if user_update.email and user_update.email != current_user.email:
        existing_email = user_crud.get_user_by_email(db, user_update.email)
        if existing_email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="邮箱已被使用"
            )
    
    # 更新用户
    updated_user = user_crud.update_user(db, current_user.id, user_update)
    if not updated_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="用户不存在"
        )
    
    return ApiResponse(
        code=200,
        message="更新成功",
        data=UserResponse.model_validate(updated_user)
    )


@router.post("/change-password", response_model=ApiResponse)
def change_user_password(
    password_data: ChangePassword,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    修改密码
    
    需要认证
    """
    # 修改密码
    success = user_crud.change_password(
        db,
        current_user.id,
        password_data.old_password,
        password_data.new_password
    )
    
    if not success:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="旧密码错误"
        )
    
    return ApiResponse(
        code=200,
        message="密码修改成功"
    )

