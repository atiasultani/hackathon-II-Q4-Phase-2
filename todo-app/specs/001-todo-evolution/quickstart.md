# Quickstart Guide: Evolution of Todo - Phase II

## Prerequisites

- Node.js 18+ for frontend development
- Python 3.11+ for backend development
- PostgreSQL-compatible database (Neon Serverless PostgreSQL recommended)
- Git for version control
- Docker (optional, for containerized development)

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-name>
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

#### Environment Configuration
Create a `.env` file in the backend directory:
```env
DATABASE_URL=postgresql://username:password@localhost:5432/todo_app
BETTER_AUTH_SECRET=your-super-secret-jwt-key-here-make-it-long-and-random
NEON_DATABASE_URL=your-neon-serverless-database-url
```

#### Initialize Database
```bash
# Run database migrations
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

#### Environment Configuration
Create a `.env.local` file in the frontend directory:
```env
NEXT_PUBLIC_API_BASE_URL=http://localhost:8000/api
NEXT_PUBLIC_BETTER_AUTH_URL=http://localhost:8000/auth
```

#### Start Frontend Development Server
```bash
npm run dev
```

Frontend will be available at `http://localhost:3000`

## API Endpoints

### Authentication Endpoints
- `POST /api/auth/register` - Register a new user
- `POST /api/auth/login` - Login and get JWT token
- `POST /api/auth/logout` - Logout (invalidate session)

### Task Management Endpoints
- `GET /api/{user_id}/tasks` - Get all tasks for a user
- `POST /api/{user_id}/tasks` - Create a new task for a user
- `GET /api/{user_id}/tasks/{id}` - Get a specific task
- `PUT /api/{user_id}/tasks/{id}` - Update a specific task
- `DELETE /api/{user_id}/tasks/{id}` - Delete a specific task
- `PATCH /api/{user_id}/tasks/{id}/complete` - Toggle task completion status

## Development Workflow

### Running Both Servers Simultaneously
Use a process manager like `concurrently`:
```bash
# From project root
npm install -g concurrently
concurrently "cd backend && uvicorn src.main:app --reload" "cd frontend && npm run dev"
```

### Running Tests
#### Backend Tests
```bash
cd backend
pytest
```

#### Frontend Tests
```bash
cd frontend
npm test
```

### Database Migrations
```bash
# From backend directory
alembic revision --autogenerate -m "Description of changes"
alembic upgrade head
```

## Environment Variables

### Backend (.env)
- `DATABASE_URL`: Database connection string
- `BETTER_AUTH_SECRET`: Secret key for JWT signing
- `NEON_DATABASE_URL`: Neon Serverless database URL (if using Neon)
- `ACCESS_TOKEN_EXPIRE_MINUTES`: JWT token expiration time (default: 30 days)

### Frontend (.env.local)
- `NEXT_PUBLIC_API_BASE_URL`: Base URL for API endpoints
- `NEXT_PUBLIC_BETTER_AUTH_URL`: Better Auth URL
- `NEXT_PUBLIC_JWT_ALGORITHM`: Algorithm used for JWT verification

## Common Commands

### Backend
- `uvicorn src.main:app --reload` - Start development server
- `pytest` - Run tests
- `black .` - Format code with black
- `mypy .` - Run type checker

### Frontend
- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run start` - Start production server
- `npm test` - Run tests
- `npm run lint` - Run linter

## Troubleshooting

### CORS Issues
Make sure your backend allows requests from your frontend origin. In `backend/src/main.py`:
```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Add your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### Database Connection Issues
- Verify your DATABASE_URL is correct
- Ensure your PostgreSQL server is running
- Check firewall settings if using remote database

### Authentication Issues
- Verify BETTER_AUTH_SECRET is the same in both frontend and backend
- Check that JWT tokens are being properly passed in Authorization headers