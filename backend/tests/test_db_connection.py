"""
测试数据库连接
"""
from sqlalchemy import text
from app.core.database import engine, SessionLocal
from app.core.config import settings

def test_database_connection():
    """测试数据库连接是否正常"""
    print("=" * 50)
    print("测试数据库连接")
    print("=" * 50)
    
    print(f"\n数据库URL: {settings.DATABASE_URL}")
    
    try:
        # 测试创建会话
        db = SessionLocal()
        print("✓ 成功创建数据库会话")
        
        # 测试执行查询
        result = db.execute(text("SELECT 1"))
        print("✓ 成功执行测试查询")
        print(f"  查询结果: {result.scalar()}")
        
        # 关闭会话
        db.close()
        print("✓ 成功关闭数据库会话")
        
        print("\n" + "=" * 50)
        print("数据库连接测试通过！✓")
        print("=" * 50)
        return True
        
    except Exception as e:
        print(f"\n✗ 数据库连接失败: {e}")
        print("\n" + "=" * 50)
        print("数据库连接测试失败！✗")
        print("=" * 50)
        return False

if __name__ == "__main__":
    test_database_connection()

