import React, { useState } from 'react';
import apiClient from '../services/apiClient';

interface TaskItemProps {
  task: {
    id: string;
    title: string;
    description?: string;
    completed: boolean;
    created_at: string;
    updated_at: string;
  };
  userId: string;
  onTaskUpdated?: (updatedTask: any) => void;
  onTaskDeleted?: (taskId: string) => void;
}

const TaskItem: React.FC<TaskItemProps> = ({ task, userId, onTaskUpdated, onTaskDeleted }) => {
  const [isEditing, setIsEditing] = useState(false);
  const [editData, setEditData] = useState({
    title: task.title,
    description: task.description || ''
  });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleToggleComplete = async () => {
    setLoading(true);
    setError('');

    try {
      const updatedTask = await apiClient.toggleTaskCompletion(userId, task.id, !task.completed);
      if (onTaskUpdated) {
        onTaskUpdated(updatedTask);
      }
    } catch (err: any) {
      // Ensure we only set string values to error state
      const errorMessage = err.response?.data?.detail || 'Failed to update task. Please try again.';
      setError(typeof errorMessage === 'string' ? errorMessage : 'Failed to update task. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  const handleDelete = async () => {
    if (!window.confirm('Are you sure you want to delete this task?')) {
      return;
    }

    setLoading(true);
    setError('');

    try {
      await apiClient.deleteTask(userId, task.id);
      if (onTaskDeleted) {
        onTaskDeleted(task.id);
      }
    } catch (err: any) {
      // Ensure we only set string values to error state
      const errorMessage = err.response?.data?.detail || 'Failed to delete task. Please try again.';
      setError(typeof errorMessage === 'string' ? errorMessage : 'Failed to delete task. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  const handleEdit = async () => {
    setLoading(true);
    setError('');

    try {
      const updatedTask = await apiClient.updateTask(userId, task.id, {
        title: editData.title,
        description: editData.description
      });
      if (onTaskUpdated) {
        onTaskUpdated(updatedTask);
      }
      setIsEditing(false);
    } catch (err: any) {
      // Ensure we only set string values to error state
      const errorMessage = err.response?.data?.detail || 'Failed to update task. Please try again.';
      setError(typeof errorMessage === 'string' ? errorMessage : 'Failed to update task. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className={`p-4 mb-3 border rounded-md shadow-sm ${task.completed ? 'bg-green-50' : 'bg-white'}`}>
      {error && (
        <div className="mb-2 p-2 bg-red-50 text-red-700 rounded text-sm">
          {error}
        </div>
      )}

      {isEditing ? (
        <div className="space-y-3">
          <input
            type="text"
            value={editData.title}
            onChange={(e) => setEditData({ ...editData, title: e.target.value })}
            className="w-full px-2 py-1 border border-gray-300 rounded text-sm"
            placeholder="Task title"
          />
          <textarea
            value={editData.description}
            onChange={(e) => setEditData({ ...editData, description: e.target.value })}
            className="w-full px-2 py-1 border border-gray-300 rounded text-sm"
            placeholder="Task description"
            rows={2}
          />
          <div className="flex justify-end space-x-2">
            <button
              onClick={() => setIsEditing(false)}
              className="px-3 py-1 text-xs bg-gray-200 rounded hover:bg-gray-300"
              disabled={loading}
            >
              Cancel
            </button>
            <button
              onClick={handleEdit}
              className="px-3 py-1 text-xs bg-indigo-600 text-white rounded hover:bg-indigo-700"
              disabled={loading}
            >
              Save
            </button>
          </div>
        </div>
      ) : (
        <div>
          <div className="flex items-start">
            <input
              type="checkbox"
              checked={task.completed}
              onChange={handleToggleComplete}
              disabled={loading}
              className="mt-1 mr-2"
            />
            <div className="flex-1">
              <h3 className={`text-lg ${task.completed ? 'line-through text-gray-500' : ''}`}>
                {task.title}
              </h3>
              {task.description && (
                <p className={`mt-1 text-gray-600 ${task.completed ? 'line-through' : ''}`}>
                  {task.description}
                </p>
              )}
            </div>
            <div className="flex space-x-1">
              <button
                onClick={() => setIsEditing(true)}
                className="p-1 text-xs bg-blue-100 text-blue-700 rounded hover:bg-blue-200"
                disabled={loading}
              >
                Edit
              </button>
              <button
                onClick={handleDelete}
                className="p-1 text-xs bg-red-100 text-red-700 rounded hover:bg-red-200"
                disabled={loading}
              >
                Delete
              </button>
            </div>
          </div>
          <div className="mt-2 text-xs text-gray-500">
            Created: {new Date(task.created_at).toLocaleDateString()}
            {task.completed && ' | Completed'}
          </div>
        </div>
      )}
    </div>
  );
};

export default TaskItem;