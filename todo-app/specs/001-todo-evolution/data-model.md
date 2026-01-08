# Data Model: Evolution of Todo - Phase II

## Entity: User
**Description**: Represents a registered user of the system with authentication credentials

**Fields**:
- `id` (UUID/String, Primary Key): Unique identifier for the user
- `email` (String, Unique, Not Null): User's email address for authentication
- `hashed_password` (String, Not Null): Securely hashed password using bcrypt or similar
- `created_at` (DateTime, Not Null): Timestamp of account creation
- `updated_at` (DateTime, Not Null): Timestamp of last account update

**Validation Rules**:
- Email must be a valid email format
- Email must be unique across all users
- Password must meet security requirements (length, complexity)
- All required fields must be present

**State Transitions**: None (user is either registered/active or deleted)

## Entity: Task
**Description**: Represents a todo item created by a user, containing title, description, completion status, and user association

**Fields**:
- `id` (UUID/String, Primary Key): Unique identifier for the task
- `title` (String, Max 255 chars, Not Null): Title of the task
- `description` (Text, Max 1000 chars, Nullable): Detailed description of the task
- `completed` (Boolean, Not Null, Default: False): Completion status of the task
- `user_id` (UUID/String, Foreign Key, Not Null): Reference to the owning user
- `created_at` (DateTime, Not Null): Timestamp of task creation
- `updated_at` (DateTime, Not Null): Timestamp of last task update

**Validation Rules**:
- Title must not be empty
- Title must be less than 256 characters
- Description, if provided, must be less than 1001 characters
- User_id must reference a valid existing user
- Task must be associated with exactly one user

**State Transitions**:
- `incomplete` → `completed` (via PATCH /api/{user_id}/tasks/{id}/complete with {completed: true})
- `completed` → `incomplete` (via PATCH /api/{user_id}/tasks/{id}/complete with {completed: false})

## Entity: Authentication Token (Conceptual)
**Description**: JWT token issued upon successful authentication (handled by Better Auth)

**Fields**:
- `token` (String): The JWT token string
- `user_id` (UUID/String): The user the token is associated with
- `expires_at` (DateTime): When the token expires
- `created_at` (DateTime): When the token was issued

**Note**: This entity is primarily managed by the Better Auth library, with tokens stored client-side.

## Relationships

### User → Tasks (One-to-Many)
- One user can own many tasks
- Each task belongs to exactly one user
- When a user is deleted, their tasks should also be deleted (CASCADE delete)
- All tasks must have a valid user association

**Relationship Constraints**:
- Foreign key constraint on user_id in tasks table
- Cascade delete to remove user's tasks when user is deleted
- Index on user_id for efficient querying of user's tasks

## Database Schema Implementation

### SQLModel Implementation

```python
from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import Optional, List
import uuid

class UserBase(SQLModel):
    email: str = Field(unique=True, nullable=False)

class User(UserBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    hashed_password: str = Field(nullable=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    # Relationship to tasks
    tasks: List["Task"] = Relationship(back_populates="user")

class UserRead(UserBase):
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime

class UserCreate(UserBase):
    password: str  # Plain text password to be hashed

class TaskBase(SQLModel):
    title: str = Field(max_length=255, nullable=False)
    description: Optional[str] = Field(default=None, max_length=1000)
    completed: bool = Field(default=False)

class Task(TaskBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    user_id: uuid.UUID = Field(foreign_key="user.id", nullable=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    # Relationship to user
    user: User = Relationship(back_populates="tasks")

class TaskRead(TaskBase):
    id: uuid.UUID
    user_id: uuid.UUID
    created_at: datetime
    updated_at: datetime

class TaskUpdate(SQLModel):
    title: Optional[str] = Field(default=None, max_length=255)
    description: Optional[str] = Field(default=None, max_length=1000)

class TaskToggleComplete(SQLModel):
    completed: bool
```

## Indexes

### User Table
- Primary key index on `id`
- Unique index on `email` for fast duplicate detection
- Index on `created_at` for chronological queries

### Task Table
- Primary key index on `id`
- Index on `user_id` for efficient user-specific queries
- Index on `completed` for filtering completed/incomplete tasks
- Composite index on `(user_id, completed)` for common combined queries
- Index on `created_at` for chronological ordering

## Constraints

### Referential Integrity
- Foreign key constraint from `tasks.user_id` to `users.id`
- Cascade delete to remove tasks when user is deleted
- Not-null constraints on required fields

### Data Validation
- Email format validation
- Length constraints on text fields
- Boolean values for completion status
- UUID format for identifiers

## Query Patterns

### Common Queries
1. Get all tasks for a specific user: `SELECT * FROM tasks WHERE user_id = ?`
2. Get completed tasks for a user: `SELECT * FROM tasks WHERE user_id = ? AND completed = TRUE`
3. Get a specific task for a user: `SELECT * FROM tasks WHERE id = ? AND user_id = ?`
4. Count tasks by completion status: `SELECT completed, COUNT(*) FROM tasks WHERE user_id = ? GROUP BY completed`