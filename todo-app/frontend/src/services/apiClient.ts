import axios, { AxiosInstance, AxiosRequestConfig } from 'axios';

class ApiClient {
  private client: AxiosInstance;

  constructor() {
    this.client = axios.create({
      baseURL: process.env.NEXT_PUBLIC_API_BASE_URL || 'https://asultani-todo-app.hf.space',
      timeout: 10000,
      headers: {
        'Content-Type': 'application/json',
      },
    });

    // Add request interceptor to include JWT token
    this.client.interceptors.request.use(
      (config) => {
        const token = localStorage.getItem('access_token');
        if (token) {
          config.headers.Authorization = `Bearer ${token}`;
        }
        return config;
      },
      (error) => {
        return Promise.reject(error);
      }
    );

    // Add response interceptor to handle token expiration
    this.client.interceptors.response.use(
      (response) => {
        return response;
      },
      (error) => {
        if (error.response?.status === 401) {
          // Token might be expired, clear it and redirect to login
          localStorage.removeItem('access_token');
          window.location.href = '/login';
        }
        return Promise.reject(error);
      }
    );
  }

  // Authentication methods
  async register(email: string, password: string) {
    try {
      const response = await this.client.post('/api/auth/register', {
        email,
        password,
      });
      return response.data;
    } catch (error) {
      throw error;
    }
  }

  async login(email: string, password: string) {
    try {
      // For login, we need to use the default axios instance without the auth header
      const response = await axios.post(`${process.env.NEXT_PUBLIC_API_BASE_URL || 'http://localhost:8000'}/api/auth/login`, {
        username: email,  // Using username for email field
        password,
      }, {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
      });

      // Store the token
      if (response.data.access_token) {
        localStorage.setItem('access_token', response.data.access_token);
      }

      return response.data;
    } catch (error) {
      throw error;
    }
  }

  async logout() {
    try {
      await this.client.post('/api/auth/logout');
    } finally {
      // Always remove the token regardless of API response
      localStorage.removeItem('access_token');
    }
  }

  // Task methods
  async getUserTasks(userId: string) {
    try {
      const response = await this.client.get(`/api/${userId}/tasks`);
      return response.data;
    } catch (error) {
      throw error;
    }
  }

  async createTask(userId: string, taskData: { title: string; description?: string }) {
    try {
      const response = await this.client.post(`/api/${userId}/tasks`, taskData);
      return response.data;
    } catch (error) {
      throw error;
    }
  }

  async updateTask(userId: string, taskId: string, taskData: { title?: string; description?: string }) {
    try {
      const response = await this.client.put(`/api/${userId}/tasks/${taskId}`, taskData);
      return response.data;
    } catch (error) {
      throw error;
    }
  }

  async deleteTask(userId: string, taskId: string) {
    try {
      const response = await this.client.delete(`/api/${userId}/tasks/${taskId}`);
      return response.data;
    } catch (error) {
      throw error;
    }
  }

  async toggleTaskCompletion(userId: string, taskId: string, completed: boolean) {
    try {
      const response = await this.client.patch(`/api/${userId}/tasks/${taskId}/complete`, {
        completed
      });
      return response.data;
    } catch (error) {
      throw error;
    }
  }

  // Generic request method
  async request<T>(config: AxiosRequestConfig): Promise<T> {
    const response = await this.client.request<T>(config);
    return response.data;
  }
}

export default new ApiClient();
