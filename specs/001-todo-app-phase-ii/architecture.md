# Todo App Phase II - Architecture

## High-Level System Architecture
The Todo App Phase II follows a standard three-tier architecture:
- **Frontend Layer**: React/Next.js application running in the browser
- **Backend Layer**: FastAPI server providing REST API endpoints
- **Database Layer**: PostgreSQL database storing user and task data

## Frontend ↔ Backend ↔ Database Flow
1. User interacts with the frontend application in the browser
2. Frontend makes authenticated HTTP requests to the backend API
3. Backend validates JWT tokens and processes requests
4. Backend queries/updates the database as needed
5. Backend returns JSON responses to the frontend
6. Frontend updates the UI based on API responses

## Authentication Flow (JWT-based)
1. User signs up or signs in via frontend forms
2. Backend validates credentials and generates JWT token
3. JWT token is returned to frontend and stored in memory/cookies
4. All subsequent API requests include the JWT token in Authorization header
5. Backend middleware validates JWT token for each protected endpoint
6. Tokens have expiration times and can be refreshed when needed

## Separation of Concerns
- **Frontend**: UI rendering, user interactions, form validation, API communication
- **Backend**: Authentication, business logic, data validation, API routing
- **Database**: Data persistence, relationships, constraints, indexing
- **Authentication**: User identity, session management, token generation/verification