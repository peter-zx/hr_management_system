import { render, screen, fireEvent } from '@testing-library/react';
import UploadPage from '../pages/UploadPage';  // 导入 UploadPage 组件
import axios from 'axios';

// 模拟 axios 请求
jest.mock('axios');

describe('UploadPage', () => {
  it('应该成功上传文件', async () => {
    // 模拟文件上传的成功响应
    axios.post.mockResolvedValue({ status: 200 });

    render(<UploadPage />);

    const fileInput = screen.getByLabelText('选择文件');
    const file = new File(['dummy content'], 'testfile.txt', { type: 'text/plain' });

    fireEvent.change(fileInput, { target: { files: [file] } });

    const uploadButton = screen.getByText('上传');
    fireEvent.click(uploadButton);

    // 检查是否显示了上传成功的消息
    expect(await screen.findByText('文件上传成功')).toBeInTheDocument();
  });

  it('上传失败时应该显示错误信息', async () => {
    // 模拟文件上传的失败响应
    axios.post.mockRejectedValue(new Error('上传失败'));

    render(<UploadPage />);

    const fileInput = screen.getByLabelText('选择文件');
    const file = new File(['dummy content'], 'testfile.txt', { type: 'text/plain' });

    fireEvent.change(fileInput, { target: { files: [file] } });

    const uploadButton = screen.getByText('上传');
    fireEvent.click(uploadButton);

    // 检查是否显示了上传失败的消息
    expect(await screen.findByText('文件上传失败')).toBeInTheDocument();
  });
});
