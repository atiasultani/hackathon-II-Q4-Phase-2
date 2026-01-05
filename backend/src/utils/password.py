from passlib.context import CryptContext
from typing import Union

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a plain password against its hash.

    Args:
        plain_password: The plain text password to verify
        hashed_password: The hashed password to compare against

    Returns:
        True if the password matches the hash, False otherwise
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """
    Generate a hash for the given password.

    Args:
        password: The plain text password to hash

    Returns:
        The hashed password
    """
    return pwd_context.hash(password)


def validate_password_strength(password: str) -> Union[bool, str]:
    """
    Validate the strength of a password.

    Args:
        password: The password to validate

    Returns:
        True if password is strong, otherwise an error message
    """
    if len(password) < 8:
        return "Password must be at least 8 characters long"

    if not any(c.isupper() for c in password):
        return "Password must contain at least one uppercase letter"

    if not any(c.islower() for c in password):
        return "Password must contain at least one lowercase letter"

    if not any(c.isdigit() for c in password):
        return "Password must contain at least one number"

    if not any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
        return "Password must contain at least one special character"

    return True