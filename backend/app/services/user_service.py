from sqlmodel import Session, select
from typing import Optional
from uuid import UUID

from .. import models
from .. import schemas

class UserService:
    @staticmethod
    def get_user_by_id(db: Session, user_id: UUID) -> Optional[models.User]:
        statement = select(models.User).where(models.User.id == user_id)
        return db.exec(statement).first()

    @staticmethod
    def get_user_by_email(db: Session, email: str) -> Optional[models.User]:
        statement = select(models.User).where(models.User.email == email)
        return db.exec(statement).first()

    @staticmethod
    def create_user(db: Session, user: schemas.UserCreate) -> models.User:
        db_user = models.User(
            email=user.email,
            name=user.name
        )
        # In a real implementation, we'd hash the password here
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user