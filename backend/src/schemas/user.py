from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
import uuid


class UserBase(BaseModel):
    """
    Base schema for user with common fields.
    """
    email: EmailStr
    first_name: Optional[str] = None
    last_name: Optional[str] = None


class UserCreate(UserBase):
    """
    Schema for creating a new user.
    """
    password: str
    email: EmailStr


class UserRead(UserBase):
    """
    Schema for reading user data (without sensitive information).
    """
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime
    is_active: bool
    last_login: Optional[datetime] = None


class UserUpdate(BaseModel):
    """
    Schema for updating user information.
    """
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = None


class UserLogin(BaseModel):
    """
    Schema for user login credentials.
    """
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    """
    Response schema for user operations.
    """
    id: uuid.UUID
    email: EmailStr
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    is_active: bool


class Token(BaseModel):
    """
    Schema for JWT token response.
    """
    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    """
    Schema for token data.
    """
    username: Optional[str] = None