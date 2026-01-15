import React, { useState, useEffect } from 'react';
import TaskItem from './TaskItem';
import apiClient from '../services/apiClient';

interface TaskListProps {
  userId: string;
  refreshSignal?: number;   // ✅ ADD THIS
}

const TaskList: React.FC<TaskListProps> = ({ userId , refreshSignal}) => {
  const [tasks, setTasks] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    loadTasks();
  }, [userId refreshSignal]);

  const loadTasks = async () => {
    setLoading(true);
    setError('');

    try {
      const userTasks = await apiClient.getUserTasks(userId);
      setTasks(userTasks);
    } catch (err: any) {
      // Ensure we only set string values to error state
      const errorMessage = err.response?.data?.detail || 'Failed to load tasks. Please try again.';
      setError(typeof errorMessage === 'string' ? errorMessage : 'Failed to load tasks. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  const handleTaskUpdated = (updatedTask: any) => {
    setTasks(prevTasks =>
      prevTasks.map(task => task.id === updatedTask.id ? updatedTask : task)
    );
  };

  const handleTaskDeleted = (deletedTaskId: string) => {
    setTasks(prevTasks =>
      prevTasks.filter(task => task.id !== deletedTaskId)
    );
  };

  if (loading) {
    return (
      <div className="flex justify-center items-center h-32">
        <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-indigo-600"></div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="p-4 bg-red-50 text-red-700 rounded">
        {error}
        <button
          onClick={loadTasks}
          className="ml-4 px-3 py-1 bg-red-100 rounded text-sm hover:bg-red-200"
        >
          Retry
        </button>
      </div>
    );
  }

  if (tasks.length === 0) {
    return (
      <div className="p-6 text-center text-gray-500">
        <p>No tasks yet. Create your first task!</p>
      </div>
    );
  }

  return (
    <div className="mt-4">
      <h2 className="text-xl font-semibold mb-4">Your Tasks</h2>
      <div>
        {tasks.map((task) => (
          <TaskItem
            key={task.id}
            task={task}
            userId={userId}
            onTaskUpdated={handleTaskUpdated}
            onTaskDeleted={handleTaskDeleted}
          />
        ))}
      </div>
    </div>
  );
};

export default TaskList;
