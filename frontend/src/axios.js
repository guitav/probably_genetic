import axios from 'axios';

const instance = axios.create({
  baseURL: 'http://localhost:8000/'
});
instance.CancelToken = axios.CancelToken;
instance.isCancel = axios.isCancel;
instance.withCredentials = true
export default instance
