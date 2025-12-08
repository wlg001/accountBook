import { Card, Button } from 'antd';
import { useAuthStore } from '../../store/authStore';
import { useNavigate } from 'react-router-dom';

const Dashboard = () => {
  const { user, logout } = useAuthStore();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  return (
    <div style={{ padding: '24px', minHeight: '100vh', background: '#f0f2f5' }}>
      <Card
        title="🎉 欢迎使用记账本"
        extra={<Button onClick={handleLogout}>退出登录</Button>}
        style={{ maxWidth: 800, margin: '0 auto' }}
      >
        <h2>👋 你好，{user?.nickname || user?.username}！</h2>
        
        <p>✅ 恭喜你！用户认证系统已经完整实现。</p>
        
        <div style={{ marginTop: 24, padding: 16, background: '#f6f8fa', borderRadius: 8 }}>
          <h3>📊 当前功能状态</h3>
          <ul>
            <li>✅ 用户注册</li>
            <li>✅ 用户登录</li>
            <li>✅ 自动登录（Token持久化）</li>
            <li>✅ 路由守卫（权限控制）</li>
            <li>✅ 退出登录</li>
          </ul>
        </div>

        <div style={{ marginTop: 24, padding: 16, background: '#fff7e6', borderRadius: 8 }}>
          <h3>🚀 即将推出的功能</h3>
          <ul>
            <li>⏳ 分类管理（Sprint 2）</li>
            <li>⏳ 快速记账（Sprint 3）</li>
            <li>⏳ 账目列表（Sprint 3）</li>
            <li>⏳ 数据统计（Sprint 4）</li>
          </ul>
        </div>

        <div style={{ marginTop: 24 }}>
          <h3>ℹ️ 你的信息</h3>
          <p>用户名: {user?.username}</p>
          <p>邮箱: {user?.email}</p>
          <p>昵称: {user?.nickname || '未设置'}</p>
          <p>注册时间: {new Date(user?.created_at || '').toLocaleString('zh-CN')}</p>
        </div>
      </Card>
    </div>
  );
};

export default Dashboard;

