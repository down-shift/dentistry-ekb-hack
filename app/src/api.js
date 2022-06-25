import axios from "axios";


axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";


export const API = axios.create({
  baseURL: "/api/",
  headers: {
    "Content-Type": "application/json",
    "Accept-Language": "ru-RU",
  },
});

export const analyseImage = (fd) => {
  return API.post("detect/", fd);
}

export default API;



