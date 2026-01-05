# Todo App Phase II - REST API Endpoints

## Authentication Endpoints

### POST /auth/signup
- **Purpose**: Create a new user account
- **Request Body**:
  ```json
  {
    "email": "user@example.com",
    "password": "securepassword123"
  }
  ```
- **Response**:
  ```json
  {
    "user_id": "uuid-string",
    "email": "user@example.com",
    "token": "jwt-token-string"
  }
  ```
- **Authentication**: Not required
- **Success**: 201 Created
- **Errors**: 400 Bad Request (validation error), 409 Conflict (email exists)

### POST /auth/signin
- **Purpose**: Authenticate user and return JWT token
- **Request Body**:
  ```json
  {
    "email": "user@example.com",
    "password": "securepassword123"
  }
  ```
- **Response**:
  ```json
  {
    "user_id": "uuid-string",
    "email": "user@example.com",
    "token": "jwt-token-string"
  }
  ```
- **Authentication**: Not required
- **Success**: 200 OK
- **Errors**: 400 Bad Request (validation error), 401 Unauthorized (invalid credentials)

### POST /auth/signout
- **Purpose**: Invalidate current user session
- **Request Body**: None
- **Response**:
  ```json
  {
    "message": "Successfully signed out"
  }
  ```
- **Authentication**: Required (valid JWT token)
- **Success**: 200 OK
- **Errors**: 401 Unauthorized (invalid token)

## Task Endpoints

### GET /tasks
- **Purpose**: Retrieve all tasks for the authenticated user
- **Request Body**: None
- **Response**:
  ```json
  [
    {
      "id": "task-uuid",
      "title": "Task title",
      "description": "Task description",
      "completed": false,
      "due_date": "2023-12-31T10:00:00Z",
      "created_at": "2023-12-01T10:00:00Z",
      "updated_at": "2023-12-01T10:00:00Z"
    }
  ]
  ```
- **Authentication**: Required (valid JWT token)
- **Success**: 200 OK
- **Errors**: 401 Unauthorized (invalid token)

### POST /tasks
- **Purpose**: Create a new task for the authenticated user
- **Request Body**:
  ```json
  {
    "title": "New task",
    "description": "Task description",
    "due_date": "2023-12-31T10:00:00Z",
    "completed": false
  }
  ```
- **Response**:
  ```json
  {
    "id": "new-task-uuid",
    "title": "New task",
    "description": "Task description",
    "completed": false,
    "due_date": "2023-12-31T10:00:00Z",
    "created_at": "2023-12-01T10:00:00Z",
    "updated_at": "2023-12-01T10:00:00Z"
  }
  ```
- **Authentication**: Required (valid JWT token)
- **Success**: 201 Created
- **Errors**: 400 Bad Request (validation error), 401 Unauthorized (invalid token)

### GET /tasks/{task_id}
- **Purpose**: Retrieve a specific task by ID
- **Request Body**: None
- **Response**:
  ```json
  {
    "id": "task-uuid",
    "title": "Task title",
    "description": "Task description",
    "completed": false,
    "due_date": "2023-12-31T10:00:00Z",
    "created_at": "2023-12-01T10:00:00Z",
    "updated_at": "2023-12-01T10:00:00Z"
  }
  ```
- **Authentication**: Required (valid JWT token)
- **Success**: 200 OK
- **Errors**: 401 Unauthorized (invalid token), 403 Forbidden (task doesn't belong to user), 404 Not Found (task doesn't exist)

### PUT /tasks/{task_id}
- **Purpose**: Update a specific task by ID
- **Request Body**:
  ```json
  {
    "title": "Updated task title",
    "description": "Updated description",
    "due_date": "2023-12-31T10:00:00Z",
    "completed": true
  }
  ```
- **Response**:
  ```json
  {
    "id": "task-uuid",
    "title": "Updated task title",
    "description": "Updated description",
    "completed": true,
    "due_date": "2023-12-31T10:00:00Z",
    "created_at": "2023-12-01T10:00:00Z",
    "updated_at": "2023-12-02T10:00:00Z"
  }
  ```
- **Authentication**: Required (valid JWT token)
- **Success**: 200 OK
- **Errors**: 400 Bad Request (validation error), 401 Unauthorized (invalid token), 403 Forbidden (task doesn't belong to user), 404 Not Found (task doesn't exist)

### DELETE /tasks/{task_id}
- **Purpose**: Delete a specific task by ID
- **Request Body**: None
- **Response**:
  ```json
  {
    "message": "Task deleted successfully"
  }
  ```
- **Authentication**: Required (valid JWT token)
- **Success**: 200 OK
- **Errors**: 401 Unauthorized (invalid token), 403 Forbidden (task doesn't belong to user), 404 Not Found (task doesn't exist)

## Authentication Requirements
- All `/auth/` endpoints except `/signup` and `/signin` require valid JWT token
- All `/tasks/` endpoints require valid JWT token
- Invalid or expired tokens result in 401 Unauthorized response

## Error Handling Rules
- All error responses follow the format:
  ```json
  {
    "error": "Error message",
    "code": "error_code"
  }
  ```
- 400 Bad Request: Validation errors or malformed requests
- 401 Unauthorized: Missing or invalid authentication token
- 403 Forbidden: User attempting to access resources they don't own
- 404 Not Found: Requested resource does not exist
- 500 Internal Server Error: Unexpected server errors