from sqlmodel import Session, select
from typing import Optional, List
from datetime import datetime
from uuid import UUID
from ..models.task import Task, TaskCreate, TaskUpdate
from ..exceptions import TaskNotFoundException, UnauthorizedAccessException


class TaskService:
    """
    Service class for handling task-related operations.
    """

    @staticmethod
    def get_task_by_id(session: Session, task_id: UUID) -> Optional[Task]:
        """
        Retrieve a task by its ID.

        Args:
            session: Database session
            task_id: UUID of the task to retrieve

        Returns:
            Task object if found, None otherwise
        """
        return session.get(Task, task_id)

    @staticmethod
    def get_tasks_by_user_id(session: Session, user_id: UUID, completed: Optional[bool] = None) -> List[Task]:
        """
        Retrieve all tasks for a specific user.

        Args:
            session: Database session
            user_id: UUID of the user whose tasks to retrieve
            completed: Optional filter for completed status

        Returns:
            List of Task objects
        """
        query = select(Task).where(Task.user_id == user_id)

        if completed is not None:
            query = query.where(Task.completed == completed)

        query = query.order_by(Task.created_at.desc())
        return session.exec(query).all()

    @staticmethod
    def create_task(session: Session, task_create: TaskCreate) -> Task:
        """
        Create a new task for a user.

        Args:
            session: Database session
            task_create: Task creation data

        Returns:
            Created Task object
        """
        # Verify that the user_id in the task creation matches the authenticated user
        # This validation should be done at the API level, but we include it here as well
        db_task = Task(
            title=task_create.title,
            description=task_create.description,
            completed=task_create.completed,
            due_date=task_create.due_date,
            user_id=task_create.user_id
        )
        session.add(db_task)
        session.commit()
        session.refresh(db_task)
        return db_task

    @staticmethod
    def update_task(session: Session, task_id: UUID, user_id: UUID, task_update: TaskUpdate) -> Optional[Task]:
        """
        Update a task if it belongs to the specified user.

        Args:
            session: Database session
            task_id: UUID of the task to update
            user_id: UUID of the user requesting the update
            task_update: Task update data

        Returns:
            Updated Task object if successful, None if task not found or user not authorized

        Raises:
            UnauthorizedAccessException: If user tries to update another user's task
        """
        db_task = TaskService.get_task_by_id(session, task_id)
        if not db_task:
            return None

        # Check if the task belongs to the user
        if db_task.user_id != user_id:
            raise UnauthorizedAccessException("You can only update tasks that belong to you")

        # Update task fields
        update_data = task_update.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_task, field, value)

        db_task.updated_at = datetime.utcnow()
        session.add(db_task)
        session.commit()
        session.refresh(db_task)
        return db_task

    @staticmethod
    def delete_task(session: Session, task_id: UUID, user_id: UUID) -> bool:
        """
        Delete a task if it belongs to the specified user.

        Args:
            session: Database session
            task_id: UUID of the task to delete
            user_id: UUID of the user requesting the deletion

        Returns:
            True if task was deleted, False if task not found or user not authorized

        Raises:
            UnauthorizedAccessException: If user tries to delete another user's task
        """
        db_task = TaskService.get_task_by_id(session, task_id)
        if not db_task:
            return False

        # Check if the task belongs to the user
        if db_task.user_id != user_id:
            raise UnauthorizedAccessException("You can only delete tasks that belong to you")

        session.delete(db_task)
        session.commit()
        return True

    @staticmethod
    def mark_task_completed(session: Session, task_id: UUID, user_id: UUID, completed: bool) -> Optional[Task]:
        """
        Mark a task as completed or incomplete.

        Args:
            session: Database session
            task_id: UUID of the task to update
            user_id: UUID of the user requesting the update
            completed: Boolean indicating completion status

        Returns:
            Updated Task object if successful, None if task not found or user not authorized

        Raises:
            UnauthorizedAccessException: If user tries to update another user's task
        """
        db_task = TaskService.get_task_by_id(session, task_id)
        if not db_task:
            return None

        # Check if the task belongs to the user
        if db_task.user_id != user_id:
            raise UnauthorizedAccessException("You can only update tasks that belong to you")

        db_task.completed = completed
        db_task.updated_at = datetime.utcnow()
        session.add(db_task)
        session.commit()
        session.refresh(db_task)
        return db_task