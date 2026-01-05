# API Contract: Todo App Phase II

**Feature**: Todo App Phase II - Full-Stack Web Application
**Version**: 1.0
**Date**: 2026-01-05

## Base URL
```
https://api.todoapp.com/v1  # Production
http://localhost:8000       # Development
```

## Authentication
All API endpoints (except authentication endpoints) require JWT authentication using the Authorization header:

```
Authorization: Bearer <jwt-token>
```

## Common Response Format

### Success Response
```json
{
  "success": true,
  "data": { /* response data */ },
  "message": "Optional success message"
}
```

### Error Response
```json
{
  "success": false,
  "error": "Error message",
  "code": "ERROR_CODE"
}
```

## Endpoints

### Authentication

#### POST /api/auth/signup
Create a new user account

**Request Body**:
```json
{
  "email": "user@example.com",
  "password": "securepassword123"
}
```

**Validation**:
- Email: required, valid email format, max 255 chars
- Password: required, min 8 chars

**Success Response (201)**:
```json
{
  "success": true,
  "data": {
    "user_id": "uuid-string",
    "email": "user@example.com",
    "token": "jwt-token-string"
  },
  "message": "User created successfully"
}
```

**Error Responses**:
- 400: Invalid input data
- 409: Email already exists

#### POST /api/auth/signin
Authenticate user and return JWT token

**Request Body**:
```json
{
  "email": "user@example.com",
  "password": "securepassword123"
}
```

**Validation**:
- Email: required, valid email format
- Password: required

**Success Response (200)**:
```json
{
  "success": true,
  "data": {
    "user_id": "uuid-string",
    "email": "user@example.com",
    "token": "jwt-token-string"
  },
  "message": "Authentication successful"
}
```

**Error Responses**:
- 400: Invalid input data
- 401: Invalid credentials

#### POST /api/auth/signout
Invalidate current user session

**Headers**:
```
Authorization: Bearer <jwt-token>
```

**Success Response (200)**:
```json
{
  "success": true,
  "message": "Successfully signed out"
}
```

**Error Responses**:
- 401: Invalid or expired token

### Tasks

#### GET /api/tasks
Retrieve all tasks for the authenticated user

**Headers**:
```
Authorization: Bearer <jwt-token>
```

**Query Parameters**:
- `completed` (optional): Filter by completion status (true/false)
- `limit` (optional): Number of tasks to return (default: 50, max: 100)
- `offset` (optional): Number of tasks to skip (for pagination)

**Success Response (200)**:
```json
{
  "success": true,
  "data": [
    {
      "id": "task-uuid",
      "title": "Task title",
      "description": "Task description",
      "completed": false,
      "due_date": "2023-12-31T10:00:00Z",
      "created_at": "2023-12-01T10:00:00Z",
      "updated_at": "2023-12-01T10:00:00Z"
    }
  ],
  "message": "Tasks retrieved successfully"
}
```

**Error Responses**:
- 401: Invalid or expired token

#### POST /api/tasks
Create a new task for the authenticated user

**Headers**:
```
Authorization: Bearer <jwt-token>
```

**Request Body**:
```json
{
  "title": "New task",
  "description": "Task description",
  "due_date": "2023-12-31T10:00:00Z",
  "completed": false
}
```

**Validation**:
- Title: required, 1-100 characters
- Description: optional, max 500 characters
- Due date: optional, valid ISO 8601 format
- Completed: optional, boolean (default: false)

**Success Response (201)**:
```json
{
  "success": true,
  "data": {
    "id": "new-task-uuid",
    "title": "New task",
    "description": "Task description",
    "completed": false,
    "due_date": "2023-12-31T10:00:00Z",
    "created_at": "2023-12-01T10:00:00Z",
    "updated_at": "2023-12-01T10:00:00Z"
  },
  "message": "Task created successfully"
}
```

**Error Responses**:
- 400: Invalid input data
- 401: Invalid or expired token

#### GET /api/tasks/{id}
Retrieve a specific task by ID

**Headers**:
```
Authorization: Bearer <jwt-token>
```

**Path Parameters**:
- `id`: Task UUID

**Success Response (200)**:
```json
{
  "success": true,
  "data": {
    "id": "task-uuid",
    "title": "Task title",
    "description": "Task description",
    "completed": false,
    "due_date": "2023-12-31T10:00:00Z",
    "created_at": "2023-12-01T10:00:00Z",
    "updated_at": "2023-12-01T10:00:00Z"
  },
  "message": "Task retrieved successfully"
}
```

**Error Responses**:
- 401: Invalid or expired token
- 403: Task does not belong to user
- 404: Task not found

#### PUT /api/tasks/{id}
Update a specific task by ID

**Headers**:
```
Authorization: Bearer <jwt-token>
```

**Path Parameters**:
- `id`: Task UUID

**Request Body** (all fields optional):
```json
{
  "title": "Updated task title",
  "description": "Updated description",
  "due_date": "2023-12-31T10:00:00Z",
  "completed": true
}
```

**Validation**:
- Title: 1-100 characters (if provided)
- Description: max 500 characters (if provided)
- Due date: valid ISO 8601 format (if provided)
- Completed: boolean (if provided)

**Success Response (200)**:
```json
{
  "success": true,
  "data": {
    "id": "task-uuid",
    "title": "Updated task title",
    "description": "Updated description",
    "completed": true,
    "due_date": "2023-12-31T10:00:00Z",
    "created_at": "2023-12-01T10:00:00Z",
    "updated_at": "2023-12-02T10:00:00Z"
  },
  "message": "Task updated successfully"
}
```

**Error Responses**:
- 400: Invalid input data
- 401: Invalid or expired token
- 403: Task does not belong to user
- 404: Task not found

#### DELETE /api/tasks/{id}
Delete a specific task by ID

**Headers**:
```
Authorization: Bearer <jwt-token>
```

**Path Parameters**:
- `id`: Task UUID

**Success Response (200)**:
```json
{
  "success": true,
  "message": "Task deleted successfully"
}
```

**Error Responses**:
- 401: Invalid or expired token
- 403: Task does not belong to user
- 404: Task not found

## HTTP Status Codes

- `200`: Success (GET, PUT, DELETE)
- `201`: Created (POST)
- `400`: Bad Request (validation error)
- `401`: Unauthorized (missing or invalid token)
- `403`: Forbidden (user cannot access resource)
- `404`: Not Found (resource does not exist)
- `409`: Conflict (resource already exists)
- `500`: Internal Server Error

## Security Requirements

1. All endpoints (except authentication) require valid JWT token
2. Users can only access their own data
3. Input validation on all fields
4. Proper error handling without information leakage
5. Rate limiting on authentication endpoints
6. HTTPS in production

## Error Codes

- `INVALID_CREDENTIALS`: Email/password combination is incorrect
- `EMAIL_EXISTS`: Email already registered
- `INVALID_INPUT`: Request data validation failed
- `TASK_NOT_FOUND`: Task with given ID does not exist
- `UNAUTHORIZED_ACCESS`: User trying to access another user's data
- `TOKEN_EXPIRED`: JWT token has expired
- `TOKEN_INVALID`: JWT token is malformed or invalid
- `RATE_LIMIT_EXCEEDED`: Too many requests from same IP