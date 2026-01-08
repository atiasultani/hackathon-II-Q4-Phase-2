import React, { createContext, useContext, useState, useEffect, ReactNode } from 'react';
import apiClient from '../services/apiClient';

interface User {
  id: string;
  email: string;
  created_at: string;
  updated_at: string;
}

interface AuthContextType {
  user: User | null;
  token: string | null;
  login: (email: string, password: string) => Promise<void>;
  logout: () => void;
  register: (email: string, password: string) => Promise<void>;
  loading: boolean;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};

interface AuthProviderProps {
  children: ReactNode;
}

export const AuthProvider: React.FC<AuthProviderProps> = ({ children }) => {
  const [user, setUser] = useState<User | null>(null);
  const [token, setToken] = useState<string | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Check if there's a token in localStorage on initial load
    const storedToken = localStorage.getItem('access_token');
    if (storedToken) {
      setToken(storedToken);
      // You might want to validate the token or fetch user info here
    }
    setLoading(false);
  }, []);

  const login = async (email: string, password: string) => {
    try {
      setLoading(true);
      const response = await apiClient.login(email, password);
      if (response.access_token) {
        setToken(response.access_token);
        localStorage.setItem('access_token', response.access_token);
        // You might want to fetch user info here
      }
    } catch (error) {
      throw error;
    } finally {
      setLoading(false);
    }
  };

  const logout = () => {
    apiClient.logout();
    setToken(null);
    setUser(null);
    localStorage.removeItem('access_token');
  };

  const register = async (email: string, password: string) => {
    try {
      setLoading(true);
      await apiClient.register(email, password);
      // Automatically log in after registration
      await login(email, password);
    } catch (error) {
      throw error;
    } finally {
      setLoading(false);
    }
  };

  const value = {
    user,
    token,
    login,
    logout,
    register,
    loading,
  };

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
};