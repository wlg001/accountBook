/**
 * 分类状态管理Store
 */
import { create } from 'zustand';
import categoryAPI from '../services/category';
import type { Category, CategoryType, CategoryCreateRequest, CategoryUpdateRequest } from '../types/category';

interface CategoryState {
  // 状态
  categories: Category[];
  loading: boolean;
  error: string | null;

  // 操作
  fetchCategories: (type?: CategoryType) => Promise<void>;
  createCategory: (data: CategoryCreateRequest) => Promise<Category>;
  updateCategory: (id: number, data: CategoryUpdateRequest) => Promise<Category>;
  deleteCategory: (id: number) => Promise<void>;
  clearError: () => void;
}

export const useCategoryStore = create<CategoryState>((set, get) => ({
  // 初始状态
  categories: [],
  loading: false,
  error: null,

  // 获取分类列表
  fetchCategories: async (type?: CategoryType) => {
    try {
      set({ loading: true, error: null });
      const categories = await categoryAPI.getCategories(type);
      set({ categories, loading: false });
    } catch (error: any) {
      const errorMessage = error?.response?.data?.message || error?.message || '获取分类失败';
      set({ error: errorMessage, loading: false });
      throw error;
    }
  },

  // 创建分类
  createCategory: async (data: CategoryCreateRequest) => {
    try {
      set({ loading: true, error: null });
      const newCategory = await categoryAPI.createCategory(data);
      
      // 添加到列表
      set((state) => ({
        categories: [...state.categories, newCategory],
        loading: false,
      }));
      
      return newCategory;
    } catch (error: any) {
      const errorMessage = error?.response?.data?.message || error?.message || '创建分类失败';
      set({ error: errorMessage, loading: false });
      throw error;
    }
  },

  // 更新分类
  updateCategory: async (id: number, data: CategoryUpdateRequest) => {
    try {
      set({ loading: true, error: null });
      const updatedCategory = await categoryAPI.updateCategory(id, data);
      
      // 更新列表中的分类
      set((state) => ({
        categories: state.categories.map((cat) =>
          cat.id === id ? updatedCategory : cat
        ),
        loading: false,
      }));
      
      return updatedCategory;
    } catch (error: any) {
      const errorMessage = error?.response?.data?.message || error?.message || '更新分类失败';
      set({ error: errorMessage, loading: false });
      throw error;
    }
  },

  // 删除分类
  deleteCategory: async (id: number) => {
    try {
      set({ loading: true, error: null });
      await categoryAPI.deleteCategory(id);
      
      // 从列表中移除
      set((state) => ({
        categories: state.categories.filter((cat) => cat.id !== id),
        loading: false,
      }));
    } catch (error: any) {
      const errorMessage = error?.response?.data?.message || error?.message || '删除分类失败';
      set({ error: errorMessage, loading: false });
      throw error;
    }
  },

  // 清除错误
  clearError: () => {
    set({ error: null });
  },
}));

