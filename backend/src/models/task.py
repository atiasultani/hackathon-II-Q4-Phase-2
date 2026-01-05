from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import datetime
import uuid
from .base import TimestampMixin
from .user import User  # Import User for relationship


class TaskBase(SQLModel):
    """
    Base class for Task model with common fields.
    """
    title: str = Field(min_length=1, max_length=100, nullable=False)
    description: Optional[str] = Field(default=None, max_length=500)
    completed: bool = Field(default=False)
    due_date: Optional[datetime] = Field(default=None)


class Task(TaskBase, TimestampMixin, table=True):
    """
    Task model representing a todo item.
    Contains title, description, completion status, creation timestamp, and user ID reference.
    """
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
    user_id: uuid.UUID = Field(foreign_key="user.id", nullable=False)

    # Relationship to user
    user: User = Relationship(back_populates="tasks")


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
    title: str = Field(min_length=1, max_length=100)
    user_id: uuid.UUID


class TaskUpdate(SQLModel):
    """
    Schema for updating task information.
    """
    title: Optional[str] = Field(default=None, min_length=1, max_length=100)
    description: Optional[str] = None
    completed: Optional[bool] = None
    due_date: Optional[datetime] = None