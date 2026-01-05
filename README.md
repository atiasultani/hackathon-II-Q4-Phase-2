# Todo App Phase II

A full-stack todo application with user authentication, REST API, and database integration. The system allows users to register, authenticate, and manage their personal todo lists with proper data isolation between users.

## Tech Stack

- **Frontend**: Next.js 16+, TypeScript, Tailwind CSS
- **Backend**: FastAPI, Python 3.11, SQLModel ORM
- **Database**: PostgreSQL 14+
- **Authentication**: JWT-based with Better Auth
- **Styling**: Tailwind CSS

## Project Structure

```
backend/
├── src/
│   ├── models/
│   │   ├── user.py
│   │   └── task.py
│   ├── schemas/
│   │   ├── user.py
│   │   └── task.py
│   ├── services/
│   │   ├── user_service.py
│   │   └── task_service.py
│   ├── api/
│   │   ├── auth.py
│   │   └── tasks.py
│   ├── auth/
│   │   └── jwt.py
│   └── main.py
├── requirements.txt
└── alembic/
    └── versions/

frontend/
├── app/
│   ├── (auth)/
│   │   ├── login/
│   │   └── signup/
│   ├── dashboard/
│   ├── components/
│   │   ├── TaskForm.tsx
│   │   ├── TaskItem.tsx
│   │   └── TaskList.tsx
│   ├── contexts/
│   │   └── AuthContext.tsx
│   └── types/
│       └── task.ts
├── package.json
├── tailwind.config.js
└── .env.local
```

## Setup Instructions

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set environment variables in `.env`:
   ```env
   DATABASE_URL=postgresql://username:password@localhost:5432/todo_app
   JWT_SECRET=your-jwt-secret-here
   ACCESS_TOKEN_EXPIRE_MINUTES=1440
   ```

5. Run database migrations:
   ```bash
   alembic upgrade head
   ```

6. Start the backend server:
   ```bash
   uvicorn src.main:app --reload --port 8000
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Set environment variables in `.env.local`:
   ```env
   NEXT_PUBLIC_API_URL=http://localhost:8000
   ```

4. Start the development server:
   ```bash
   npm run dev
   ```

The frontend will be available at `http://localhost:3000`.

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

## Security Features

- JWT-based authentication required for all protected endpoints
- User data isolation - users can only access their own tasks
- Input validation on all endpoints
- Proper error handling without information leakage