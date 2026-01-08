---
description: "Task list for Evolution of Todo - Phase II implementation"
---

# Tasks: Evolution of Todo - Phase II

**Input**: Design documents from `/specs/001-todo-evolution/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Tests are OPTIONAL - only included where explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Web app**: `backend/src/`, `frontend/src/`
- **API**: `backend/src/api/`
- **Models**: `backend/src/models/`
- **Schemas**: `backend/src/schemas/`
- **Services**: `backend/src/services/`
- **Frontend components**: `frontend/src/components/`
- **Frontend pages**: `frontend/src/pages/`

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create backend project structure with FastAPI dependencies in backend/
- [X] T002 Create frontend project structure with Next.js dependencies in frontend/
- [X] T003 [P] Initialize backend Python project with FastAPI, SQLModel, and Neon PostgreSQL dependencies in backend/requirements.txt
- [X] T004 [P] Initialize frontend Next.js project with TypeScript, Tailwind CSS, and Better Auth dependencies in frontend/package.json
- [X] T005 [P] Configure project linting, formatting, and pre-commit hooks for both backend and frontend

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T006 Setup database schema and migrations framework using Alembic in backend/alembic/
- [X] T007 [P] Implement authentication/authorization framework with Better Auth and JWT in backend/src/auth/
- [X] T008 [P] Setup API routing and middleware structure in backend/src/main.py and backend/src/api/
- [X] T009 Create base models/entities that all stories depend on in backend/src/models/
- [X] T010 Configure error handling and logging infrastructure in backend/src/utils/
- [X] T011 Setup environment configuration management in backend/src/config.py
- [X] T012 [P] Configure CORS and security middleware in backend/src/main.py
- [X] T013 [P] Set up centralized API client for frontend in frontend/src/services/apiClient.ts

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - User Registration and Authentication (Priority: P1) 🎯 MVP

**Goal**: Enable new users to register for an account and authenticate so that they can securely access their todo tasks

**Independent Test**: Can be fully tested by registering a new user, authenticating, and verifying that a JWT token is issued that can be used for subsequent requests

### Implementation for User Story 1

- [X] T014 [P] [US1] Create User model in backend/src/models/user.py based on data model specification
- [X] T015 [P] [US1] Create User schemas (UserCreate, UserRead) in backend/src/schemas/user.py
- [X] T016 [US1] Implement UserService with registration and authentication methods in backend/src/services/user_service.py
- [X] T017 [US1] Implement authentication endpoints in backend/src/api/auth.py (register, login, logout)
- [X] T018 [US1] Implement JWT token generation and validation in backend/src/auth/jwt.py
- [X] T019 [P] [US1] Create LoginForm component in frontend/src/components/LoginForm.tsx
- [X] T020 [P] [US1] Create RegisterForm component in frontend/src/components/RegisterForm.tsx
- [X] T021 [US1] Create login page in frontend/src/pages/login.tsx
- [X] T022 [US1] Create register page in frontend/src/pages/register.tsx
- [X] T023 [US1] Implement AuthContext for frontend authentication state management in frontend/src/contexts/AuthContext.tsx
- [X] T024 [US1] Add authentication validation to API client in frontend/src/services/apiClient.ts
- [X] T025 [US1] Add user registration and login functionality with error handling

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Basic Task Management (Priority: P1)

**Goal**: Enable authenticated users to create, read, update, and delete their own tasks so that they can manage their personal todo list

**Independent Test**: Can be fully tested by authenticating as a user and performing all CRUD operations on tasks, verifying that only the authenticated user's tasks are accessible

### Implementation for User Story 2

- [X] T026 [P] [US2] Create Task model in backend/src/models/task.py based on data model specification
- [X] T027 [P] [US2] Create Task schemas (TaskCreate, TaskRead, TaskUpdate) in backend/src/schemas/task.py
- [X] T028 [US2] Implement TaskService with CRUD operations in backend/src/services/task_service.py
- [X] T029 [US2] Implement task endpoints in backend/src/api/tasks.py (GET, POST, PUT, DELETE for /api/{user_id}/tasks)
- [X] T030 [US2] Add user isolation validation middleware to ensure user_id in URL matches authenticated user
- [X] T031 [P] [US2] Create TaskForm component in frontend/src/components/TaskForm.tsx
- [X] T032 [P] [US2] Create TaskList component in frontend/src/components/TaskList.tsx
- [X] T033 [P] [US2] Create TaskItem component in frontend/src/components/TaskItem.tsx
- [X] T034 [US2] Create dashboard page in frontend/src/pages/dashboard.tsx
- [X] T035 [US2] Implement task CRUD operations in frontend with API calls
- [X] T036 [US2] Add proper error handling for task operations
- [X] T037 [US2] Add loading states and UI feedback for task operations

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Task Completion Toggle (Priority: P2)

**Goal**: Enable authenticated users to mark tasks as complete or incomplete so that they can track their progress on their todo list

**Independent Test**: Can be fully tested by authenticating as a user, creating tasks, and toggling their completion status, verifying that the changes are persisted and only affect my tasks

### Implementation for User Story 3

- [X] T038 [US3] Implement PATCH endpoint for task completion toggle in backend/src/api/tasks.py (/api/{user_id}/tasks/{id}/complete)
- [X] T039 [US3] Add toggle completion method to TaskService in backend/src/services/task_service.py
- [X] T040 [P] [US3] Update TaskItem component to include completion toggle functionality in frontend/src/components/TaskItem.tsx
- [X] T041 [US3] Implement completion toggle API call in frontend TaskItem component
- [X] T042 [US3] Add visual indication of completion status in TaskItem component
- [X] T043 [US3] Add TaskToggleComplete schema in backend/src/schemas/task.py

**Checkpoint**: At this point, User Stories 1, 2, AND 3 should all work independently

---

## Phase 6: User Story 4 - Secure Multi-User Isolation (Priority: P1)

**Goal**: Ensure that authenticated users can only access their own tasks and not see other users' tasks so that their data remains private and secure

**Independent Test**: Can be fully tested by having multiple users with tasks, authenticating as one user, and verifying that only that user's tasks are accessible

### Implementation for User Story 4

- [X] T044 [US4] Implement comprehensive user isolation validation across all backend endpoints
- [X] T045 [US4] Add database-level user filtering to all task queries in TaskService
- [X] T046 [US4] Add comprehensive error handling for unauthorized access attempts
- [X] T047 [US4] Implement 401 Unauthorized responses for invalid JWT tokens
- [X] T048 [US4] Implement 403 Forbidden responses when user_id in URL doesn't match authenticated user
- [X] T049 [US4] Add validation to ensure all API endpoints verify user_id matches authenticated user
- [X] T050 [US4] Add frontend error handling for unauthorized access responses
- [X] T051 [US4] Add user feedback for access denied scenarios

**Checkpoint**: All user stories should now be independently functional

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T052 [P] Add comprehensive documentation in docs/
- [X] T053 Code cleanup and refactoring across all components
- [X] T054 Add comprehensive error handling and user feedback throughout the application
- [X] T055 [P] Add additional unit tests in backend/tests/unit/ and frontend/tests/
- [X] T056 Add security hardening and input validation
- [X] T057 Run quickstart.md validation to ensure smooth setup experience
- [X] T058 Add responsive design improvements to UI components
- [X] T059 Add loading states and better UX feedback
- [X] T060 Performance optimization across all user stories

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - Depends on User authentication (US1) for user context
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - Depends on User authentication and Tasks (US1, US2)
- **User Story 4 (P1)**: Can start after Foundational (Phase 2) - Depends on User authentication and Tasks (US1, US2), but can be implemented in parallel with other stories

### Within Each User Story

- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 2

```bash
# Launch all models for User Story 2 together:
Task: "Create Task model in backend/src/models/task.py"
Task: "Create Task schemas in backend/src/schemas/task.py"

# Launch frontend components for User Story 2 together:
Task: "Create TaskForm component in frontend/src/components/TaskForm.tsx"
Task: "Create TaskList component in frontend/src/components/TaskList.tsx"
Task: "Create TaskItem component in frontend/src/components/TaskItem.tsx"
```

---

## Implementation Strategy

### MVP First (User Stories 1 and 2 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1 (Authentication)
4. Complete Phase 4: User Story 2 (Basic Task Management)
5. **STOP and VALIDATE**: Test User Stories 1 and 2 independently - this is a functional MVP!
6. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo
3. Add User Story 2 → Test independently → Deploy/Demo (Now have full CRUD!)
4. Add User Story 3 → Test independently → Deploy/Demo (Now have completion toggling!)
5. Add User Story 4 → Test independently → Deploy/Demo (Now have complete security!)
6. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Stories 3 and 4
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify dependencies are properly handled
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- User Story 2 has dependency on User Story 1 (authentication) for user context
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence