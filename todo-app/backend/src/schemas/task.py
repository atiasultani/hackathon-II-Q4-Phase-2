from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
import uuid


class TaskBase(BaseModel):
    title: str = Field(max_length=255)
    description: Optional[str] = Field(default=None, max_length=1000)
    completed: bool = False


class TaskCreate(TaskBase):
    pass


class TaskRead(TaskBase):
    id: uuid.UUID
    user_id: uuid.UUID
    created_at: datetime
    updated_at: datetime


class TaskUpdate(BaseModel):
    title: Optional[str] = Field(default=None, max_length=255)
    description: Optional[str] = Field(default=None, max_length=1000)
    completed: Optional[bool] = None


class TaskToggleComplete(BaseModel):
    completed: bool