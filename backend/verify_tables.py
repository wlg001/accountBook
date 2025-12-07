"""
验证数据库表结构
"""
from sqlalchemy import inspect, text
from app.core.database import engine, SessionLocal

def verify_database():
    """验证数据库表结构"""
    print("=" * 60)
    print("验证数据库表结构")
    print("=" * 60)
    
    # 创建inspector
    inspector = inspect(engine)
    
    # 获取所有表名
    tables = inspector.get_table_names()
    print(f"\n✅ 成功创建 {len(tables)} 个表:")
    for table in tables:
        print(f"   - {table}")
    
    # 详细检查每个表
    for table_name in tables:
        print(f"\n📋 表: {table_name}")
        print("-" * 60)
        
        # 获取列信息
        columns = inspector.get_columns(table_name)
        print(f"   字段数: {len(columns)}")
        for col in columns:
            nullable = "NULL" if col['nullable'] else "NOT NULL"
            print(f"   - {col['name']}: {col['type']} {nullable}")
        
        # 获取索引
        indexes = inspector.get_indexes(table_name)
        if indexes:
            print(f"\n   索引数: {len(indexes)}")
            for idx in indexes:
                unique = "UNIQUE" if idx['unique'] else ""
                print(f"   - {idx['name']}: {idx['column_names']} {unique}")
        
        # 获取外键
        foreign_keys = inspector.get_foreign_keys(table_name)
        if foreign_keys:
            print(f"\n   外键数: {len(foreign_keys)}")
            for fk in foreign_keys:
                print(f"   - {fk['constrained_columns']} -> {fk['referred_table']}.{fk['referred_columns']}")
    
    # 测试查询
    print("\n" + "=" * 60)
    print("测试基础查询")
    print("=" * 60)
    
    db = SessionLocal()
    try:
        # 测试每个表的查询
        for table in tables:
            result = db.execute(text(f"SELECT COUNT(*) FROM {table}"))
            count = result.scalar()
            print(f"✅ {table}: {count} 条记录")
    finally:
        db.close()
    
    print("\n" + "=" * 60)
    print("数据库验证完成！✅")
    print("=" * 60)

if __name__ == "__main__":
    verify_database()

