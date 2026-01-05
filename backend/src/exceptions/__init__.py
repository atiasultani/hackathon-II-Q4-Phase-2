from fastapi import HTTPException, status
from typing import Optional

class BaseException(HTTPException):
    """Base exception class for the application"""

    def __init__(self, detail: str, status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR):
        super().__init__(status_code=status_code, detail=detail)

class UserNotFoundException(BaseException):
    """Raised when a user is not found"""

    def __init__(self, detail: str = "User not found"):
        super().__init__(detail=detail, status_code=status.HTTP_404_NOT_FOUND)

class TaskNotFoundException(BaseException):
    """Raised when a task is not found"""

    def __init__(self, detail: str = "Task not found"):
        super().__init__(detail=detail, status_code=status.HTTP_404_NOT_FOUND)

class UserAlreadyExistsException(BaseException):
    """Raised when trying to create a user that already exists"""

    def __init__(self, detail: str = "User already exists"):
        super().__init__(detail=detail, status_code=status.HTTP_409_CONFLICT)

class InvalidCredentialsException(BaseException):
    """Raised when invalid credentials are provided"""

    def __init__(self, detail: str = "Invalid credentials"):
        super().__init__(detail=detail, status_code=status.HTTP_401_UNAUTHORIZED)

class UnauthorizedAccessException(BaseException):
    """Raised when a user tries to access another user's data"""

    def __init__(self, detail: str = "Unauthorized access"):
        super().__init__(detail=detail, status_code=status.HTTP_403_FORBIDDEN)

class InvalidInputException(BaseException):
    """Raised when invalid input is provided"""

    def __init__(self, detail: str = "Invalid input"):
        super().__init__(detail=detail, status_code=status.HTTP_400_BAD_REQUEST)

def create_error_response(success: bool, error: str, code: Optional[str] = None):
    """Create a standardized error response"""
    response = {
        "success": success,
        "error": error
    }
    if code:
        response["code"] = code
    return response

def create_success_response(data, message: str = "Success"):
    """Create a standardized success response"""
    return {
        "success": True,
        "data": data,
        "message": message
    }