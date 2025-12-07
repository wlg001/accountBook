/**
 * 常量定义
 */

// API基础URL
export const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000/api/v1';

// 应用信息
export const APP_TITLE = import.meta.env.VITE_APP_TITLE || '记账本';
export const APP_VERSION = import.meta.env.VITE_APP_VERSION || '1.0.0';

// 本地存储键名
export const STORAGE_KEYS = {
  TOKEN: 'accountbook_token',
  USER: 'accountbook_user',
} as const;

// 日期格式
export const DATE_FORMAT = 'YYYY-MM-DD';
export const DATETIME_FORMAT = 'YYYY-MM-DD HH:mm:ss';
export const TIME_FORMAT = 'HH:mm:ss';

// 分页配置
export const PAGE_SIZE = 20;
export const PAGE_SIZE_OPTIONS = [10, 20, 50, 100];

// 账目类型
export const TRANSACTION_TYPES = {
  INCOME: 'income',
  EXPENSE: 'expense',
} as const;

// 颜色配置
export const COLORS = {
  PRIMARY: '#1890ff',
  INCOME: '#52c41a',
  EXPENSE: '#ff4d4f',
  WARNING: '#faad14',
  SUCCESS: '#52c41a',
  ERROR: '#ff4d4f',
} as const;

