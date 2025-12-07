/**
 * 认证状态管理Store
 */
import { create } from 'zustand';
import authAPI, { User, LoginRequest, RegisterRequest } from '../services/auth';
import { STORAGE_KEYS } from '../utils/constants';

interface AuthState {
  // 状态
  user: User | null;
  token: string | null;
  isAuthenticated: boolean;
  loading: boolean;

  // 操作
  login: (data: LoginRequest) => Promise<void>;
  register: (data: RegisterRequest) => Promise<void>;
  logout: () => void;
  fetchUserInfo: () => Promise<void>;
  updateUser: (data: any) => Promise<void>;
  setToken: (token: string) => void;
  setUser: (user: User) => void;
}

export const useAuthStore = create<AuthState>((set, get) => ({
  // 初始状态
  user: null,
  token: localStorage.getItem(STORAGE_KEYS.TOKEN),
  isAuthenticated: !!localStorage.getItem(STORAGE_KEYS.TOKEN),
  loading: false,

  // 设置Token
  setToken: (token: string) => {
    localStorage.setItem(STORAGE_KEYS.TOKEN, token);
    set({ token, isAuthenticated: true });
  },

  // 设置用户信息
  setUser: (user: User) => {
    set({ user });
  },

  // 登录
  login: async (data: LoginRequest) => {
    try {
      set({ loading: true });
      const response = await authAPI.login(data);
      const { access_token, user } = response;

      // 保存Token和用户信息
      localStorage.setItem(STORAGE_KEYS.TOKEN, access_token);
      localStorage.setItem(STORAGE_KEYS.USER, JSON.stringify(user));

      set({
        token: access_token,
        user,
        isAuthenticated: true,
        loading: false,
      });
    } catch (error) {
      set({ loading: false });
      throw error;
    }
  },

  // 注册
  register: async (data: RegisterRequest) => {
    try {
      set({ loading: true });
      await authAPI.register(data);

      // 注册成功后自动登录
      await get().login({
        username: data.username,
        password: data.password,
      });
    } catch (error) {
      set({ loading: false });
      throw error;
    }
  },

  // 登出
  logout: () => {
    localStorage.removeItem(STORAGE_KEYS.TOKEN);
    localStorage.removeItem(STORAGE_KEYS.USER);
    set({
      user: null,
      token: null,
      isAuthenticated: false,
    });
  },

  // 获取用户信息
  fetchUserInfo: async () => {
    try {
      set({ loading: true });
      const response = await authAPI.getMe();
      const user = response;

      localStorage.setItem(STORAGE_KEYS.USER, JSON.stringify(user));
      set({ user, loading: false });
    } catch (error) {
      set({ loading: false });
      // Token失效，自动登出
      get().logout();
      throw error;
    }
  },

  // 更新用户信息
  updateUser: async (data: any) => {
    try {
      set({ loading: true });
      const response = await authAPI.updateMe(data);
      const user = response;

      localStorage.setItem(STORAGE_KEYS.USER, JSON.stringify(user));
      set({ user, loading: false });
    } catch (error) {
      set({ loading: false });
      throw error;
    }
  },
}));

