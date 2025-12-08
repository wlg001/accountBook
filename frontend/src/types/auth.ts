/**
 * 认证相关类型定义
 */

export type RegisterRequest = {
  username: string;
  email: string;
  password: string;
  nickname?: string;
};

export type LoginRequest = {
  username: string;
  password: string;
};

export type UpdateUserRequest = {
  nickname?: string;
  email?: string;
  avatar_url?: string;
};

export type ChangePasswordRequest = {
  old_password: string;
  new_password: string;
};

export type User = {
  id: number;
  username: string;
  email: string;
  nickname?: string;
  avatar_url?: string;
  is_active: boolean;
  created_at: string;
  updated_at?: string;
};

export type LoginResponse = {
  access_token: string;
  token_type: string;
  user: User;
};

