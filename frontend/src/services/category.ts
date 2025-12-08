/**
 * 分类相关API
 */
import api from './api';
import type {
  Category,
  CategoryCreateRequest,
  CategoryUpdateRequest,
} from '../types/category';

// API函数
const categoryAPI = {
  /**
   * 获取分类列表
   * @param type 分类类型筛选（可选）
   */
  getCategories: async (type?: 'income' | 'expense'): Promise<Category[]> => {
    const params = type ? { type } : {};
    const response = await api.get('/categories', { params });
    // api拦截器已经返回了response.data，这里response就是{code, message, data}
    return response.data || [];
  },

  /**
   * 获取单个分类
   * @param id 分类ID
   */
  getCategory: async (id: number): Promise<Category> => {
    const response = await api.get(`/categories/${id}`);
    // api拦截器已经返回了response.data，这里response就是{code, message, data}
    return response.data;
  },

  /**
   * 创建分类
   * @param data 分类数据
   */
  createCategory: async (data: CategoryCreateRequest): Promise<Category> => {
    const response = await api.post('/categories', data);
    // api拦截器已经返回了response.data，这里response就是{code, message, data}
    return response.data;
  },

  /**
   * 更新分类
   * @param id 分类ID
   * @param data 更新数据
   */
  updateCategory: async (
    id: number,
    data: CategoryUpdateRequest
  ): Promise<Category> => {
    const response = await api.put(`/categories/${id}`, data);
    // api拦截器已经返回了response.data，这里response就是{code, message, data}
    return response.data;
  },

  /**
   * 删除分类
   * @param id 分类ID
   */
  deleteCategory: async (id: number): Promise<void> => {
    await api.delete(`/categories/${id}`);
  },
};

export default categoryAPI;

