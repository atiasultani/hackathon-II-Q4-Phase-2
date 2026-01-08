from fastapi import HTTPException, status
from fastapi.responses import JSONResponse
from typing import Optional
import logging


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_error_response(status_code: int, detail: str):
    """
    Creates a standardized error response.

    Args:
        status_code: HTTP status code
        detail: Error message
    """
    logger.error(f"Error {status_code}: {detail}")
    return JSONResponse(
        status_code=status_code,
        content={"detail": detail}
    )


def handle_unauthorized_error(detail: str = "Unauthorized"):
    """Raises an HTTP exception for unauthorized access."""
    logger.warning(f"Unauthorized access attempt: {detail}")
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=detail,
        headers={"WWW-Authenticate": "Bearer"},
    )


def handle_forbidden_error(detail: str = "Forbidden"):
    """Raises an HTTP exception for forbidden access."""
    logger.warning(f"Forbidden access attempt: {detail}")
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail=detail
    )


def handle_not_found_error(entity: str = "Resource"):
    """Raises an HTTP exception for not found resources."""
    error_detail = f"{entity} not found"
    logger.info(error_detail)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=error_detail
    )


def handle_bad_request_error(detail: str = "Bad Request"):
    """Raises an HTTP exception for bad requests."""
    logger.warning(f"Bad request: {detail}")
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=detail
    )


def log_api_call(endpoint: str, user_id: Optional[str] = None):
    """Logs API calls for monitoring and debugging."""
    user_info = f" by user {user_id}" if user_id else ""
    logger.info(f"API call to {endpoint}{user_info}")