"""
初始化系统预设分类数据
"""
from app.core.database import SessionLocal
from app.models.category import Category
from sqlalchemy import text

# 系统预设分类数据
SYSTEM_CATEGORIES = [
    # 支出分类
    {
        "name": "餐饮",
        "type": "expense",
        "icon": "🍜",
        "color": "#FF6B6B",
        "sort_order": 1,
    },
    {
        "name": "交通",
        "type": "expense",
        "icon": "🚌",
        "color": "#4ECDC4",
        "sort_order": 2,
    },
    {
        "name": "购物",
        "type": "expense",
        "icon": "🛍️",
        "color": "#FFE66D",
        "sort_order": 3,
    },
    {
        "name": "娱乐",
        "type": "expense",
        "icon": "🎬",
        "color": "#A8E6CF",
        "sort_order": 4,
    },
    {
        "name": "医疗",
        "type": "expense",
        "icon": "🏥",
        "color": "#FF8B94",
        "sort_order": 5,
    },
    {
        "name": "教育",
        "type": "expense",
        "icon": "📚",
        "color": "#C7CEEA",
        "sort_order": 6,
    },
    {
        "name": "住房",
        "type": "expense",
        "icon": "🏠",
        "color": "#B4A7D6",
        "sort_order": 7,
    },
    {
        "name": "其他",
        "type": "expense",
        "icon": "📦",
        "color": "#95E1D3",
        "sort_order": 8,
    },
    # 收入分类
    {
        "name": "工资",
        "type": "income",
        "icon": "💰",
        "color": "#52C41A",
        "sort_order": 1,
    },
    {
        "name": "奖金",
        "type": "income",
        "icon": "🎁",
        "color": "#73D13D",
        "sort_order": 2,
    },
    {
        "name": "投资",
        "type": "income",
        "icon": "📈",
        "color": "#95DE64",
        "sort_order": 3,
    },
    {
        "name": "兼职",
        "type": "income",
        "icon": "💼",
        "color": "#B7EB8F",
        "sort_order": 4,
    },
    {
        "name": "其他",
        "type": "income",
        "icon": "💵",
        "color": "#D9F7BE",
        "sort_order": 5,
    },
]


def init_system_categories():
    """初始化系统预设分类"""
    print("=" * 60)
    print("初始化系统预设分类数据")
    print("=" * 60)
    
    db = SessionLocal()
    try:
        # 检查是否已经初始化过
        existing_count = db.query(Category).filter(Category.is_system == True).count()
        if existing_count > 0:
            print(f"\n⚠️  系统分类已存在 ({existing_count} 个)，跳过初始化")
            print("如需重新初始化，请先删除现有的系统分类")
            return
        
        # 插入系统分类
        print(f"\n正在插入 {len(SYSTEM_CATEGORIES)} 个系统预设分类...")
        
        expense_count = 0
        income_count = 0
        
        for cat_data in SYSTEM_CATEGORIES:
            category = Category(
                user_id=None,  # 系统分类user_id为NULL
                name=cat_data["name"],
                type=cat_data["type"],
                icon=cat_data["icon"],
                color=cat_data["color"],
                is_system=True,  # 标记为系统分类
                sort_order=cat_data["sort_order"],
            )
            db.add(category)
            
            if cat_data["type"] == "expense":
                expense_count += 1
                print(f"  ✓ 支出分类: {cat_data['icon']} {cat_data['name']} ({cat_data['color']})")
            else:
                income_count += 1
                print(f"  ✓ 收入分类: {cat_data['icon']} {cat_data['name']} ({cat_data['color']})")
        
        # 提交到数据库
        db.commit()
        
        print("\n" + "=" * 60)
        print(f"✅ 系统分类初始化成功!")
        print(f"   支出分类: {expense_count} 个")
        print(f"   收入分类: {income_count} 个")
        print(f"   总计: {expense_count + income_count} 个")
        print("=" * 60)
        
        # 验证数据
        print("\n验证数据库中的分类...")
        all_categories = db.query(Category).filter(Category.is_system == True).all()
        print(f"✓ 数据库中共有 {len(all_categories)} 个系统分类")
        
    except Exception as e:
        db.rollback()
        print(f"\n❌ 初始化失败: {e}")
        raise
    finally:
        db.close()


def show_categories():
    """显示所有系统分类"""
    print("\n" + "=" * 60)
    print("系统分类列表")
    print("=" * 60)
    
    db = SessionLocal()
    try:
        # 支出分类
        expense_categories = db.query(Category).filter(
            Category.is_system == True,
            Category.type == "expense"
        ).order_by(Category.sort_order).all()
        
        print("\n【支出分类】")
        for cat in expense_categories:
            print(f"  {cat.icon} {cat.name:6s} - {cat.color}")
        
        # 收入分类
        income_categories = db.query(Category).filter(
            Category.is_system == True,
            Category.type == "income"
        ).order_by(Category.sort_order).all()
        
        print("\n【收入分类】")
        for cat in income_categories:
            print(f"  {cat.icon} {cat.name:6s} - {cat.color}")
        
        print("\n" + "=" * 60)
        
    finally:
        db.close()


if __name__ == "__main__":
    # 初始化系统分类
    init_system_categories()
    
    # 显示分类列表
    show_categories()

