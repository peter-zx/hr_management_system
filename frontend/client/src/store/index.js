import { createStore, applyMiddleware } from 'redux';
import thunk from 'redux-thunk'; // 用于异步操作
import rootReducer from './reducers';

// 创建 Redux Store
const store = createStore(rootReducer, applyMiddleware(thunk));

export default store;
