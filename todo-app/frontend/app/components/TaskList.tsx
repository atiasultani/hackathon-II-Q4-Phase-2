'use client';

import React, { useState, useEffect } from 'react';
import TaskItem from './TaskItem';
import TaskForm from './TaskForm';
import { Task } from '../types/task';

interface TaskListProps {
  tasks: Task[];
  onTaskUpdate: (task: Task) => void;
  onTaskDelete: (taskId: string) => void;
  onTaskCreate: (task: Omit<Task, 'id' | 'created_at' | 'updated_at'>) => void;
}

const TaskList: React.FC<TaskListProps> = ({
  tasks,
  onTaskUpdate,
  onTaskDelete,
  onTaskCreate
}) => {
  const [localTasks, setLocalTasks] = useState<Task[]>(tasks);

  useEffect(() => {
    setLocalTasks(tasks);
  }, [tasks]);

  const handleTaskUpdate = (updatedTask: Task) => {
    setLocalTasks(localTasks.map(task =>
      task.id === updatedTask.id ? updatedTask : task
    ));
    onTaskUpdate(updatedTask);
  };

  const handleTaskDelete = (taskId: string) => {
    setLocalTasks(localTasks.filter(task => task.id !== taskId));
    onTaskDelete(taskId);
  };

  const handleTaskCreate = (newTask: Omit<Task, 'id' | 'created_at' | 'updated_at'>) => {
    onTaskCreate(newTask);
  };

  return (
    <div className="container mx-auto px-4 py-8">
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-gray-800 mb-6">My Tasks</h1>
        <TaskForm onTaskCreate={handleTaskCreate} />
      </div>

      <div className="space-y-4">
        {localTasks.length === 0 ? (
          <p className="text-gray-500 text-center py-8">No tasks yet. Add a new task to get started!</p>
        ) : (
          localTasks.map(task => (
            <TaskItem
              key={task.id}
              task={task}
              onUpdate={handleTaskUpdate}
              onDelete={handleTaskDelete}
            />
          ))
        )}
      </div>
    </div>
  );
};

export default TaskList;