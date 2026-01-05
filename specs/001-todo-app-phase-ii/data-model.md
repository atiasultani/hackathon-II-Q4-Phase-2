# Data Model: Todo App Phase II

**Feature**: Todo App Phase II - Full-Stack Web Application
**Date**: 2026-01-05
**Entities**: User, Task (Todo), JWT Token

## Entity: User

### Fields
- `id` (UUID/STRING, PRIMARY KEY): Unique identifier for the user
- `email` (STRING, UNIQUE, NOT NULL): User's email address
- `password_hash` (STRING, NOT NULL): Hashed password for authentication
- `created_at` (TIMESTAMP, NOT NULL): Timestamp of account creation
- `updated_at` (TIMESTAMP, NOT NULL): Timestamp of last account update
- `last_login` (TIMESTAMP, NULLABLE): Timestamp of last login (optional)

### Relationships
- One-to-Many: User has many Tasks
- Foreign Key: tasks.user_id references users.id

### Validation Rules
- Email: Must be valid email format, unique across system
- Password: Minimum 8 characters (validation happens before hashing)
- Email: Required field, max length 255 characters

## Entity: Task (Todo)

### Fields
- `id` (UUID/STRING, PRIMARY KEY): Unique identifier for the task
- `user_id` (UUID/STRING, FOREIGN KEY, NOT NULL): References the user who owns the task
- `title` (STRING, NOT NULL): Task title (max 100 characters)
- `description` (TEXT, NULLABLE): Optional task description (max 500 characters)
- `completed` (BOOLEAN, NOT NULL, DEFAULT: false): Completion status of the task
- `due_date` (TIMESTAMP, NULLABLE): Optional due date for the task
- `created_at` (TIMESTAMP, NOT NULL): Timestamp of task creation
- `updated_at` (TIMESTAMP, NOT NULL): Timestamp of last task update

### Relationships
- Many-to-One: Task belongs to one User
- Foreign Key: tasks.user_id references users.id

### Validation Rules
- Title: Required field, 1-100 characters
- Description: Optional, max 500 characters
- Completed: Boolean value, defaults to false
- Due date: If provided, must be valid date format
- User ID: Required field, must reference existing user

## Entity: JWT Token (Conceptual)

### Fields (Stored in memory/cookies, not database)
- `token` (STRING): The JWT token string
- `user_id` (UUID/STRING): Associated user ID (in token payload)
- `expires_at` (TIMESTAMP): Expiration time of the token
- `created_at` (TIMESTAMP): Time of token creation

### Validation Rules
- Must follow JWT standard format
- Must contain valid user ID in payload
- Must not be expired at time of use
- Must be properly signed with server secret

## Database Schema Design

### Users Table
```
users
├── id (PRIMARY KEY)
├── email (UNIQUE)
├── password_hash
├── created_at
├── updated_at
└── last_login
```

### Tasks Table
```
tasks
├── id (PRIMARY KEY)
├── user_id (FOREIGN KEY → users.id)
├── title
├── description
├── completed
├── due_date
├── created_at
└── updated_at
```

## Indexes
- `users.email`: Unique index for efficient login lookup
- `tasks.user_id`: Index for efficient user-specific task retrieval
- `tasks.created_at`: Index for sorting tasks by creation date
- `tasks.due_date`: Index for sorting tasks by due date

## Constraints
- Foreign key constraint: tasks.user_id references users.id
- Cascade delete: When user is deleted, all their tasks are deleted
- Email uniqueness: No duplicate email addresses allowed
- Required fields: All NOT NULL fields must have values

## State Transitions

### Task State Transitions
- `created` → `active` (default state when created)
- `active` → `completed` (when user marks task as complete)
- `completed` → `active` (when user unmarks task as complete)
- `any state` → `deleted` (when user deletes task)

### User Authentication States
- `unauthenticated` → `authenticated` (after successful login)
- `authenticated` → `unauthenticated` (after logout or token expiration)