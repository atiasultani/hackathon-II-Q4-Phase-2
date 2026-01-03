'use client';

import React, { createContext, useContext, useState, ReactNode, useEffect } from 'react';

interface User {
  id: string;
  email: string;
  name: string;
}

interface AuthContextType {
  user: User | null;
  login: (email: string, password: string) => Promise<void>;
  register: (email: string, password: string, name: string) => Promise<void>;
  logout: () => void;
  loading: boolean;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

interface AuthProviderProps {
  children: ReactNode;
}

export const AuthProvider: React.FC<AuthProviderProps> = ({ children }) => {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  // Check if user is logged in on initial load
  useEffect(() => {
    // In a real implementation, we would check for a valid token here
    // For now, we'll just set loading to false
    setLoading(false);
  }, []);

  const login = async (email: string, password: string) => {
    // In a real implementation, this would call the login API
    // For now, we'll just simulate a successful login
    setUser({
      id: 'user1',
      email,
      name: email.split('@')[0] // Simple name extraction
    });
  };

  const register = async (email: string, password: string, name: string) => {
    // In a real implementation, this would call the register API
    // For now, we'll just simulate a successful registration
    setUser({
      id: 'user1',
      email,
      name
    });
  };

  const logout = () => {
    // In a real implementation, this would clear the token
    setUser(null);
  };

  const value = {
    user,
    login,
    register,
    logout,
    loading
  };

  return (
    <AuthContext.Provider value={value}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (context === undefined) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};