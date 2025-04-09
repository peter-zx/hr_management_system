import { render, screen } from '@testing-library/react';
import EmployeePage from '../pages/EmployeePage';  // 导入 EmployeePage 组件
import axios from 'axios';

// 模拟 axios 请求
jest.mock('axios');

describe('EmployeePage', () => {
  it('应该渲染员工列表', async () => {
    // 模拟返回的员工数据
    axios.get.mockResolvedValue({
      data: [
        { id: 1, name: '张三', id_number: '123456' },
        { id: 2, name: '李四', id_number: '654321' },
      ],
    });

    render(<EmployeePage />);

    // 等待并检查页面中是否显示员工名称
    expect(await screen.findByText('张三')).toBeInTheDocument();
    expect(await screen.findByText('李四')).toBeInTheDocument();
  });

  it('显示加载失败的错误', async () => {
    axios.get.mockRejectedValue(new Error('加载员工数据失败'));

    render(<EmployeePage />);

    // 检查是否显示了错误消息
    expect(await screen.findByText('加载失败')).toBeInTheDocument();
  });
});
