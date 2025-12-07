import { ConfigProvider } from 'antd';
import zhCN from 'antd/locale/zh_CN';
import { APP_TITLE } from './utils/constants';

function App() {
  return (
    <ConfigProvider
      locale={zhCN}
      theme={{
        token: {
          colorPrimary: '#1890ff',
          colorSuccess: '#52c41a',
          colorError: '#ff4d4f',
          colorWarning: '#faad14',
          borderRadius: 8,
        },
      }}
    >
      <div className="App">
        <h1>{APP_TITLE}</h1>
        <p>前端项目初始化成功！</p>
        <p>技术栈：React + TypeScript + Vite + Ant Design</p>
      </div>
    </ConfigProvider>
  );
}

export default App;
