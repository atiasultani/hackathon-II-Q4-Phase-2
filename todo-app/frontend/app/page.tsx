'use client';

import React, { useState, useEffect } from 'react';
import TaskList from './components/TaskList';
import { Task } from './types/task';
import { taskApi } from './lib/api';

const DashboardPage = () => {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchTasks();
  }, []);

  const fetchTasks = async () => {
    try {
      setLoading(true);
      const tasksData = await taskApi.getTasks();
      setTasks(tasksData);
    } catch (error) {
      console.error('Error fetching tasks:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleTaskUpdate = async (updatedTask: Task) => {
    try {
      const updatedTaskResponse = await taskApi.updateTask(updatedTask.id, updatedTask);
      setTasks(tasks.map(task =>
        task.id === updatedTask.id ? updatedTaskResponse : task
      ));
    } catch (error) {
      console.error('Error updating task:', error);
    }
  };

  const handleTaskDelete = async (taskId: string) => {
    try {
      await taskApi.deleteTask(taskId);
      setTasks(tasks.filter(task => task.id !== taskId));
    } catch (error) {
      console.error('Error deleting task:', error);
    }
  };

  const handleTaskCreate = async (newTask: Omit<Task, 'id' | 'created_at' | 'updated_at'>) => {
    try {
      const createdTask = await taskApi.createTask(newTask);
      setTasks([...tasks, createdTask]);
    } catch (error) {
      console.error('Error creating task:', error);
    }
  };

  if (loading) {
    return (
      <div className="flex justify-center items-center h-screen">
        <div className="text-xl">Loading tasks...</div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <header className="bg-white shadow">
        <div className="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8">
          <h1 className="text-2xl font-bold text-gray-900">Todo App</h1>
        </div>
      </header>
      <main>
        <TaskList
          tasks={tasks}
          onTaskUpdate={handleTaskUpdate}
          onTaskDelete={handleTaskDelete}
          onTaskCreate={handleTaskCreate}
        />
      </main>
    </div>
  );
};

export default DashboardPage;