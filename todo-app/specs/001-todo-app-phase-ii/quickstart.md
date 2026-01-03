# Quickstart Guide: Hackathon Todo App Phase II

## Overview
This guide provides the essential steps to set up and run the Hackathon Todo App Phase II project.

## Prerequisites
- Node.js 18+ for frontend development
- Python 3.11+ for backend development
- PostgreSQL (or access to Neon Serverless PostgreSQL)
- Git for version control

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-name>
```

### 2. Backend Setup
1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install fastapi sqlmodel python-jose[cryptography] passlib[bcrypt] python-multipart
   ```

4. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your database connection details and JWT secret
   ```

5. Run the backend:
   ```bash
   uvicorn src.main:app --reload --port 8000
   ```

### 3. Frontend Setup
1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your backend API URL
   ```

4. Run the frontend:
   ```bash
   npm run dev
   ```

## Environment Variables

### Backend (.env)
- `DATABASE_URL`: Connection string for PostgreSQL database
- `JWT_SECRET_KEY`: Secret key for JWT token signing
- `JWT_ALGORITHM`: Algorithm for JWT encoding (default: HS256)
- `ACCESS_TOKEN_EXPIRE_MINUTES`: Token expiration time in minutes

### Frontend (.env)
- `NEXT_PUBLIC_API_BASE_URL`: Base URL for backend API (e.g., http://localhost:8000)

## API Endpoints

### Authentication
- `POST /api/auth/register` - Register a new user
- `POST /api/auth/login` - Login and get JWT token
- `POST /api/auth/logout` - Logout user

### Todos
- `GET /api/todos` - Get all todos for authenticated user
- `POST /api/todos` - Create a new todo
- `GET /api/todos/{id}` - Get a specific todo
- `PUT /api/todos/{id}` - Update a todo
- `DELETE /api/todos/{id}` - Delete a todo

## Database Setup
1. Ensure PostgreSQL is running
2. Run the database migrations:
   ```bash
   python -m src.database.migrate
   ```

## Testing
### Backend Tests
```bash
cd backend
python -m pytest
```

### Frontend Tests
```bash
cd frontend
npm test
```

## Development Workflow
1. Make changes to the code
2. Run backend tests: `python -m pytest`
3. Run frontend tests: `npm test`
4. Verify API contracts match the specifications in `specs/001-todo-app-phase-ii/contracts/`
5. Commit changes with descriptive commit messages

## Architecture Notes
- The application follows a clear separation between frontend and backend
- All API requests must include a valid JWT token in the Authorization header
- Database queries always filter by the authenticated user's ID to ensure data isolation
- Frontend communicates with backend only through the defined API contracts