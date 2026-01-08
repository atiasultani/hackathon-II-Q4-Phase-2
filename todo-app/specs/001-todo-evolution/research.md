# Research: Evolution of Todo - Phase II

## Technology Decisions

### Backend Framework: FastAPI
**Decision**: Use FastAPI for the backend REST API
**Rationale**: FastAPI provides excellent performance, automatic API documentation, strong typing support with Pydantic, and async capabilities. It integrates well with SQLModel and JWT authentication.
**Alternatives considered**: Flask, Django, Express.js (Node.js)
- Flask: More mature but slower development and lacks automatic docs
- Django: Too heavy for this use case with built-in admin that isn't needed
- Express.js: Would create stack inconsistency (mixing JS/TS with Python)

### Frontend Framework: Next.js 16+
**Decision**: Use Next.js 16+ with App Router
**Rationale**: Next.js provides excellent developer experience, server-side rendering, static generation options, and great TypeScript support. The App Router provides modern routing patterns.
**Alternatives considered**: React with Create React App, Vue, Angular
- React CRA: Requires more manual setup for routing and optimization
- Vue: Good but team would need to learn new syntax
- Angular: Too heavy for this simple application

### Database: Neon Serverless PostgreSQL
**Decision**: Use Neon Serverless PostgreSQL
**Rationale**: Neon provides serverless PostgreSQL with excellent scaling, automatic branching, and pay-per-use pricing. It's compatible with standard PostgreSQL and works well with SQLModel.
**Alternatives considered**: SQLite, MongoDB, traditional PostgreSQL
- SQLite: Not suitable for multi-user web application
- MongoDB: Would require changing to document-based approach, not ideal for relational data
- Traditional PostgreSQL: Requires manual server management

### ORM: SQLModel
**Decision**: Use SQLModel as the ORM
**Rationale**: SQLModel combines Pydantic and SQLAlchemy, providing type safety and compatibility with FastAPI's Pydantic models. It's developed by the same creator as FastAPI.
**Alternatives considered**: SQLAlchemy alone, Tortoise ORM, Peewee
- SQLAlchemy alone: Would require separate validation models
- Tortoise ORM: Async-first but less mature than SQLModel
- Peewee: Simpler but lacks Pydantic integration

### Authentication: Better Auth with JWT
**Decision**: Use Better Auth for authentication with JWT tokens
**Rationale**: Better Auth provides a complete authentication solution with social logins, email/password, and secure JWT handling. It integrates well with Next.js and FastAPI.
**Alternatives considered**: Auth0, Firebase Auth, custom JWT implementation
- Auth0: Commercial solution, more complex than needed
- Firebase Auth: Would tie to Google ecosystem
- Custom JWT: More development work and security considerations

## API Design Patterns

### REST API Structure
Following the required API contract from the specification:
- GET /api/{user_id}/tasks - Retrieve all tasks for a user
- POST /api/{user_id}/tasks - Create a new task for a user
- GET /api/{user_id}/tasks/{id} - Retrieve a specific task
- PUT /api/{user_id}/tasks/{id} - Update a specific task
- DELETE /api/{user_id}/tasks/{id} - Delete a specific task
- PATCH /api/{user_id}/tasks/{id}/complete - Toggle task completion

### Authentication Flow
1. Frontend: User registers/logs in via Better Auth
2. Frontend: Receives JWT token from Better Auth
3. Frontend: Attaches JWT token to Authorization header for API requests
4. Backend: Validates JWT token on all protected endpoints
5. Backend: Extracts user_id from token and validates against URL parameter
6. Backend: Ensures user can only access their own data

## Security Considerations

### JWT Implementation
- Tokens expire after reasonable period (likely 24 hours)
- Refresh tokens for extended sessions
- Proper secret management with environment variables
- Token revocation mechanism for logout

### User Isolation
- All API endpoints validate that the authenticated user matches the user_id in the URL
- Database queries are filtered by user_id
- 403 Forbidden responses when user tries to access other users' data

## Development Approach

### Agent Specialization
- Frontend Agent: Responsible for Next.js UI components and pages
- Backend Agent: Handles FastAPI endpoints and services
- Auth Agent: Manages authentication and security
- Database Agent: Designs and manages SQLModel schemas
- API Contract Agent: Ensures API compliance with specifications