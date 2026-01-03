from sqlmodel import Session, select
from typing import List, Optional
from uuid import UUID

from .. import models
from .. import schemas

class TaskService:
    @staticmethod
    def get_tasks_by_user_id(db: Session, user_id: UUID) -> List[models.Task]:
        statement = select(models.Task).where(models.Task.user_id == user_id)
        return db.exec(statement).all()

    @staticmethod
    def create_task(db: Session, task: schemas.TaskCreate, user_id: UUID) -> models.Task:
        db_task = models.Task(
            **task.model_dump(),
            user_id=user_id
        )
        db.add(db_task)
        db.commit()
        db.refresh(db_task)
        return db_task

    @staticmethod
    def get_task_by_id(db: Session, task_id: UUID, user_id: UUID) -> Optional[models.Task]:
        statement = select(models.Task).where(
            models.Task.id == task_id,
            models.Task.user_id == user_id
        )
        return db.exec(statement).first()

    @staticmethod
    def update_task(
        db: Session,
        task_id: UUID,
        task_update: schemas.TaskUpdate,
        user_id: UUID
    ) -> Optional[models.Task]:
        db_task = TaskService.get_task_by_id(db, task_id, user_id)
        if not db_task:
            return None

        # Update task fields
        for field, value in task_update.model_dump(exclude_unset=True).items():
            setattr(db_task, field, value)

        db.add(db_task)
        db.commit()
        db.refresh(db_task)
        return db_task

    @staticmethod
    def delete_task(db: Session, task_id: UUID, user_id: UUID) -> bool:
        db_task = TaskService.get_task_by_id(db, task_id, user_id)
        if not db_task:
            return False

        db.delete(db_task)
        db.commit()
        return True

    @staticmethod
    def update_task_completion(db: Session, task_id: UUID, completed: bool, user_id: UUID) -> Optional[models.Task]:
        db_task = TaskService.get_task_by_id(db, task_id, user_id)
        if not db_task:
            return None

        db_task.completed = completed
        db.add(db_task)
        db.commit()
        db.refresh(db_task)
        return db_task