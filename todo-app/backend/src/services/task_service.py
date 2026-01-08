from sqlmodel import Session, select
from typing import List, Optional
from uuid import UUID
from ..models.task import Task, TaskCreate, TaskUpdate
from ..schemas.task import TaskToggleComplete
from ..models.user import User
from ..schemas.task import TaskRead
from ..utils.error_handlers import log_api_call


class TaskService:
    @staticmethod
    def create_task(*, session: Session, task_create: TaskCreate, user_id: UUID) -> Task:
        """Create a new task for a user."""
        log_api_call("create_task", str(user_id))

        db_task = Task(
            title=task_create.title,
            description=task_create.description,
            completed=task_create.completed,
            user_id=user_id
        )

        session.add(db_task)
        session.commit()
        session.refresh(db_task)

        return db_task

    @staticmethod
    def get_tasks_by_user_id(*, session: Session, user_id: UUID) -> List[Task]:
        """Get all tasks for a specific user."""
        log_api_call("get_tasks_by_user_id", str(user_id))

        statement = select(Task).where(Task.user_id == user_id)
        tasks = session.exec(statement).all()
        return tasks

    @staticmethod
    def get_task_by_id_and_user_id(*, session: Session, task_id: UUID, user_id: UUID) -> Optional[Task]:
        """Get a specific task by its ID and user ID."""
        log_api_call("get_task_by_id_and_user_id", str(user_id))

        statement = select(Task).where(Task.id == task_id, Task.user_id == user_id)
        task = session.exec(statement).first()
        return task

    @staticmethod
    def update_task(*, session: Session, task_id: UUID, task_update: TaskUpdate, user_id: UUID) -> Optional[Task]:
        """Update a task by its ID."""
        log_api_call("update_task", str(user_id))

        statement = select(Task).where(Task.id == task_id, Task.user_id == user_id)
        db_task = session.exec(statement).first()

        if not db_task:
            return None

        # Update the task with the provided fields
        update_data = task_update.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_task, field, value)

        session.add(db_task)
        session.commit()
        session.refresh(db_task)

        return db_task

    @staticmethod
    def delete_task(*, session: Session, task_id: UUID, user_id: UUID) -> bool:
        """Delete a task by its ID."""
        log_api_call("delete_task", str(user_id))

        statement = select(Task).where(Task.id == task_id, Task.user_id == user_id)
        db_task = session.exec(statement).first()

        if not db_task:
            return False

        session.delete(db_task)
        session.commit()

        return True

    @staticmethod
    def toggle_task_completion(*, session: Session, task_id: UUID, task_toggle: TaskToggleComplete, user_id: UUID) -> Optional[Task]:
        """Toggle the completion status of a task."""
        log_api_call("toggle_task_completion", str(user_id))

        statement = select(Task).where(Task.id == task_id, Task.user_id == user_id)
        db_task = session.exec(statement).first()

        if not db_task:
            return None

        # Update the completion status
        db_task.completed = task_toggle.completed

        session.add(db_task)
        session.commit()
        session.refresh(db_task)

        return db_task