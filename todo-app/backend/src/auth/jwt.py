from datetime import datetime, timedelta
from typing import Optional
import uuid
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import HTTPException, status
from ..config import settings
from ..schemas.user import TokenData


# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def _bcrypt_safe(password: str) -> str:
    # bcrypt limit is 72 BYTES, not chars
    b = password.encode("utf-8")
    if len(b) > 72:
        b = b[:72]
        return b.decode("utf-8", errors="ignore")
    return password


def get_password_hash(password: str) -> str:
    safe = _bcrypt_safe(password)
    return pwd_context.hash(safe)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    safe = _bcrypt_safe(plain_password)
    return pwd_context.verify(safe, hashed_password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """Create a JWT access token."""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.BETTER_AUTH_SECRET, algorithm="HS256")
    return encoded_jwt


def verify_token(token: str, credentials_exception: HTTPException):
    """Verify a JWT token and return the token data."""
    try:
        payload = jwt.decode(token, settings.BETTER_AUTH_SECRET, algorithms=["HS256"])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
        token_data = TokenData(user_id=uuid.UUID(user_id))
    except JWTError:
        raise credentials_exception
    return token_data