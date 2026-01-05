# Todo App Phase II - UI Pages

## Application Pages

### Login Page
- **Route**: `/login`
- **Purpose**: Allows users to sign in to their accounts
- **Components**:
  - Header (without user controls)
  - AuthForm (in 'signin' mode)
- **Access Control**: Available to unauthenticated users only
- **Behavior**:
  - Redirects to dashboard if user is already authenticated
  - Shows signup link for new users
  - Handles authentication errors
- **Success Flow**: Redirects to dashboard upon successful authentication

### Signup Page
- **Route**: `/signup`
- **Purpose**: Allows new users to create accounts
- **Components**:
  - Header (without user controls)
  - AuthForm (in 'signup' mode)
- **Access Control**: Available to unauthenticated users only
- **Behavior**:
  - Redirects to dashboard if user is already authenticated
  - Shows login link for existing users
  - Handles registration errors
- **Success Flow**: Redirects to dashboard upon successful registration

### Dashboard Page
- **Route**: `/dashboard` (or `/`)
- **Purpose**: Main application page showing user's tasks
- **Components**:
  - Header (with user controls)
  - TaskForm (for creating new tasks)
  - TaskList (showing all user tasks)
- **Access Control**: Requires authentication
- **Behavior**:
  - Fetches user's tasks on page load
  - Shows loading state while fetching data
  - Allows creating new tasks
  - Enables editing and deleting existing tasks
  - Shows empty state when no tasks exist
- **Success Flow**: Provides full task management functionality

### Task Edit Page
- **Route**: `/tasks/:id/edit`
- **Purpose**: Allows users to edit specific tasks
- **Components**:
  - Header (with user controls)
  - TaskForm (pre-filled with task data)
- **Access Control**: Requires authentication and task ownership
- **Behavior**:
  - Fetches specific task data on page load
  - Shows loading state while fetching data
  - Pre-fills form with existing task data
  - Handles task update errors
- **Success Flow**: Redirects back to dashboard after successful update

## Routing
- **Protected Routes**: All routes except `/login` and `/signup` require authentication
- **Redirects**: Unauthenticated users are redirected to login page
- **Authorization**: Users can only access their own tasks
- **Default Route**: `/` redirects to `/dashboard` for authenticated users

## Access Control per Page
- **Public Pages**: `/login`, `/signup`
- **Protected Pages**: All other routes require valid authentication token
- **Authorization Checks**: Task-specific pages verify user ownership of the requested task
- **Unauthorized Access**: Redirects to login page with appropriate error message