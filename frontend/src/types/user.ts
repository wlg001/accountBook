/**
 * 用户相关类型定义
 */

// 用户信息
export interface User {
  id: number;
  username: string;
  email: string;
  nickname?: string;
  avatar_url?: string;
  is_active: boolean;
  created_at: string;
  updated_at?: string;
}

// 登录请求
export interface LoginRequest {
  username: string;
  password: string;
}

// 登录响应
export interface LoginResponse {
  access_token: string;
  token_type: string;
  user: User;
}

// 注册请求
export interface RegisterRequest {
  username: string;
  email: string;
  password: string;
  nickname?: string;
}

// 用户更新请求
export interface UpdateUserRequest {
  nickname?: string;
  email?: string;
  avatar_url?: string;
}

// 修改密码请求
export interface ChangePasswordRequest {
  old_password: string;
  new_password: string;
}

