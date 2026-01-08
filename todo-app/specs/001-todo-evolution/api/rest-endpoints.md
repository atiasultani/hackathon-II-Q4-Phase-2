# REST API Endpoints Specification

## API Overview

The REST API provides endpoints for all task management and user operations. All endpoints require JWT authentication in the Authorization header, except for authentication-specific endpoints.

## Authentication Requirements

- All endpoints (except authentication endpoints) require a valid JWT token in the Authorization header
- Format: `Authorization: Bearer <jwt_token>`
- Invalid or missing tokens result in 401 Unauthorized responses

## Base URL

All API endpoints are accessible under the `/api/` path.

## Endpoints

### Authentication Endpoints

#### POST /api/auth/register
- **Purpose**: Register a new user account
- **Request**:
  - Body: `{ "email": "user@example.com", "password": "secure_password" }`
- **Response**:
  - Success: 200 OK with user confirmation
  - Error: 400 Bad Request for invalid input, 409 Conflict for duplicate email
- **Authentication**: Not required

#### POST /api/auth/login
- **Purpose**: Authenticate user and return JWT token
- **Request**:
  - Body: `{ "email": "user@example.com", "password": "secure_password" }`
- **Response**:
  - Success: 200 OK with JWT token
  - Error: 400 Bad Request for invalid input, 401 Unauthorized for invalid credentials
- **Authentication**: Not required

### Task Management Endpoints

#### GET /api/{user_id}/tasks
- **Purpose**: Retrieve all tasks for the specified user
- **Parameters**:
  - `user_id`: The ID of the user whose tasks to retrieve
- **Response**:
  - Success: 200 OK with array of tasks
  - Error: 401 Unauthorized for invalid token, 403 Forbidden for user mismatch
- **Authentication**: Required

#### POST /api/{user_id}/tasks
- **Purpose**: Create a new task for the specified user
- **Parameters**:
  - `user_id`: The ID of the user creating the task
- **Request**:
  - Body: `{ "title": "Task title", "description": "Task description" }`
- **Response**:
  - Success: 201 Created with the created task
  - Error: 400 Bad Request for invalid input, 401 Unauthorized for invalid token, 403 Forbidden for user mismatch
- **Authentication**: Required

#### GET /api/{user_id}/tasks/{id}
- **Purpose**: Retrieve a specific task for the specified user
- **Parameters**:
  - `user_id`: The ID of the user whose task to retrieve
  - `id`: The ID of the task to retrieve
- **Response**:
  - Success: 200 OK with the task details
  - Error: 401 Unauthorized for invalid token, 403 Forbidden for user mismatch, 404 Not Found for non-existent task
- **Authentication**: Required

#### PUT /api/{user_id}/tasks/{id}
- **Purpose**: Update a specific task for the specified user
- **Parameters**:
  - `user_id`: The ID of the user whose task to update
  - `id`: The ID of the task to update
- **Request**:
  - Body: `{ "title": "Updated title", "description": "Updated description" }`
- **Response**:
  - Success: 200 OK with updated task
  - Error: 400 Bad Request for invalid input, 401 Unauthorized for invalid token, 403 Forbidden for user mismatch, 404 Not Found for non-existent task
- **Authentication**: Required

#### DELETE /api/{user_id}/tasks/{id}
- **Purpose**: Delete a specific task for the specified user
- **Parameters**:
  - `user_id`: The ID of the user whose task to delete
  - `id`: The ID of the task to delete
- **Response**:
  - Success: 204 No Content
  - Error: 401 Unauthorized for invalid token, 403 Forbidden for user mismatch, 404 Not Found for non-existent task
- **Authentication**: Required

#### PATCH /api/{user_id}/tasks/{id}/complete
- **Purpose**: Toggle the completion status of a specific task for the specified user
- **Parameters**:
  - `user_id`: The ID of the user whose task to update
  - `id`: The ID of the task to update
- **Request**:
  - Body: `{ "completed": true }` (or false to mark incomplete)
- **Response**:
  - Success: 200 OK with updated task
  - Error: 400 Bad Request for invalid input, 401 Unauthorized for invalid token, 403 Forbidden for user mismatch, 404 Not Found for non-existent task
- **Authentication**: Required

## Request/Response Format

- **Content-Type**: application/json
- **Response Format**: JSON objects with appropriate HTTP status codes
- **Error Format**: Standard error responses with descriptive messages

## Security Requirements

- All user-specific endpoints must validate that the `user_id` parameter matches the authenticated user
- All endpoints except authentication must validate JWT tokens
- Unauthorized requests must return 401 Unauthorized
- User mismatch attempts must return 403 Forbidden
- Non-existent resources must return 404 Not Found

## Error Handling

- 400 Bad Request: Invalid input data
- 401 Unauthorized: Invalid or missing authentication token
- 403 Forbidden: User attempting to access another user's data
- 404 Not Found: Requested resource does not exist
- 409 Conflict: Attempt to create duplicate resources (e.g., register with existing email)
- 500 Internal Server Error: Unexpected server errors