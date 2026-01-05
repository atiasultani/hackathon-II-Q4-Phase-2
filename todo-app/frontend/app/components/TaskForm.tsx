'use client';

import React, { useState } from 'react';

interface TaskFormProps {
  onTaskCreate: (task: { title: string; description?: string }) => void;
}

const TaskForm: React.FC<TaskFormProps> = ({ onTaskCreate }) => {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (title.trim() === '') return;

    onTaskCreate({
      title: title.trim(),
      description: description.trim() || undefined
    });

    setTitle('');
    setDescription('');
  };

  return (
    <form onSubmit={handleSubmit} className="bg-white p-6 rounded-lg shadow-md mb-6">
      <div className="mb-4">
        <label htmlFor="title" className="block text-gray-700 font-medium mb-2">
          Task Title *
        </label>
        <input
          type="text"
          id="title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          placeholder="What needs to be done?"
          required
        />
      </div>

      <div className="mb-4">
        <label htmlFor="description" className="block text-gray-700 font-medium mb-2">
          Description (Optional)
        </label>
        <textarea
          id="description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          placeholder="Add details..."
          rows={3}
        />
      </div>

      <button
        type="submit"
        className="bg-blue-500 hover:bg-blue-600 text-white font-medium py-2 px-4 rounded-md transition duration-200"
      >
        Add Task
      </button>
    </form>
  );
};

export default TaskForm;