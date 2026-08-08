import axios from "axios";

const api = axios.create({
    baseURL: "http://localhost:5000/api"
});

api.interceptors.request.use(async (config) => {
    const token = localStorage.getItem("access_token");
    if (token) {
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
        
        if (error.response && error.response.status === 401 && !originalRequest._retry) {
            
            originalRequest._retry = true;
            
            try {
                const refreshToken = localStorage.getItem("refresh_token");
                
                const resp = await api.post("/auth/refresh", {}, {
                    headers: { Authorization: `Bearer ${refreshToken}` }
                });

                const newAccessToken = resp.data.access_token;
                localStorage.setItem("access_token", newAccessToken);
                
                originalRequest.headers.Authorization = `Bearer ${newAccessToken}`;
                return api(originalRequest);
                
            } catch (refreshError) {
                console.log("Refresh token expired. Logging out...");
                localStorage.clear();
                window.location.href = "/login";
            }
        }
        
        return Promise.reject(error);
    }
);

export default api;

