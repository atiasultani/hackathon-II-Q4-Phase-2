from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime
import uuid
from .base import TimestampMixin
from .task import Task  # Import Task for relationship


class UserBase(SQLModel):
    """
    Base class for User model with common fields.
    """
    email: str = Field(unique=True, nullable=False, max_length=255)
    first_name: Optional[str] = Field(default=None, max_length=100)
    last_name: Optional[str] = Field(default=None, max_length=100)


class User(UserBase, TimestampMixin, table=True):
    """
    User model representing an authenticated user of the system.
    Contains email, password hash, and user metadata.
    """
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
    password_hash: str = Field(nullable=False)
    is_active: bool = Field(default=True)
    last_login: Optional[datetime] = Field(default=None)

    # Relationship to tasks
    tasks: List["Task"] = Relationship(back_populates="user")


class UserRead(UserBase):
    """
    Schema for reading user data (without sensitive information).
    """
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime
    is_active: bool
    last_login: Optional[datetime]


class UserCreate(UserBase):
    """
    Schema for creating a new user.
    """
    password: str
    email: str = Field(unique=True, nullable=False, max_length=255)


class UserUpdate(SQLModel):
    """
    Schema for updating user information.
    """
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = Field(default=None, unique=True, max_length=255)
    is_active: Optional[bool] = None


class UserLogin(SQLModel):
    """
    Schema for user login credentials.
    """
    email: str
    password: str