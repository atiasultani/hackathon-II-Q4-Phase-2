# Todo App Phase II - Task CRUD Feature

## User Stories
- As a registered user, I want to create tasks so that I can keep track of my to-dos
- As a registered user, I want to view my tasks so that I can see what I need to do
- As a registered user, I want to update my tasks so that I can modify their details
- As a registered user, I want to delete my tasks so that I can remove completed or unwanted items
- As a registered user, I want to mark tasks as complete/incomplete so that I can track my progress
- As a registered user, I want to see only my tasks so that my data remains private

## Acceptance Criteria
- Users can create a new task with a title (required), description (optional), due date (optional), and completion status (default: false)
- Users can retrieve a list of all their tasks
- Users can retrieve a specific task by its ID
- Users can update task details (title, description, due date, completion status)
- Users can delete a specific task by its ID
- Users can mark a task as complete or incomplete
- Users can only access tasks that belong to them
- All operations require valid authentication token

## Validation Rules
- Task title must be between 1 and 100 characters
- Task description must not exceed 500 characters
- Due date must be a valid date format (ISO 8601)
- Completion status must be a boolean value
- User must be authenticated to perform any task operations
- User can only modify tasks that belong to them

## Ownership Rules (User Isolation)
- Each task is associated with a specific user ID
- Users can only view, edit, or delete their own tasks
- API endpoints validate that the requested task belongs to the authenticated user
- Unauthorized access attempts return 403 Forbidden error
- Task listing endpoints only return tasks owned by the authenticated user