"""
测试数据库模型定义
"""
from app.models import User, Category, Transaction, Budget
from app.core.database import Base, engine


def test_models_definition():
    """测试所有模型是否正确定义"""
    print("=" * 50)
    print("测试数据库模型定义")
    print("=" * 50)
    
    models = [User, Category, Transaction, Budget]
    
    for model in models:
        print(f"\n✓ {model.__name__} 模型定义成功")
        print(f"  表名: {model.__tablename__}")
        print(f"  字段数: {len(model.__table__.columns)}")
        
        # 列出所有字段
        print(f"  字段列表:")
        for column in model.__table__.columns:
            nullable = "NULL" if column.nullable else "NOT NULL"
            primary = "PK" if column.primary_key else ""
            foreign = "FK" if column.foreign_keys else ""
            unique = "UNIQUE" if column.unique else ""
            flags = " ".join(filter(None, [primary, foreign, unique, nullable]))
            print(f"    - {column.name}: {column.type} [{flags}]")
    
    print("\n" + "=" * 50)
    print("所有模型定义正确！✓")
    print("=" * 50)
    return True


def test_create_tables():
    """测试创建数据库表"""
    print("\n" + "=" * 50)
    print("测试创建数据库表")
    print("=" * 50)
    
    try:
        # 创建所有表
        Base.metadata.create_all(bind=engine)
        print("\n✓ 数据库表创建成功！")
        
        # 列出所有表
        print("\n创建的表:")
        for table_name in Base.metadata.tables.keys():
            print(f"  - {table_name}")
        
        print("\n" + "=" * 50)
        print("数据库表创建测试通过！✓")
        print("=" * 50)
        return True
        
    except Exception as e:
        print(f"\n✗ 创建表失败: {e}")
        print("\n" + "=" * 50)
        print("数据库表创建测试失败！✗")
        print("=" * 50)
        return False


if __name__ == "__main__":
    # 测试模型定义
    test_models_definition()
    
    # 测试创建表
    test_create_tables()

