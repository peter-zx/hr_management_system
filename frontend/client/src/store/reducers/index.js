import { combineReducers } from 'redux';
import authReducer from './authReducer';

// 合并所有 Reducers
const rootReducer = combineReducers({
  auth: authReducer,
});

export default rootReducer;
