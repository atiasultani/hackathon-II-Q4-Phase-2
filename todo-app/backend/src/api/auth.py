from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlmodel import Session
from typing import Annotated
from datetime import timedelta
import uuid
from ..database.config import get_session
from ..models.user import User
from ..schemas.user import UserCreate, UserLogin, Token
from ..services.user_service import UserService
from ..auth.jwt import create_access_token, verify_password
from ..config import settings
from ..utils.error_handlers import handle_bad_request_error


router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/token")


@router.post("/auth/register", response_model=dict)
def register(user_create: UserCreate, session: Session = Depends(get_session)):
    """Register a new user."""
    # Check if user already exists
    existing_user = UserService.get_user_by_email(session=session, email=user_create.email)
    if existing_user:
        handle_bad_request_error("Email already registered")

    # Create the user
    user = UserService.create_user(session=session, user_create=user_create)

    return {"message": "User created successfully", "user_id": str(user.id)}


@router.post("/auth/login", response_model=Token)
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], session: Session = Depends(get_session)):
    """Authenticate user and return access token."""
    # Authenticate the user
    user = UserService.authenticate_user(
        session=session,
        email=form_data.username,
        password=form_data.password
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Create access token
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": str(user.id)}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/auth/logout")
def logout():
    """Logout endpoint."""
    return {"message": "Logged out successfully"}