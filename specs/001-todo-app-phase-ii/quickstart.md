# Quickstart Guide: Todo App Phase II

**Feature**: Todo App Phase II - Full-Stack Web Application
**Date**: 2026-01-05

## Prerequisites

- Python 3.11+ installed
- Node.js 18+ installed
- PostgreSQL 14+ installed (or access to Neon Serverless PostgreSQL)
- Git installed

## Setup Instructions

### 1. Clone and Navigate to Repository
```bash
git clone [repository-url]
cd [repository-name]
```

### 2. Backend Setup (FastAPI)

#### Navigate to Backend Directory
```bash
cd backend
```

#### Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### Install Dependencies
```bash
pip install -r requirements.txt
```

#### Set Environment Variables
Create a `.env` file in the backend root:
```env
DATABASE_URL=postgresql://username:password@localhost:5432/todo_app
BETTER_AUTH_SECRET=your-secret-key-here
JWT_SECRET=your-jwt-secret-here
```

#### Run Database Migrations
```bash
alembic upgrade head
```

#### Start Backend Server
```bash
uvicorn src.main:app --reload --port 8000
```

Backend will be available at `http://localhost:8000`

### 3. Frontend Setup (Next.js)

#### Navigate to Frontend Directory
```bash
cd frontend  # from project root
```

#### Install Dependencies
```bash
npm install
```

#### Set Environment Variables
Create a `.env.local` file in the frontend root:
```env
NEXT_PUBLIC_API_URL=http://localhost:8000
NEXT_PUBLIC_BETTER_AUTH_URL=http://localhost:8000
```

#### Start Frontend Development Server
```bash
npm run dev
```

Frontend will be available at `http://localhost:3000`

## API Endpoints

### Authentication
- `POST /api/auth/signup` - Create new user account
- `POST /api/auth/signin` - Login user
- `POST /api/auth/signout` - Logout user

### Tasks
- `GET /api/tasks` - Get all user tasks
- `POST /api/tasks` - Create new task
- `GET /api/tasks/{id}` - Get specific task
- `PUT /api/tasks/{id}` - Update task
- `DELETE /api/tasks/{id}` - Delete task

## Running Tests

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

## Environment Variables

### Backend (.env)
- `DATABASE_URL` - PostgreSQL connection string
- `BETTER_AUTH_SECRET` - Secret for Better Auth
- `JWT_SECRET` - Secret for JWT token signing
- `ACCESS_TOKEN_EXPIRE_MINUTES` - Token expiration time (default: 1440 minutes)

### Frontend (.env.local)
- `NEXT_PUBLIC_API_URL` - Backend API URL
- `NEXT_PUBLIC_BETTER_AUTH_URL` - Better Auth URL

## Development Commands

### Backend
- `uvicorn src.main:app --reload` - Start development server
- `alembic revision --autogenerate -m "migration message"` - Generate migration
- `alembic upgrade head` - Apply migrations
- `python -m pytest` - Run tests

### Frontend
- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run start` - Start production server
- `npm test` - Run tests
- `npm run lint` - Run linter

## Database Schema Initialization

The application uses SQLModel ORM with Alembic for migrations. Initial schema includes:

- `users` table with email, password_hash, timestamps
- `tasks` table with title, description, completion status, due_date, user reference

Migrations are automatically applied when running `alembic upgrade head`.

## Authentication Flow

1. User registers via `/api/auth/signup` with email and password
2. System creates user and returns JWT token
3. User includes JWT in Authorization header for protected endpoints
4. Backend validates token and allows access to user-specific data only
5. User can log out via `/api/auth/signout`

## Common Issues and Solutions

### Database Connection Issues
- Ensure PostgreSQL is running
- Check `DATABASE_URL` in backend `.env` file
- Verify database exists and credentials are correct

### Authentication Issues
- Ensure `BETTER_AUTH_SECRET` and `JWT_SECRET` are set
- Check that tokens are properly included in requests
- Verify that token hasn't expired

### Frontend-Backend Communication
- Ensure both servers are running
- Check that `NEXT_PUBLIC_API_URL` points to correct backend URL
- Verify CORS settings in backend

## Next Steps

1. Implement user authentication flow
2. Create task management endpoints
3. Build frontend UI components
4. Connect frontend to backend API
5. Add comprehensive error handling
6. Implement proper validation and security measures