from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from typing import List
from uuid import UUID
import logging

from .. import schemas
from ..database import engine
from ..auth import auth
from ..services.task_service import TaskService

# Set up logging
logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/tasks", tags=["tasks"])

@router.get("/", response_model=List[schemas.TaskRead])
async def get_tasks(current_user=Depends(auth.current_user)):
    try:
        with Session(engine) as session:
            tasks = TaskService.get_tasks_by_user_id(session, current_user.id)
            return tasks
    except Exception as e:
        logger.error(f"Error getting tasks for user {current_user.id}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while retrieving tasks"
        )

@router.post("/", response_model=schemas.TaskRead)
async def create_task(task: schemas.TaskCreate, current_user=Depends(auth.current_user)):
    try:
        # Validate input
        if not task.title or task.title.strip() == "":
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Task title is required"
            )

        with Session(engine) as session:
            db_task = TaskService.create_task(session, task, current_user.id)
            return db_task
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error creating task for user {current_user.id}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while creating the task"
        )

@router.get("/{task_id}", response_model=schemas.TaskRead)
async def get_task(task_id: UUID, current_user=Depends(auth.current_user)):
    try:
        with Session(engine) as session:
            task = TaskService.get_task_by_id(session, task_id, current_user.id)
            if not task:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Task not found"
                )
            return task
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error getting task {task_id} for user {current_user.id}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while retrieving the task"
        )

@router.put("/{task_id}", response_model=schemas.TaskRead)
async def update_task(
    task_id: UUID,
    task_update: schemas.TaskUpdate,
    current_user=Depends(auth.current_user)
):
    try:
        with Session(engine) as session:
            db_task = TaskService.update_task(session, task_id, task_update, current_user.id)
            if not db_task:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Task not found"
                )
            return db_task
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error updating task {task_id} for user {current_user.id}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while updating the task"
        )

@router.delete("/{task_id}")
async def delete_task(task_id: UUID, current_user=Depends(auth.current_user)):
    try:
        with Session(engine) as session:
            success = TaskService.delete_task(session, task_id, current_user.id)
            if not success:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Task not found"
                )
            return {"message": "Task deleted successfully"}
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error deleting task {task_id} for user {current_user.id}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while deleting the task"
        )

@router.patch("/{task_id}/complete")
async def update_task_completion(
    task_id: UUID,
    completed: bool,
    current_user=Depends(auth.current_user)
):
    try:
        with Session(engine) as session:
            db_task = TaskService.update_task_completion(session, task_id, completed, current_user.id)
            if not db_task:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Task not found"
                )
            return {"id": db_task.id, "completed": db_task.completed}
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error updating task completion {task_id} for user {current_user.id}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while updating task completion"
        )