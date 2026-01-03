# Todo App

A full-stack todo application built with Next.js, FastAPI, and PostgreSQL.

## Features

- User authentication and authorization
- Create, read, update, and delete tasks
- Mark tasks as complete/incomplete
- Responsive UI for all device sizes

## Tech Stack

- **Frontend**: Next.js 16+, TypeScript, Tailwind CSS
- **Backend**: Python FastAPI, SQLModel ORM
- **Database**: PostgreSQL
- **Authentication**: Better Auth

## Setup Instructions

### Prerequisites

- Node.js 18+
- Python 3.9+
- PostgreSQL (or use SQLite for development)

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   ```bash
   cp ../.env .env
   # Update the .env file with your database credentials
   ```

4. Run the application:
   ```bash
   python main.py
   ```

The backend will be available at `http://localhost:8000`.

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Run the development server:
   ```bash
   npm run dev
   ```

The frontend will be available at `http://localhost:3000`.

## API Endpoints

### Authentication
- `POST /api/auth/register` - User registration
- `POST /api/auth/login` - User login
- `GET /api/auth/me` - Get current user info

### Tasks
- `GET /api/tasks` - Get all user's tasks
- `POST /api/tasks` - Create new task
- `GET /api/tasks/{task_id}` - Get specific task
- `PUT /api/tasks/{task_id}` - Update task
- `DELETE /api/tasks/{task_id}` - Delete task
- `PATCH /api/tasks/{task_id}/complete` - Mark task as complete/incomplete

## Environment Variables

The application uses the following environment variables:

- `DATABASE_URL` - Database connection string
- `BETTER_AUTH_SECRET` - Secret key for authentication
- `BETTER_AUTH_URL` - Base URL for auth
- `NEXT_PUBLIC_API_URL` - API URL for frontend

## Running Tests

Backend tests:
```bash
cd backend
python -m pytest tests/
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request