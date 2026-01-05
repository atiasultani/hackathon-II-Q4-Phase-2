'use client';

import React, { useState } from 'react';
import { Task } from '../types/task';

interface TaskItemProps {
  task: Task;
  onUpdate: (task: Task) => void;
  onDelete: (taskId: string) => void;
}

const TaskItem: React.FC<TaskItemProps> = ({ task, onUpdate, onDelete }) => {
  const [isEditing, setIsEditing] = useState(false);
  const [title, setTitle] = useState(task.title);
  const [description, setDescription] = useState(task.description || '');

  const handleToggleComplete = () => {
    onUpdate({
      ...task,
      completed: !task.completed
    });
  };

  const handleSave = () => {
    onUpdate({
      ...task,
      title,
      description: description || undefined
    });
    setIsEditing(false);
  };

  const handleCancel = () => {
    setTitle(task.title);
    setDescription(task.description || '');
    setIsEditing(false);
  };

  const handleDelete = () => {
    onDelete(task.id);
  };

  return (
    <div className={`bg-white p-4 rounded-lg shadow-md border-l-4 ${task.completed ? 'border-green-500' : 'border-blue-500'}`}>
      {isEditing ? (
        <div>
          <input
            type="text"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            className="w-full px-3 py-2 border border-gray-300 rounded-md mb-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
          <textarea
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            className="w-full px-3 py-2 border border-gray-300 rounded-md mb-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
            rows={2}
          />
          <div className="flex space-x-2">
            <button
              onClick={handleSave}
              className="bg-green-500 hover:bg-green-600 text-white text-sm py-1 px-3 rounded transition duration-200"
            >
              Save
            </button>
            <button
              onClick={handleCancel}
              className="bg-gray-500 hover:bg-gray-600 text-white text-sm py-1 px-3 rounded transition duration-200"
            >
              Cancel
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
              className="mt-1 mr-3 h-5 w-5 text-blue-600 rounded focus:ring-blue-500"
            />
            <div className="flex-1">
              <h3 className={`text-lg font-medium ${task.completed ? 'line-through text-gray-500' : 'text-gray-800'}`}>
                {task.title}
              </h3>
              {task.description && (
                <p className={`mt-1 ${task.completed ? 'line-through text-gray-500' : 'text-gray-600'}`}>
                  {task.description}
                </p>
              )}
              <p className="text-xs text-gray-400 mt-2">
                Created: {new Date(task.created_at).toLocaleDateString()}
              </p>
            </div>
            <div className="flex space-x-2">
              <button
                onClick={() => setIsEditing(true)}
                className="text-blue-500 hover:text-blue-700 text-sm font-medium"
              >
                Edit
              </button>
              <button
                onClick={handleDelete}
                className="text-red-500 hover:text-red-700 text-sm font-medium"
              >
                Delete
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default TaskItem;