# Todo App API Documentation

## Authentication

All API endpoints require authentication via JWT tokens. Include the token in the Authorization header:

```
Authorization: Bearer <token>
```

## Endpoints

### Authentication

#### Register User
- **POST** `/api/auth/register`
- **Request Body**:
  ```json
  {
    "email": "user@example.com",
    "password": "securepassword",
    "name": "User Name"
  }
  ```
- **Response**: User object with JWT token

#### Login User
- **POST** `/api/auth/login`
- **Request Body**:
  ```json
  {
    "email": "user@example.com",
    "password": "securepassword"
  }
  ```
- **Response**: User object with JWT token

#### Get Current User
- **GET** `/api/auth/me`
- **Headers**: Authorization: Bearer <token>
- **Response**: Current user object

### Tasks

#### Get All Tasks
- **GET** `/api/tasks`
- **Headers**: Authorization: Bearer <token>
- **Response**: Array of task objects
- **Permissions**: User can only access their own tasks

#### Create Task
- **POST** `/api/tasks`
- **Headers**: Authorization: Bearer <token>
- **Request Body**:
  ```json
  {
    "title": "Task Title",
    "description": "Task Description",
    "completed": false
  }
  ```
- **Response**: Created task object
- **Permissions**: Task is assigned to authenticated user

#### Get Task
- **GET** `/api/tasks/{task_id}`
- **Headers**: Authorization: Bearer <token>
- **Response**: Task object
- **Permissions**: User can only access their own tasks

#### Update Task
- **PUT** `/api/tasks/{task_id}`
- **Headers**: Authorization: Bearer <token>
- **Request Body**:
  ```json
  {
    "title": "Updated Title",
    "description": "Updated Description",
    "completed": true
  }
  ```
- **Response**: Updated task object
- **Permissions**: User can only update their own tasks

#### Delete Task
- **DELETE** `/api/tasks/{task_id}`
- **Headers**: Authorization: Bearer <token>
- **Response**: Success message
- **Permissions**: User can only delete their own tasks

#### Update Task Completion
- **PATCH** `/api/tasks/{task_id}/complete`
- **Headers**: Authorization: Bearer <token>
- **Request Body**:
  ```json
  {
    "completed": true
  }
  ```
- **Response**: Object with task ID and completion status
- **Permissions**: User can only update completion status of their own tasks

## Error Responses

All error responses follow this format:

```json
{
  "detail": "Error message"
}
```

Common HTTP status codes:
- 200: Success
- 201: Created
- 400: Bad Request
- 401: Unauthorized
- 404: Not Found
- 500: Internal Server Error

## Rate Limiting

API endpoints may be subject to rate limiting to prevent abuse.