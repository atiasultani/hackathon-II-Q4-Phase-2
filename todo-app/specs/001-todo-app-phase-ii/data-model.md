# Data Model: Hackathon Todo App Phase II

## Entities

### User
- **id**: UUID (Primary Key)
- **email**: String (Unique, Required, Validated)
- **password_hash**: String (Required, Securely hashed)
- **created_at**: DateTime (Auto-generated)
- **updated_at**: DateTime (Auto-generated)
- **is_active**: Boolean (Default: true)

**Validation Rules:**
- Email must be a valid email format
- Password must meet security requirements (min 8 chars, complexity)
- Email must be unique across all users

**Relationships:**
- One-to-Many: User → Todos (user_id foreign key in todos table)

### Todo
- **id**: UUID (Primary Key)
- **title**: String (Required, Max 255 chars)
- **description**: Text (Optional)
- **is_completed**: Boolean (Default: false)
- **created_at**: DateTime (Auto-generated)
- **updated_at**: DateTime (Auto-generated)
- **user_id**: UUID (Foreign Key to User, Required)

**Validation Rules:**
- Title is required and cannot be empty
- Title must be less than 255 characters
- Todo must belong to an existing user
- Only the owner can modify/delete the todo

**State Transitions:**
- Active (is_completed = false) → Completed (is_completed = true)

## Database Schema Constraints

### Indexes
- User.email: Unique index for fast lookups and uniqueness enforcement
- Todo.user_id: Index for efficient user-based filtering
- Todo.created_at: Index for chronological sorting

### Foreign Key Constraints
- Todo.user_id references User.id with cascade behavior defined appropriately
- Prevents orphaned todo items

## Security Considerations
- All queries must filter by user_id to enforce data isolation
- No cross-user data access should be possible through the data model
- Proper validation at the database level to prevent invalid data