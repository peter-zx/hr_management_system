import axios from 'axios';

// 设置用户登录状态
export const login = (userData) => async (dispatch) => {
  try {
    const response = await axios.post(`${process.env.REACT_APP_API_URL}/api/auth/login`, userData);
    if (response.status === 200) {
      dispatch({
        type: 'LOGIN_SUCCESS',
        payload: response.data,
      });
    }
  } catch (error) {
    dispatch({
      type: 'LOGIN_FAILURE',
      payload: error.message,
    });
  }
};

// 设置用户登出
export const logout = () => {
  return {
    type: 'LOGOUT',
  };
};
