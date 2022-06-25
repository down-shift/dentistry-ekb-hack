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

export const getUploadsHistory = (user_id) => {
  return API.get("uploads/", {
    params: {
      tg_user: user_id
    }
  })
}

export const getDentistAdvice = () => {
  return API.get("advice")
}

export default API;



