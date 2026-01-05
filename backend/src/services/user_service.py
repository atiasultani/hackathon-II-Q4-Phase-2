from sqlmodel import Session, select
from typing import Optional
from datetime import datetime
from ..models.user import User, UserCreate
from ..utils.password import verify_password, get_password_hash
from ..exceptions import UserNotFoundException, UserAlreadyExistsException, InvalidCredentialsException
from uuid import UUID


class UserService:
    """
    Service class for handling user-related operations.
    """

    @staticmethod
    def get_user_by_id(session: Session, user_id: UUID) -> Optional[User]:
        """
        Retrieve a user by their ID.

        Args:
            session: Database session
            user_id: UUID of the user to retrieve

        Returns:
            User object if found, None otherwise
        """
        return session.get(User, user_id)

    @staticmethod
    def get_user_by_email(session: Session, email: str) -> Optional[User]:
        """
        Retrieve a user by their email address.

        Args:
            session: Database session
            email: Email address of the user to retrieve

        Returns:
            User object if found, None otherwise
        """
        statement = select(User).where(User.email == email)
        return session.exec(statement).first()

    @staticmethod
    def create_user(session: Session, user_create: UserCreate) -> User:
        """
        Create a new user.

        Args:
            session: Database session
            user_create: User creation data

        Returns:
            Created User object

        Raises:
            UserAlreadyExistsException: If a user with the email already exists
        """
        # Check if user already exists
        existing_user = UserService.get_user_by_email(session, user_create.email)
        if existing_user:
            raise UserAlreadyExistsException(f"User with email {user_create.email} already exists")

        # Create new user
        hashed_password = get_password_hash(user_create.password)
        db_user = User(
            email=user_create.email,
            first_name=user_create.first_name,
            last_name=user_create.last_name,
            password_hash=hashed_password
        )
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
        return db_user

    @staticmethod
    def authenticate_user(session: Session, email: str, password: str) -> Optional[User]:
        """
        Authenticate a user with email and password.

        Args:
            session: Database session
            email: User's email address
            password: User's password

        Returns:
            User object if authentication is successful, None otherwise
        """
        user = UserService.get_user_by_email(session, email)
        if not user or not verify_password(password, user.password_hash):
            return None

        # Update last login time
        user.last_login = datetime.utcnow()
        session.add(user)
        session.commit()

        return user

    @staticmethod
    def update_user(session: Session, user_id: UUID, **kwargs) -> Optional[User]:
        """
        Update a user's information.

        Args:
            session: Database session
            user_id: UUID of the user to update
            **kwargs: Fields to update

        Returns:
            Updated User object if successful, None if user not found
        """
        db_user = UserService.get_user_by_id(session, user_id)
        if not db_user:
            return None

        # Update user fields
        for field, value in kwargs.items():
            if hasattr(db_user, field):
                setattr(db_user, field, value)

        db_user.updated_at = datetime.utcnow()
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
        return db_user

    @staticmethod
    def delete_user(session: Session, user_id: UUID) -> bool:
        """
        Delete a user by ID.

        Args:
            session: Database session
            user_id: UUID of the user to delete

        Returns:
            True if user was deleted, False if user not found
        """
        db_user = UserService.get_user_by_id(session, user_id)
        if not db_user:
            return False

        session.delete(db_user)
        session.commit()
        return True