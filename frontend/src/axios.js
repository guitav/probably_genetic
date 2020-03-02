import axios from 'axios';
const API_ENDPOINT = 'http://localhost:8080/'

const instance = axios.create({baseURL: API_ENDPOINT});
instance.CancelToken = axios.CancelToken;
instance.isCancel = axios.isCancel;
instance.withCredentials = true
export default instance
