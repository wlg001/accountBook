/**
 * 认证相关API
 */
import api from './api';

// 请求和响应类型定义
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

// API函数
const authAPI = {
  /**
   * 用户注册
   */
  register: async (data: RegisterRequest) => {
    const response = await api.post('/auth/register', data);
    return response.data;
  },

  /**
   * 用户登录
   */
  login: async (data: LoginRequest) => {
    const response = await api.post('/auth/login', data);
    return response.data;
  },

  /**
   * 获取当前用户信息
   */
  getMe: async () => {
    const response = await api.get('/auth/me');
    return response.data;
  },

  /**
   * 更新当前用户信息
   */
  updateMe: async (data: UpdateUserRequest) => {
    const response = await api.put('/auth/me', data);
    return response.data;
  },

  /**
   * 修改密码
   */
  changePassword: async (data: ChangePasswordRequest) => {
    const response = await api.post('/auth/change-password', data);
    return response.data;
  },
};

export default authAPI;

