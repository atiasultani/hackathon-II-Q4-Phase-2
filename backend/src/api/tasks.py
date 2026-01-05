from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlmodel import Session
from typing import Any, List
from uuid import UUID
import jwt
from ..database import get_session
from ..models.task import Task, TaskCreate, TaskUpdate
from ..services.task_service import TaskService
from ..exceptions import TaskNotFoundException, UnauthorizedAccessException
from ..auth.jwt import security
from fastapi.security import HTTPAuthorizationCredentials
from ..config import settings

router = APIRouter()


def get_current_user_id(credentials: HTTPAuthorizationCredentials = Depends(security)) -> UUID:
    """
    Extract the user ID from the JWT token.
    """
    token = credentials.credentials
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    # Extract user_id from token payload
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
        user_id: str = payload.get("user_id")
        if user_id is None:
            raise credentials_exception
    except jwt.JWTError:
        raise credentials_exception

    return UUID(user_id)


@router.get("/tasks", response_model=List[Task])
def get_tasks(
    completed: bool = Query(None, description="Filter by completion status"),
    user_id: UUID = Depends(get_current_user_id),
    session: Session = Depends(get_session)
) -> Any:
    """
    Retrieve all tasks for the authenticated user.
    """
    tasks = TaskService.get_tasks_by_user_id(session, user_id, completed)
    return tasks


@router.post("/tasks", response_model=Task)
def create_task(
    task_create: TaskCreate,
    user_id: UUID = Depends(get_current_user_id),
    session: Session = Depends(get_session)
) -> Any:
    """
    Create a new task for the authenticated user.
    """
    # Validate input data
    if len(task_create.title) < 1 or len(task_create.title) > 100:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Task title must be between 1 and 100 characters"
        )

    if task_create.description and len(task_create.description) > 500:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Task description must not exceed 500 characters"
        )

    # Ensure the task is created for the authenticated user
    task_create.user_id = user_id
    task = TaskService.create_task(session, task_create)
    return task


@router.get("/tasks/{task_id}", response_model=Task)
def get_task(
    task_id: UUID,
    user_id: UUID = Depends(get_current_user_id),
    session: Session = Depends(get_session)
) -> Any:
    """
    Retrieve a specific task by ID.
    """
    task = TaskService.get_task_by_id(session, task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    # Verify that the task belongs to the user
    if task.user_id != user_id:
        raise UnauthorizedAccessException("You can only access tasks that belong to you")

    return task


@router.put("/tasks/{task_id}", response_model=Task)
def update_task(
    task_id: UUID,
    task_update: TaskUpdate,
    user_id: UUID = Depends(get_current_user_id),
    session: Session = Depends(get_session)
) -> Any:
    """
    Update a specific task by ID.
    """
    # Validate input data if title is being updated
    if task_update.title is not None:
        if len(task_update.title) < 1 or len(task_update.title) > 100:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Task title must be between 1 and 100 characters"
            )

    if task_update.description is not None and len(task_update.description) > 500:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Task description must not exceed 500 characters"
        )

    updated_task = TaskService.update_task(session, task_id, user_id, task_update)
    if not updated_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    return updated_task


@router.delete("/tasks/{task_id}")
def delete_task(
    task_id: UUID,
    user_id: UUID = Depends(get_current_user_id),
    session: Session = Depends(get_session)
) -> Any:
    """
    Delete a specific task by ID.
    """
    success = TaskService.delete_task(session, task_id, user_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    return {"message": "Task deleted successfully"}