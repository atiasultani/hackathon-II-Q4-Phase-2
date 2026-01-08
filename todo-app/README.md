# Evolution of Todo - Phase II

A full-stack todo application with user authentication, REST API, and database integration. The system allows users to register, authenticate, and manage their personal todo lists with proper data isolation between users.

## Overview

This project represents Phase II of the "Evolution of Todo" initiative, transforming a simple CLI application into a secure, multi-user full-stack web application. The system provides:

- User registration and authentication with JWT-based security
- Personalized todo list management with complete CRUD operations
- Secure data isolation between users
- Responsive web interface built with modern technologies

## Tech Stack

- **Frontend**: Next.js 14+, React, TypeScript, Tailwind CSS
- **Backend**: FastAPI, Python 3.11+, SQLModel ORM
- **Database**: PostgreSQL (with Neon integration)
- **Authentication**: Better Auth with JWT tokens
- **Styling**: Tailwind CSS
- **Development**: Claude Code with Spec-Kit Plus for spec-driven development

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
│   ├── database/
│   ├── utils/
│   └── main.py
├── requirements.txt
└── alembic/

frontend/
├── src/
│   ├── components/
│   ├── contexts/
│   ├── pages/
│   ├── services/
│   └── types/
├── package.json
└── tailwind.config.js

specs/
├── 001-todo-evolution/
│   ├── spec.md
│   ├── plan.md
│   └── tasks.md

history/
└── prompts/
    ├── 001-todo-evolution/
    └── constitution/
```

## Features

### Authentication
- User registration with email and password
- Secure JWT-based authentication
- Session management with token refresh
- Protected routes and API endpoints

### Task Management
- Create, read, update, and delete tasks
- Mark tasks as complete/incomplete
- Personalized task lists per user
- Real-time updates and validation

### Security
- JWT token validation on all protected endpoints
- User data isolation - users can only access their own tasks
- Input validation and sanitization
- Secure password hashing

## Setup Instructions

### Prerequisites
- Node.js 18+ for frontend
- Python 3.11+ for backend
- PostgreSQL database (Neon recommended)
- Git

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
- `PUT /api/tasks/{id}/toggle` - Toggle task completion status

## Development

### Running Tests
Backend tests:
```bash
pytest
```

Frontend tests:
```bash
npm run test
```

### Code Quality
- TypeScript for type safety
- ESLint for code linting
- Prettier for code formatting
- Type checking enforced

### Spec-Driven Development
This project follows a spec-driven development approach using Spec-Kit Plus:
- Specifications are stored in `/specs/`
- Implementation tasks are generated from specs
- Architecture decisions are documented as ADRs

## Security Features

- JWT-based authentication required for all protected endpoints
- User data isolation - users can only access their own tasks
- Input validation on all endpoints
- Proper error handling without information leakage
- Secure password hashing with bcrypt
- CORS configuration for web security

## Architecture

The application follows a clean architecture pattern:

- **Presentation Layer**: Next.js frontend with React components
- **API Layer**: FastAPI backend with REST endpoints
- **Business Logic**: Service layer with domain logic
- **Data Layer**: SQLModel ORM with PostgreSQL database

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Project Status

This project is part of the "Evolution of Todo - Phase II" initiative, implementing a secure, multi-user full-stack web application using modern web technologies and spec-driven development practices.