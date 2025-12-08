/**
 * 分类相关类型定义
 */

export type CategoryType = 'income' | 'expense';

export type Category = {
  id: number;
  user_id: number | null;
  name: string;
  type: CategoryType;
  icon?: string;
  color?: string;
  is_system: boolean;
  sort_order: number;
  created_at: string;
};

export type CategoryCreateRequest = {
  name: string;
  type: CategoryType;
  icon?: string;
  color?: string;
  sort_order?: number;
};

export type CategoryUpdateRequest = {
  name?: string;
  icon?: string;
  color?: string;
  sort_order?: number;
};

