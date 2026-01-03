import pytest
from sqlmodel import create_engine
from app.models.user import User
from app.models.task import Task

# Use an in-memory SQLite database for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

def test_user_model():
    # Test creating a user instance
    user = User(
        email="test@example.com",
        name="Test User"
    )

    assert user.email == "test@example.com"
    assert user.name == "Test User"
    assert user.id is not None  # UUID should be generated

def test_task_model():
    # Test creating a task instance
    from uuid import UUID

    user_id = UUID("12345678-1234-5678-1234-567812345678")  # Mock UUID

    task = Task(
        title="Test Task",
        description="Test Description",
        completed=False,
        user_id=user_id
    )

    assert task.title == "Test Task"
    assert task.description == "Test Description"
    assert task.completed is False
    assert task.user_id == user_id
    assert task.id is not None  # UUID should be generated