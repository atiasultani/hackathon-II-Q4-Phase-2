import React, { useState, useEffect } from 'react';
import { useAuth } from '../contexts/AuthContext';
import TaskForm from '../components/TaskForm';
import TaskList from '../components/TaskList';
import apiClient from '../services/apiClient';

const DashboardPage: React.FC = () => {
  const { user, logout, loading } = useAuth();
  const [showTaskForm, setShowTaskForm] = useState(false);

  useEffect(() => {
    if (!loading && !user) {
      // Redirect to login if not authenticated
      window.location.href = '/login';
    }
  }, [user, loading]);

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-indigo-600"></div>
      </div>
    );
  }

  if (!user) {
    return null; // Redirect happens in useEffect
  }

  const handleTaskCreated = () => {
    setShowTaskForm(false);
  };

  return (
    <div className="min-h-screen bg-gray-50">
      <nav className="bg-white shadow">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between h-16">
            <div className="flex items-center">
              <h1 className="text-xl font-bold text-gray-900">Todo App</h1>
            </div>
            <div className="flex items-center space-x-4">
              <span className="text-sm text-gray-700">Welcome, {user.email}</span>
              <button
                onClick={logout}
                className="px-4 py-2 text-sm font-medium text-white bg-red-600 border border-transparent rounded-md hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500"
              >
                Logout
              </button>
            </div>
          </div>
        </div>
      </nav>

      <main className="max-w-4xl mx-auto py-6 sm:px-6 lg:px-8">
        <div className="px-4 py-6 sm:px-0">
          <div className="flex justify-between items-center mb-6">
            <h2 className="text-2xl font-bold text-gray-900">My Tasks</h2>
            <button
              onClick={() => setShowTaskForm(!showTaskForm)}
              className="px-4 py-2 text-sm font-medium text-white bg-indigo-600 border border-transparent rounded-md hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
            >
              {showTaskForm ? 'Cancel' : 'Add Task'}
            </button>
          </div>

          {showTaskForm && (
            <div className="mb-8">
              <TaskForm
                userId={user.id}
                onTaskCreated={handleTaskCreated}
                onCancel={() => setShowTaskForm(false)}
              />
            </div>
          )}

          <div className="bg-white overflow-hidden shadow rounded-lg">
            <div className="px-4 py-5 sm:p-6">
              <TaskList userId={user.id} />
            </div>
          </div>
        </div>
      </main>
    </div>
  );
};

export default DashboardPage;