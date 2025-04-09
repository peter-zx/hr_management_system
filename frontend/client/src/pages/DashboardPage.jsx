import React, { useEffect, useState } from 'react';
import axios from 'axios';

const DashboardPage = () => {
  const [summary, setSummary] = useState({});

  useEffect(() => {
    const fetchSummary = async () => {
      try {
        const response = await axios.get(`${process.env.REACT_APP_API_URL}/api/dashboard/summary`);
        setSummary(response.data);
      } catch (error) {
        console.error('获取数据失败', error);
      }
    };

    fetchSummary();
  }, []);

  return (
    <div>
      <h2>仪表盘</h2>
      <p>员工总数: {summary.total_employees}</p>
      <p>分配记录总数: {summary.total_assignments}</p>
      <p>总薪资: {summary.total_salary}</p>
    </div>
  );
};

export default DashboardPage;
