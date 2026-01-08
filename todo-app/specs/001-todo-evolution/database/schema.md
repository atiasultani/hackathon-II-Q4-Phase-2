# Database Schema Specification

## Overview

The database schema defines the persistent data structures for the todo application using Neon Serverless PostgreSQL with SQLModel ORM. The schema ensures data integrity and supports the required functionality while maintaining user isolation.

## Database Engine

- **Database**: Neon Serverless PostgreSQL
- **ORM**: SQLModel
- **Connection**: Connection pooling with appropriate timeout settings

## Entity Definitions

### User Table

**Purpose**: Stores user account information for authentication and identification.

**Fields**:
- `id` (UUID/Integer, Primary Key): Unique identifier for each user
- `email` (String, Unique, Not Null): User's email address for authentication
- `hashed_password` (String, Not Null): Securely hashed password
- `created_at` (DateTime, Not Null): Timestamp of account creation
- `updated_at` (DateTime, Not Null): Timestamp of last update

**Constraints**:
- Email must be unique across all users
- Email must follow valid email format
- Password must be securely hashed before storage

### Task Table

**Purpose**: Stores individual todo tasks associated with specific users.

**Fields**:
- `id` (UUID/Integer, Primary Key): Unique identifier for each task
- `title` (String, Not Null): Title of the task (max length TBD)
- `description` (Text, Nullable): Detailed description of the task
- `completed` (Boolean, Not Null, Default: False): Completion status of the task
- `user_id` (UUID/Integer, Foreign Key, Not Null): Reference to the owning user
- `created_at` (DateTime, Not Null): Timestamp of task creation
- `updated_at` (DateTime, Not Null): Timestamp of last update

**Constraints**:
- `user_id` must reference a valid user in the User table
- `title` must not be empty
- Each task must be associated with a valid user

## Relationships

- **User to Tasks**: One-to-Many relationship
  - One user can have many tasks
  - Each task belongs to exactly one user
  - Deleting a user should cascade delete their tasks (or mark as inactive)

## Indexes

- **User Table**:
  - Primary key index on `id`
  - Unique index on `email`
  - Index on `created_at` for sorting

- **Task Table**:
  - Primary key index on `id`
  - Index on `user_id` for efficient user-based queries
  - Index on `completed` for filtering completed tasks
  - Index on `created_at` for chronological ordering
  - Composite index on `(user_id, completed)` for common user/completion queries

## Data Integrity

- Foreign key constraints to maintain referential integrity
- Not-null constraints on required fields
- Unique constraints where appropriate (email uniqueness)
- Proper cascading behavior for related records

## Security Considerations

- User passwords must be stored as securely hashed values (not plain text)
- No sensitive authentication information should be stored in plain text
- User isolation must be enforced at the application layer using user_id

## Migration Strategy

- Database schema should support versioning and migration
- Changes to schema should be backward compatible where possible
- Migration scripts should be provided for schema updates

## Performance Considerations

- Proper indexing to support common query patterns
- Efficient queries for retrieving user-specific tasks
- Consider partitioning for large datasets if needed

## Audit Trail

- `created_at` and `updated_at` timestamps for all records
- Ability to track when tasks were created, updated, or completed
- Potential for future expansion to include soft deletes if needed