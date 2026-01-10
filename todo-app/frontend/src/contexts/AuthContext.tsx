import React, { createContext, useContext, useState, useEffect, ReactNode } from 'react';
import { useRouter } from 'next/router';
import apiClient from '../services/apiClient';

// Helper function to decode JWT token
const decodeJWT = (token: string) => {
  try {
    const base64Url = token.split('.')[1];
    const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
    const jsonPayload = decodeURIComponent(
      atob(base64)
        .split('')
        .map(c => '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2))
        .join('')
    );

    return JSON.parse(jsonPayload);
  } catch (error) {
    console.error('Error decoding JWT:', error);
    return null;
  }
};

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
  const router = useRouter();

  useEffect(() => {
    // Check if there's a token in localStorage on initial load
    const storedToken = localStorage.getItem('access_token');
    if (storedToken) {
      setToken(storedToken);
      // Decode the stored token to get user ID
      const decodedToken = decodeJWT(storedToken);
      if (decodedToken && decodedToken.sub) {
        // We don't have the email when loading from stored token,
        // but we can set the ID at least
        setUser({
          id: decodedToken.sub,
          email: '', // Email will be unknown when loading from stored token
          created_at: '',
          updated_at: ''
        });
      }
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

        // Decode the JWT to get the user ID from the 'sub' claim
        const decodedToken = decodeJWT(response.access_token);
        if (decodedToken && decodedToken.sub) {
          // Set the user object with the ID from the token and email provided
          setUser({
            id: decodedToken.sub,
            email,
            created_at: '',
            updated_at: ''
          });
        }

        // Redirect to dashboard after successful login
        router.push('/');
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
    // Redirect to login page after logout
    router.push('/login');
  };

  const register = async (email: string, password: string) => {
    try {
      setLoading(true);
      const registerResponse = await apiClient.register(email, password);
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