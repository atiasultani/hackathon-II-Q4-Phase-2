import pytest
from unittest.mock import Mock
from sqlmodel import Session
from app.services.task_service import TaskService
from app import models, schemas
from uuid import UUID

def test_get_tasks_by_user_id():
    # Mock session
    mock_session = Mock(spec=Session)

    # Mock task data
    mock_task = models.Task(
        title="Test Task",
        description="Test Description",
        completed=False,
        user_id=UUID("12345678-1234-5678-1234-567812345678")
    )

    # Mock the exec method to return our test data
    mock_session.exec.return_value.all.return_value = [mock_task]

    user_id = UUID("12345678-1234-5678-1234-567812345678")
    result = TaskService.get_tasks_by_user_id(mock_session, user_id)

    assert len(result) == 1
    assert result[0] == mock_task
    mock_session.exec.assert_called_once()

def test_create_task():
    # Mock session
    mock_session = Mock(spec=Session)

    # Create test data
    task_create = schemas.TaskCreate(
        title="Test Task",
        description="Test Description",
        completed=False
    )
    user_id = UUID("12345678-1234-5678-1234-567812345678")

    # Mock the task object that will be returned after creation
    created_task = models.Task(
        id=UUID("87654321-4321-8765-4321-876543217654"),
        title=task_create.title,
        description=task_create.description,
        completed=task_create.completed,
        user_id=user_id
    )

    # Set up the mock to return the created task after commit/refresh
    mock_session.add.return_value = None
    mock_session.commit.return_value = None
    mock_session.refresh.return_value = None

    # Since we're mocking, we need to set up the object with the id
    created_task.id = UUID("87654321-4321-8765-4321-876543217654")

    # Call the service method
    result = TaskService.create_task(mock_session, task_create, user_id)

    # Check that the session methods were called
    mock_session.add.assert_called_once()
    mock_session.commit.assert_called_once()
    mock_session.refresh.assert_called_once()

    assert result.title == task_create.title
    assert result.user_id == user_id

def test_update_task_completion():
    # Mock session
    mock_session = Mock(spec=Session)

    # Create test data
    task_id = UUID("12345678-1234-5678-1234-567812345678")
    user_id = UUID("87654321-4321-8765-4321-876543217654")
    completed = True

    # Mock task object
    mock_task = models.Task(
        id=task_id,
        title="Test Task",
        description="Test Description",
        completed=False,  # Initially false
        user_id=user_id
    )

    # Mock the exec method to return the task
    mock_session.exec.return_value.first.return_value = mock_task
    mock_session.add.return_value = None
    mock_session.commit.return_value = None
    mock_session.refresh.return_value = None

    # Call the service method
    result = TaskService.update_task_completion(mock_session, task_id, completed, user_id)

    # Verify the task was updated
    assert result.completed == completed
    mock_session.add.assert_called_once()
    mock_session.commit.assert_called_once()
    mock_session.refresh.assert_called_once()