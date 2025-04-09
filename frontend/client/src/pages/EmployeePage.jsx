import React, { useEffect, useState } from 'react';
import axios from 'axios';

const EmployeePage = () => {
  const [employees, setEmployees] = useState([]);

  useEffect(() => {
    const fetchEmployees = async () => {
      try {
        const response = await axios.get(`${process.env.REACT_APP_API_URL}/api/employee`);
        setEmployees(response.data);
      } catch (error) {
        console.error('获取员工数据失败', error);
      }
    };

    fetchEmployees();
  }, []);

  return (
    <div>
      <h2>员工管理</h2>
      <ul>
        {employees.map((employee) => (
          <li key={employee.id}>
            {employee.name} - {employee.id_number}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default EmployeePage;
