# Todo App Phase II - UI Components

## Reusable UI Components

### AuthForm
- **Purpose**: Handles user authentication (signup/signin)
- **Responsibilities**:
  - Renders email and password input fields
  - Handles form validation
  - Submits credentials to authentication API
  - Displays authentication errors
- **Props**:
  - `mode`: 'signup' or 'signin'
  - `onSubmit`: Callback function for successful authentication
  - `onError`: Callback function for authentication errors

### TaskForm
- **Purpose**: Handles task creation and editing
- **Responsibilities**:
  - Renders task input fields (title, description, due date, completion status)
  - Handles form validation
  - Submits task data to API
  - Displays form errors
- **Props**:
  - `task`: Optional task object for editing (null for creation)
  - `onSubmit`: Callback function for successful task submission
  - `onCancel`: Callback function for canceling form

### TaskItem
- **Purpose**: Displays a single task with interactive controls
- **Responsibilities**:
  - Shows task details (title, description, due date, completion status)
  - Provides edit and delete buttons
  - Handles completion status toggle
  - Shows visual indicators for task status
- **Props**:
  - `task`: Task object to display
  - `onEdit`: Callback function for edit button
  - `onDelete`: Callback function for delete button
  - `onToggleComplete`: Callback function for completion toggle

### TaskList
- **Purpose**: Displays a list of tasks
- **Responsibilities**:
  - Fetches and displays tasks for the authenticated user
  - Handles loading states
  - Displays empty state when no tasks exist
  - Provides filtering/sorting options
- **Props**:
  - `tasks`: Array of task objects to display
  - `onTaskEdit`: Callback function for task edit
  - `onTaskDelete`: Callback function for task delete
  - `onTaskToggleComplete`: Callback function for task completion toggle

### Header
- **Purpose**: Displays application header with user controls
- **Responsibilities**:
  - Shows application title
  - Displays user authentication status
  - Provides signout button
  - Shows navigation links
- **Props**:
  - `user`: User object if authenticated
  - `onSignOut`: Callback function for signout button

### LoadingSpinner
- **Purpose**: Shows loading state during API requests
- **Responsibilities**:
  - Displays visual loading indicator
  - Optionally shows loading text
- **Props**:
  - `message`: Optional loading message to display

### ErrorMessage
- **Purpose**: Displays error messages to the user
- **Responsibilities**:
  - Shows error message with appropriate styling
  - Optionally provides error dismissal
- **Props**:
  - `message`: Error message to display
  - `onDismiss`: Optional callback for dismissing the error