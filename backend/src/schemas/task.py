from pydantic import BaseModel
from typing import Optional
from datetime import datetime
import uuid


class TaskBase(BaseModel):
    """
    Base schema for task with common fields.
    """
    title: str
    description: Optional[str] = None
    completed: bool = False
    due_date: Optional[datetime] = None


class TaskRead(TaskBase):
    """
    Schema for reading task data.
    """
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime
    user_id: uuid.UUID


class TaskCreate(TaskBase):
    """
    Schema for creating a new task.
    """
    title: str
    user_id: uuid.UUID


class TaskUpdate(BaseModel):
    """
    Schema for updating task information.
    """
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
    due_date: Optional[datetime] = None


class TaskResponse(BaseModel):
    """
    Response schema for task operations.
    """
    id: uuid.UUID
    title: str
    description: Optional[str]
    completed: bool
    due_date: Optional[datetime]
    created_at: datetime
    updated_at: datetime
    user_id: uuid.UUID