# Todo App Phase II - Database Schema

## Tables

### users
- **Purpose**: Stores user account information
- **Fields**:
  - `id` (UUID/STRING, PRIMARY KEY): Unique identifier for the user
  - `email` (STRING, UNIQUE, NOT NULL): User's email address
  - `password_hash` (STRING, NOT NULL): Hashed password for authentication
  - `created_at` (TIMESTAMP, NOT NULL): Timestamp of account creation
  - `updated_at` (TIMESTAMP, NOT NULL): Timestamp of last account update

### tasks
- **Purpose**: Stores task information associated with users
- **Fields**:
  - `id` (UUID/STRING, PRIMARY KEY): Unique identifier for the task
  - `user_id` (UUID/STRING, FOREIGN KEY, NOT NULL): References the user who owns the task
  - `title` (STRING, NOT NULL): Task title (max 100 characters)
  - `description` (TEXT, NULLABLE): Optional task description (max 500 characters)
  - `completed` (BOOLEAN, NOT NULL, DEFAULT: false): Completion status of the task
  - `due_date` (TIMESTAMP, NULLABLE): Optional due date for the task
  - `created_at` (TIMESTAMP, NOT NULL): Timestamp of task creation
  - `updated_at` (TIMESTAMP, NOT NULL): Timestamp of last task update

## Relationships
- **users to tasks**: One-to-Many relationship
  - One user can have multiple tasks
  - Each task belongs to exactly one user
  - Foreign key constraint: tasks.user_id references users.id
  - Cascade delete: When a user is deleted, all their tasks are also deleted

## Indexes
- **users.email**: Unique index on email field for efficient lookup and uniqueness enforcement
- **tasks.user_id**: Index on user_id field for efficient retrieval of user-specific tasks
- **tasks.created_at**: Index on created_at field for sorting and filtering by creation date
- **tasks.due_date**: Index on due_date field for sorting and filtering by due date

## Constraints
- **users.email**: UNIQUE constraint to ensure no duplicate email addresses
- **users.email**: NOT NULL constraint to ensure all users have an email
- **tasks.user_id**: NOT NULL constraint to ensure every task is associated with a user
- **tasks.title**: NOT NULL constraint to ensure all tasks have a title
- **Referential integrity**: Foreign key constraint ensures tasks.user_id references a valid user