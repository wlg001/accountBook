"""
测试分类CRUD操作
"""
from app.core.database import SessionLocal
from app.crud import category as category_crud
from app.schemas.category import CategoryCreate, CategoryUpdate
from app.models.category import Category


def test_category_crud():
    """测试分类CRUD操作"""
    print("=" * 60)
    print("测试分类CRUD操作")
    print("=" * 60)
    
    db = SessionLocal()
    try:
        # 测试用户ID（假设用户ID为1）
        test_user_id = 1
        
        # 1. 测试复制系统分类到用户
        print("\n【1. 复制系统分类到用户】")
        category_crud.copy_system_categories_to_user(db, test_user_id)
        user_categories = category_crud.get_categories(db, test_user_id)
        print(f"✓ 已复制 {len(user_categories)} 个分类到用户账户")
        
        # 2. 测试获取分类列表
        print("\n【2. 获取分类列表】")
        all_categories = category_crud.get_categories(db, test_user_id)
        print(f"✓ 用户共有 {len(all_categories)} 个分类")
        
        expense_categories = category_crud.get_categories(db, test_user_id, type="expense")
        print(f"✓ 支出分类: {len(expense_categories)} 个")
        
        income_categories = category_crud.get_categories(db, test_user_id, type="income")
        print(f"✓ 收入分类: {len(income_categories)} 个")
        
        # 3. 测试创建分类
        print("\n【3. 创建新分类】")
        new_category = CategoryCreate(
            name="测试分类",
            type="expense",
            icon="🧪",
            color="#FF0000",
            sort_order=100
        )
        created = category_crud.create_category(db, test_user_id, new_category)
        print(f"✓ 创建分类成功: ID={created.id}, 名称={created.name}")
        
        # 4. 测试获取单个分类
        print("\n【4. 获取单个分类】")
        found = category_crud.get_category(db, created.id, test_user_id)
        if found:
            print(f"✓ 找到分类: {found.name} ({found.type})")
        else:
            print("✗ 未找到分类")
        
        # 5. 测试更新分类
        print("\n【5. 更新分类】")
        update_data = CategoryUpdate(
            name="更新后的测试分类",
            color="#00FF00"
        )
        updated = category_crud.update_category(db, created.id, test_user_id, update_data)
        if updated:
            print(f"✓ 更新成功: {updated.name}, 颜色={updated.color}")
        else:
            print("✗ 更新失败")
        
        # 6. 测试删除分类
        print("\n【6. 删除分类】")
        deleted = category_crud.delete_category(db, created.id, test_user_id)
        if deleted:
            print(f"✓ 删除成功")
        else:
            print("✗ 删除失败")
        
        # 验证删除
        verify = category_crud.get_category(db, created.id, test_user_id)
        if verify is None:
            print("✓ 分类已从数据库中删除")
        else:
            print("✗ 分类仍然存在")
        
        print("\n" + "=" * 60)
        print("✅ 所有测试完成！")
        print("=" * 60)
        
    except Exception as e:
        db.rollback()
        print(f"\n❌ 测试失败: {e}")
        import traceback
        traceback.print_exc()
        raise
    finally:
        db.close()


if __name__ == "__main__":
    test_category_crud()

