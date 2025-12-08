"""
测试分类API接口
"""
import requests
import json

BASE_URL = "http://localhost:8000/api/v1"
TOKEN = None


def login():
    """登录获取Token"""
    global TOKEN
    url = f"{BASE_URL}/auth/login"
    data = {
        "username": "testuser",  # 假设这个用户存在
        "password": "testpass123"
    }
    response = requests.post(url, json=data)
    if response.status_code == 200:
        result = response.json()
        TOKEN = result["data"]["access_token"]
        print(f"✅ 登录成功，Token: {TOKEN[:20]}...")
        return True
    else:
        print(f"❌ 登录失败: {response.status_code} - {response.text}")
        return False


def get_headers():
    """获取请求头"""
    return {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }


def test_get_categories():
    """测试获取分类列表"""
    print("\n【测试 GET /api/v1/categories】")
    url = f"{BASE_URL}/categories"
    response = requests.get(url, headers=get_headers())
    print(f"状态码: {response.status_code}")
    if response.status_code == 200:
        result = response.json()
        print(f"✅ 获取成功，共 {len(result['data'])} 个分类")
        return True
    else:
        print(f"❌ 获取失败: {response.text}")
        return False


def test_get_categories_by_type():
    """测试按类型筛选分类"""
    print("\n【测试 GET /api/v1/categories?type=expense】")
    url = f"{BASE_URL}/categories?type=expense"
    response = requests.get(url, headers=get_headers())
    print(f"状态码: {response.status_code}")
    if response.status_code == 200:
        result = response.json()
        print(f"✅ 获取成功，支出分类: {len(result['data'])} 个")
        return True
    else:
        print(f"❌ 获取失败: {response.text}")
        return False


def test_create_category():
    """测试创建分类"""
    print("\n【测试 POST /api/v1/categories】")
    url = f"{BASE_URL}/categories"
    data = {
        "name": "测试分类API",
        "type": "expense",
        "icon": "🧪",
        "color": "#FF0000",
        "sort_order": 100
    }
    response = requests.post(url, json=data, headers=get_headers())
    print(f"状态码: {response.status_code}")
    if response.status_code == 201:
        result = response.json()
        category_id = result["data"]["id"]
        print(f"✅ 创建成功，分类ID: {category_id}")
        return category_id
    else:
        print(f"❌ 创建失败: {response.text}")
        return None


def test_get_category(category_id):
    """测试获取单个分类"""
    print(f"\n【测试 GET /api/v1/categories/{category_id}】")
    url = f"{BASE_URL}/categories/{category_id}"
    response = requests.get(url, headers=get_headers())
    print(f"状态码: {response.status_code}")
    if response.status_code == 200:
        result = response.json()
        print(f"✅ 获取成功: {result['data']['name']}")
        return True
    else:
        print(f"❌ 获取失败: {response.text}")
        return False


def test_update_category(category_id):
    """测试更新分类"""
    print(f"\n【测试 PUT /api/v1/categories/{category_id}】")
    url = f"{BASE_URL}/categories/{category_id}"
    data = {
        "name": "更新后的测试分类",
        "color": "#00FF00"
    }
    response = requests.put(url, json=data, headers=get_headers())
    print(f"状态码: {response.status_code}")
    if response.status_code == 200:
        result = response.json()
        print(f"✅ 更新成功: {result['data']['name']}, 颜色: {result['data']['color']}")
        return True
    else:
        print(f"❌ 更新失败: {response.text}")
        return False


def test_delete_category(category_id):
    """测试删除分类"""
    print(f"\n【测试 DELETE /api/v1/categories/{category_id}】")
    url = f"{BASE_URL}/categories/{category_id}"
    response = requests.delete(url, headers=get_headers())
    print(f"状态码: {response.status_code}")
    if response.status_code == 200:
        print(f"✅ 删除成功")
        return True
    else:
        print(f"❌ 删除失败: {response.text}")
        return False


def main():
    """主测试函数"""
    print("=" * 60)
    print("测试分类API接口")
    print("=" * 60)
    
    # 登录
    if not login():
        print("\n❌ 无法登录，请先创建测试用户")
        print("提示: 可以通过 /api/v1/auth/register 注册用户")
        return
    
    # 测试获取分类列表
    test_get_categories()
    
    # 测试按类型筛选
    test_get_categories_by_type()
    
    # 测试创建分类
    category_id = test_create_category()
    if category_id:
        # 测试获取单个分类
        test_get_category(category_id)
        
        # 测试更新分类
        test_update_category(category_id)
        
        # 测试删除分类
        test_delete_category(category_id)
    
    print("\n" + "=" * 60)
    print("✅ 测试完成！")
    print("=" * 60)


if __name__ == "__main__":
    main()

