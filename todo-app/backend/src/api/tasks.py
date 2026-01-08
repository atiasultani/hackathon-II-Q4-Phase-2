from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from typing import List
import uuid
from ..database.config import get_session
from ..models.task import Task, TaskCreate, TaskUpdate
from ..schemas.task import TaskToggleComplete
from ..models.user import User
from ..schemas.task import TaskRead
from ..services.task_service import TaskService
from ..auth.jwt import verify_token
from ..schemas.user import TokenData
from ..utils.error_handlers import handle_unauthorized_error, handle_forbidden_error, handle_not_found_error


router = APIRouter()


def get_current_user(token: str = Depends(lambda: None), session: Session = Depends(get_session)):
    """Get the current authenticated user based on the token."""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    # Extract token from the Authorization header
    # This function is a placeholder - actual token extraction happens in the endpoint
    pass


@router.get("/{user_id}/tasks", response_model=List[TaskRead])
def get_user_tasks(user_id: uuid.UUID, token: str, session: Session = Depends(get_session)):
    """Get all tasks for a specific user."""
    # Verify the token and extract user data
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    token_data = verify_token(token, credentials_exception)

    # Verify that the token user_id matches the requested user_id
    if token_data.user_id != user_id:
        handle_forbidden_error("Not authorized to access this user's tasks")

    # Get tasks for the user
    tasks = TaskService.get_tasks_by_user_id(session=session, user_id=user_id)
    return tasks


@router.post("/{user_id}/tasks", response_model=TaskRead)
def create_task(user_id: uuid.UUID, task_create: TaskCreate, token: str, session: Session = Depends(get_session)):
    """Create a new task for a specific user."""
    # Verify the token and extract user data
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    token_data = verify_token(token, credentials_exception)

    # Verify that the token user_id matches the requested user_id
    if token_data.user_id != user_id:
        handle_forbidden_error("Not authorized to create tasks for this user")

    # Create the task
    task = TaskService.create_task(session=session, task_create=task_create, user_id=user_id)
    return task


@router.get("/{user_id}/tasks/{id}", response_model=TaskRead)
def get_task(user_id: uuid.UUID, id: uuid.UUID, token: str, session: Session = Depends(get_session)):
    """Get a specific task for a specific user."""
    # Verify the token and extract user data
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    token_data = verify_token(token, credentials_exception)

    # Verify that the token user_id matches the requested user_id
    if token_data.user_id != user_id:
        handle_forbidden_error("Not authorized to access this user's task")

    # Get the task
    task = TaskService.get_task_by_id_and_user_id(session=session, task_id=id, user_id=user_id)
    if not task:
        handle_not_found_error("Task")

    return task


@router.put("/{user_id}/tasks/{id}", response_model=TaskRead)
def update_task(user_id: uuid.UUID, id: uuid.UUID, task_update: TaskUpdate, token: str, session: Session = Depends(get_session)):
    """Update a specific task for a specific user."""
    # Verify the token and extract user data
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    token_data = verify_token(token, credentials_exception)

    # Verify that the token user_id matches the requested user_id
    if token_data.user_id != user_id:
        handle_forbidden_error("Not authorized to update this user's task")

    # Update the task
    updated_task = TaskService.update_task(session=session, task_id=id, task_update=task_update, user_id=user_id)
    if not updated_task:
        handle_not_found_error("Task")

    return updated_task


@router.delete("/{user_id}/tasks/{id}")
def delete_task(user_id: uuid.UUID, id: uuid.UUID, token: str, session: Session = Depends(get_session)):
    """Delete a specific task for a specific user."""
    # Verify the token and extract user data
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    token_data = verify_token(token, credentials_exception)

    # Verify that the token user_id matches the requested user_id
    if token_data.user_id != user_id:
        handle_forbidden_error("Not authorized to delete this user's task")

    # Delete the task
    deleted = TaskService.delete_task(session=session, task_id=id, user_id=user_id)
    if not deleted:
        handle_not_found_error("Task")

    return {"message": "Task deleted successfully"}


@router.patch("/{user_id}/tasks/{id}/complete", response_model=TaskRead)
def toggle_task_completion(user_id: uuid.UUID, id: uuid.UUID, task_toggle: TaskToggleComplete, token: str, session: Session = Depends(get_session)):
    """Toggle the completion status of a specific task for a specific user."""
    # Verify the token and extract user data
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    token_data = verify_token(token, credentials_exception)

    # Verify that the token user_id matches the requested user_id
    if token_data.user_id != user_id:
        handle_forbidden_error("Not authorized to update this user's task")

    # Toggle task completion
    updated_task = TaskService.toggle_task_completion(session=session, task_id=id, task_toggle=task_toggle, user_id=user_id)
    if not updated_task:
        handle_not_found_error("Task")

    return updated_task