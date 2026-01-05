from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlmodel import Session
from typing import Any
from datetime import timedelta
from pydantic import EmailStr
import re
from ..database import get_session
from ..models.user import User, UserCreate
from ..schemas.user import UserRead, UserLogin, Token
from ..services.user_service import UserService
from ..auth.jwt import create_access_token, verify_password, get_password_hash, verify_token
from ..config import settings
from ..exceptions import InvalidCredentialsException, UserAlreadyExistsException
from ..exceptions import create_success_response, create_error_response

router = APIRouter()
security = HTTPBearer()


def validate_email_format(email: str) -> bool:
    """
    Validate the format of an email address.
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def validate_password_strength(password: str) -> tuple[bool, str]:
    """
    Validate the strength of a password.

    Returns:
        tuple: (is_valid, error_message)
    """
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"

    if not any(c.isupper() for c in password):
        return False, "Password must contain at least one uppercase letter"

    if not any(c.islower() for c in password):
        return False, "Password must contain at least one lowercase letter"

    if not any(c.isdigit() for c in password):
        return False, "Password must contain at least one number"

    return True, ""


@router.post("/auth/signup", response_model=UserRead)
def register_user(user_create: UserCreate, session: Session = Depends(get_session)) -> Any:
    """
    Create a new user account.
    """
    try:
        # Validate email format
        if not validate_email_format(user_create.email):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid email format"
            )

        # Validate password strength
        is_valid, error_msg = validate_password_strength(user_create.password)
        if not is_valid:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=error_msg
            )

        # Create user using the service
        db_user = UserService.create_user(session, user_create)
        return db_user
    except UserAlreadyExistsException:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with this email already exists"
        )
    except HTTPException:
        # Re-raise HTTP exceptions
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while creating the user"
        )


@router.post("/auth/signin", response_model=Token)
def login_user(user_credentials: UserLogin, session: Session = Depends(get_session)) -> Any:
    """
    Authenticate user and return JWT token.
    """
    # Validate email format
    if not validate_email_format(user_credentials.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid email format"
        )

    # Authenticate user
    user = UserService.authenticate_user(session, user_credentials.email, user_credentials.password)

    if not user:
        raise InvalidCredentialsException()

    # Create access token
    access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
    access_token = create_access_token(
        data={"sub": user.email, "user_id": str(user.id)},
        expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/auth/signout")
def logout_user() -> Any:
    """
    Invalidate current user session.
    """
    # In a real implementation, you might want to add the token to a blacklist
    # For now, we just return a success message
    return {"message": "Successfully signed out"}


@router.get("/auth/me", response_model=UserRead)
def get_current_user() -> Any:
    """
    Get information about the currently authenticated user.
    """
    # This would require extracting user info from the JWT token
    # Implementation would require a dependency to verify the token
    # Placeholder for now
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Not implemented yet"
    )