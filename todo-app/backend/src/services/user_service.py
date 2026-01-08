from sqlmodel import Session, select
from typing import Optional
from uuid import UUID
from ..models.user import User, UserCreate
from ..auth.jwt import get_password_hash, verify_password
from ..schemas.user import UserLogin


class UserService:
    @staticmethod
    def create_user(*, session: Session, user_create: UserCreate) -> User:
        """Create a new user with hashed password."""
        # Hash the password
        hashed_password = get_password_hash(user_create.password)

        # Create the user object
        db_user = User(
            email=user_create.email,
            hashed_password=hashed_password
        )

        # Add to session and commit
        session.add(db_user)
        session.commit()
        session.refresh(db_user)

        return db_user

    @staticmethod
    def authenticate_user(*, session: Session, email: str, password: str) -> Optional[User]:
        """Authenticate user by email and password."""
        # Get user by email
        statement = select(User).where(User.email == email)
        user = session.exec(statement).first()

        # Verify user exists and password is correct
        if not user or not verify_password(password, user.hashed_password):
            return None

        return user

    @staticmethod
    def get_user_by_email(*, session: Session, email: str) -> Optional[User]:
        """Get a user by email."""
        statement = select(User).where(User.email == email)
        user = session.exec(statement).first()
        return user

    @staticmethod
    def get_user_by_id(*, session: Session, user_id: UUID) -> Optional[User]:
        """Get a user by ID."""
        statement = select(User).where(User.id == user_id)
        user = session.exec(statement).first()
        return user