from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from uuid import UUID

from .. import schemas
from ..database import engine
from ..auth import auth
from ..services.user_service import UserService

router = APIRouter(prefix="/api/auth", tags=["auth"])

@router.get("/me", response_model=schemas.UserRead)
async def get_current_user(current_user=Depends(auth.current_user)):
    return current_user

@router.post("/login")
async def login(user_data: schemas.UserCreate):
    # This would integrate with Better Auth's login functionality
    # For now, we'll use the auth system directly
    return await auth.login(user_data.email, user_data.password)

@router.post("/register")
async def register(user_data: schemas.UserCreate):
    # This would integrate with Better Auth's registration functionality
    return await auth.register(
        email=user_data.email,
        password=user_data.password,
        name=user_data.name
    )