import axios from "axios";

// Create an axios instance with a base URL
const axiosInstance = axios.create({
    baseURL: 'http://localhost:3000/',
});

// Request interceptor
axiosInstance.interceptors.request.use(
    (config) => {
        config.headers['Authorization'] = `Bearer ${localStorage.getItem('token')}` ;// Example authorization header
        return config;
    },
    (error) => {
        console.log('Request error', error);
        return Promise.reject(error);
    }
);

// Response interceptor
axiosInstance.interceptors.response.use(
    (response) => {
        return response; // Return the response if successful
    },
    (error) => {
        console.log('Response error', error);
        return Promise.reject(error);
    }
);

export default axiosInstance;
