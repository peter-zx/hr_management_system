import React, { useState } from 'react';
import axios from 'axios';

const UploadPage = () => {
  const [file, setFile] = useState(null);
  const [status, setStatus] = useState('');

  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    if (selectedFile) {
      setFile(selectedFile);
    }
  };

  const handleFileUpload = async (e) => {
    e.preventDefault();

    if (!file) {
      alert('请先选择一个文件');
      return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
      setStatus('上传中...');
      const response = await axios.post(`${process.env.REACT_APP_API_URL}/api/document/upload`, formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      if (response.status === 200) {
        setStatus('文件上传成功');
      }
    } catch (error) {
      setStatus('文件上传失败');
      console.error('文件上传失败', error);
    }
  };

  return (
    <div>
      <h2>文件上传</h2>
      <form onSubmit={handleFileUpload}>
        <input type="file" onChange={handleFileChange} />
        <button type="submit">上传</button>
      </form>
      {status && <p>{status}</p>}
    </div>
  );
};

export default UploadPage;
