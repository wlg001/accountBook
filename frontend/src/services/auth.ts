/**
 * 认证相关API
 */
import api from './api';
import type {
  RegisterRequest,
  LoginRequest,
  UpdateUserRequest,
  ChangePasswordRequest,
} from '../types/auth';

// API函数
const authAPI = {
  /**
   * 用户注册
   */
  register: async (data: RegisterRequest) => {
    const response = await api.post('/auth/register', data);
    return response; // api拦截器已经返回了response.data
  },

  /**
   * 用户登录
   */
  login: async (data: LoginRequest) => {
    const response = await api.post('/auth/login', data);
    return response; // api拦截器已经返回了response.data
  },

  /**
   * 获取当前用户信息
   */
  getMe: async () => {
    const response = await api.get('/auth/me');
    return response; // api拦截器已经返回了response.data
  },

  /**
   * 更新当前用户信息
   */
  updateMe: async (data: UpdateUserRequest) => {
    const response = await api.put('/auth/me', data);
    return response; // api拦截器已经返回了response.data
  },

  /**
   * 修改密码
   */
  changePassword: async (data: ChangePasswordRequest) => {
    const response = await api.post('/auth/change-password', data);
    return response; // api拦截器已经返回了response.data
  },
};

export default authAPI;

