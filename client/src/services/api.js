import axios from "axios";

const api = axios.create({
    baseURL: "http://localhost:5000/api"
});

let isRefreshing = false;
let failedQueue = [];

const processQueue = (error, token = null) => {
  failedQueue.forEach(prom => {
    if (error) {
      prom.reject(error);
    } else {
      prom.resolve(token);
    }
  });
  failedQueue = [];
};


api.interceptors.request.use(async (config) => {
    const token = localStorage.getItem("access_token");
    if (token && !config.headers.Authorization) {
        config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
});


api.interceptors.response.use(
    (response) => {
        return response;
    },
    async (error) => {
        const originalRequest = error.config;
        
        if (error.response && error.response.status === 401 && !originalRequest._retry && originalRequest.url !== "/auth/refresh") {
            
            if (isRefreshing) {
                return new Promise(function(resolve, reject) {
                    failedQueue.push({resolve, reject});
                }).then(token => {
                    originalRequest.headers.Authorization = 'Bearer ' + token;
                    return api(originalRequest);
                }).catch(err => {
                    return Promise.reject(err);
                });
            }

            originalRequest._retry = true;
            isRefreshing = true;
            
            try {
                const refreshToken = localStorage.getItem("refresh_token");
                const resp = await api.post("/auth/refresh", {}, {
                    headers: { Authorization: `Bearer ${refreshToken}` }
                });

                const newAccessToken = resp.data.access_token;
                localStorage.setItem("access_token", newAccessToken);
                
                processQueue(null, newAccessToken);
                
                originalRequest.headers.Authorization = `Bearer ${newAccessToken}`;
                return api(originalRequest);
                
            } catch (refreshError) {
                processQueue(refreshError, null);
                console.log("Refresh token expired. Logging out...");
                localStorage.clear();
                window.location.href = "/login";
            } finally {
                isRefreshing = false;
            }
        }
        
        return Promise.reject(error);
    }
);

export default api;