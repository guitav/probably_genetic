import axios from "axios";
const API_ENDPOINT =
  process.env.NODE_ENV === "development"
    ? "http://localhost:8000/"
    : "http://ec2-3-80-140-96.compute-1.amazonaws.com:8080/";

const instance = axios.create({ baseURL: API_ENDPOINT });
instance.CancelToken = axios.CancelToken;
instance.isCancel = axios.isCancel;
instance.withCredentials = true;
export default instance;
