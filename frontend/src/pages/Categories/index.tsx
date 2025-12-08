import { useState, useEffect } from 'react';
import {
  Card,
  Tabs,
  Button,
  Modal,
  Form,
  Input,
  Select,
  Popconfirm,
  message,
  Space,
  Row,
  Col,
  Tag,
  Empty,
} from 'antd';
import {
  PlusOutlined,
  EditOutlined,
  DeleteOutlined,
  ReloadOutlined,
} from '@ant-design/icons';
import { useCategoryStore } from '../../store/categoryStore';
import type { Category, CategoryType, CategoryCreateRequest, CategoryUpdateRequest } from '../../types/category';

const { TabPane } = Tabs;
const { Option } = Select;

// 常用图标列表
const ICON_OPTIONS = [
  '🍜', '🚌', '🛍️', '🎬', '🏥', '📚', '🏠', '📦',
  '💰', '🎁', '📈', '💼', '💵', '🍔', '☕', '🎮',
  '✈️', '🚗', '🎨', '🏋️', '🎵', '📱', '💻', '🎯',
];

// 预设颜色列表
const COLOR_OPTIONS = [
  '#FF6B6B', '#4ECDC4', '#FFE66D', '#A8E6CF', '#FF8B94',
  '#C7CEEA', '#B4A7D6', '#95E1D3', '#52C41A', '#73D13D',
  '#95DE64', '#B7EB8F', '#D9F7BE', '#1890FF', '#722ED1',
];

const Categories = () => {
  const { categories, loading, fetchCategories, createCategory, updateCategory, deleteCategory } = useCategoryStore();
  const [activeTab, setActiveTab] = useState<CategoryType>('expense');
  const [modalVisible, setModalVisible] = useState(false);
  const [editingCategory, setEditingCategory] = useState<Category | null>(null);
  const [form] = Form.useForm();

  // 加载分类列表
  useEffect(() => {
    fetchCategories(activeTab);
  }, [activeTab]);

  // 获取当前类型的分类
  const currentCategories = categories.filter((cat) => cat.type === activeTab);

  // 打开添加分类Modal
  const handleAdd = () => {
    setEditingCategory(null);
    form.resetFields();
    form.setFieldsValue({ type: activeTab });
    setModalVisible(true);
  };

  // 打开编辑分类Modal
  const handleEdit = (category: Category) => {
    setEditingCategory(category);
    form.setFieldsValue({
      name: category.name,
      type: category.type,
      icon: category.icon || '',
      color: category.color || '',
      sort_order: category.sort_order || 0,
    });
    setModalVisible(true);
  };

  // 提交表单
  const handleSubmit = async () => {
    try {
      const values = await form.validateFields();
      
      if (editingCategory) {
        // 更新分类
        const updateData: CategoryUpdateRequest = {
          name: values.name,
          icon: values.icon || undefined,
          color: values.color || undefined,
          sort_order: values.sort_order || 0,
        };
        await updateCategory(editingCategory.id, updateData);
        message.success('分类更新成功');
      } else {
        // 创建分类
        const createData: CategoryCreateRequest = {
          name: values.name,
          type: values.type,
          icon: values.icon || undefined,
          color: values.color || undefined,
          sort_order: values.sort_order || 0,
        };
        await createCategory(createData);
        message.success('分类创建成功');
      }
      
      setModalVisible(false);
      form.resetFields();
      setEditingCategory(null);
    } catch (error: any) {
      if (error?.errorFields) {
        // 表单验证错误
        return;
      }
      message.error(error?.message || '操作失败');
    }
  };

  // 删除分类
  const handleDelete = async (id: number) => {
    try {
      await deleteCategory(id);
      message.success('分类删除成功');
    } catch (error: any) {
      message.error(error?.message || '删除失败');
    }
  };

  // 刷新列表
  const handleRefresh = () => {
    fetchCategories(activeTab);
  };

  return (
    <div style={{ padding: '24px', minHeight: '100vh', background: '#f0f2f5' }}>
      <Card
        title="分类管理"
        extra={
          <Space>
            <Button icon={<ReloadOutlined />} onClick={handleRefresh} loading={loading}>
              刷新
            </Button>
            <Button type="primary" icon={<PlusOutlined />} onClick={handleAdd}>
              添加分类
            </Button>
          </Space>
        }
        style={{ maxWidth: 1200, margin: '0 auto' }}
      >
        <Tabs activeKey={activeTab} onChange={(key) => setActiveTab(key as CategoryType)}>
          <TabPane tab="支出分类" key="expense">
            <CategoryList
              categories={currentCategories}
              loading={loading}
              onEdit={handleEdit}
              onDelete={handleDelete}
            />
          </TabPane>
          <TabPane tab="收入分类" key="income">
            <CategoryList
              categories={currentCategories}
              loading={loading}
              onEdit={handleEdit}
              onDelete={handleDelete}
            />
          </TabPane>
        </Tabs>
      </Card>

      {/* 添加/编辑分类Modal */}
      <Modal
        title={editingCategory ? '编辑分类' : '添加分类'}
        open={modalVisible}
        onOk={handleSubmit}
        onCancel={() => {
          setModalVisible(false);
          form.resetFields();
          setEditingCategory(null);
        }}
        confirmLoading={loading}
        width={600}
      >
        <Form
          form={form}
          layout="vertical"
          initialValues={{
            type: activeTab,
            sort_order: 0,
          }}
        >
          <Form.Item
            name="name"
            label="分类名称"
            rules={[
              { required: true, message: '请输入分类名称' },
              { max: 50, message: '分类名称不能超过50个字符' },
            ]}
          >
            <Input placeholder="请输入分类名称" />
          </Form.Item>

          <Form.Item
            name="type"
            label="分类类型"
            rules={[{ required: true, message: '请选择分类类型' }]}
          >
            <Select disabled={!!editingCategory}>
              <Option value="expense">支出</Option>
              <Option value="income">收入</Option>
            </Select>
          </Form.Item>

          <Form.Item name="icon" label="图标">
            <Select
              placeholder="选择图标（可选）"
              showSearch
              filterOption={(input, option) =>
                (option?.children as string)?.includes(input)
              }
            >
              {ICON_OPTIONS.map((icon) => (
                <Option key={icon} value={icon}>
                  {icon}
                </Option>
              ))}
            </Select>
          </Form.Item>

          <Form.Item name="color" label="颜色">
            <Select placeholder="选择颜色（可选）">
              {COLOR_OPTIONS.map((color) => (
                <Option key={color} value={color}>
                  <Space>
                    <span
                      style={{
                        display: 'inline-block',
                        width: 20,
                        height: 20,
                        background: color,
                        borderRadius: 4,
                        border: '1px solid #d9d9d9',
                      }}
                    />
                    {color}
                  </Space>
                </Option>
              ))}
            </Select>
          </Form.Item>

          <Form.Item name="sort_order" label="排序顺序">
            <Input type="number" placeholder="数字越小越靠前" />
          </Form.Item>
        </Form>
      </Modal>
    </div>
  );
};

// 分类列表组件
interface CategoryListProps {
  categories: Category[];
  loading: boolean;
  onEdit: (category: Category) => void;
  onDelete: (id: number) => void;
}

const CategoryList = ({ categories, loading, onEdit, onDelete }: CategoryListProps) => {
  if (loading && categories.length === 0) {
    return <div style={{ textAlign: 'center', padding: 40 }}>加载中...</div>;
  }

  if (categories.length === 0) {
    return <Empty description="暂无分类，点击右上角添加分类" />;
  }

  return (
    <Row gutter={[16, 16]}>
      {categories.map((category) => (
        <Col key={category.id} xs={24} sm={12} md={8} lg={6}>
          <Card
            hoverable
            style={{
              borderRadius: 8,
              border: `2px solid ${category.color || '#d9d9d9'}`,
            }}
            actions={[
              <EditOutlined key="edit" onClick={() => onEdit(category)} />,
              <Popconfirm
                key="delete"
                title="确定要删除这个分类吗？"
                description="删除后，使用此分类的账目将变为未分类"
                onConfirm={() => onDelete(category.id)}
                okText="确定"
                cancelText="取消"
              >
                <DeleteOutlined style={{ color: '#ff4d4f' }} />
              </Popconfirm>,
            ]}
          >
            <div style={{ textAlign: 'center' }}>
              <div style={{ fontSize: 32, marginBottom: 8 }}>
                {category.icon || '📦'}
              </div>
              <div style={{ fontSize: 16, fontWeight: 500, marginBottom: 8 }}>
                {category.name}
              </div>
              <Space>
                <Tag color={category.color || 'default'}>
                  {category.type === 'income' ? '收入' : '支出'}
                </Tag>
                {category.is_system && <Tag>系统</Tag>}
              </Space>
            </div>
          </Card>
        </Col>
      ))}
    </Row>
  );
};

export default Categories;

