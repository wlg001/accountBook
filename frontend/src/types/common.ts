/**
 * 通用类型定义
 */

// API响应基础结构
export interface ApiResponse<T = any> {
  code: number;
  message: string;
  data: T;
}

// 分页响应
export interface PaginatedResponse<T> {
  total: number;
  page: number;
  size: number;
  items: T[];
}

// 分页请求参数
export interface PaginationParams {
  page?: number;
  size?: number;
}

