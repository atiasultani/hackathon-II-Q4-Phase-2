---
id: 001
title: Update Project Constitution
stage: constitution
date: 2026-01-06
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: 001-todo-app-phase-ii
user: Claude Sonnet 4.5
command: /sp.constitution
labels: [constitution, governance, phase-ii]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
---

## Prompt

```text
You are governing the project "Evolution of Todo".

Current Phase: Phase II – Full-Stack Web Application.
Theme: From CLI to Distributed Cloud-Native AI Systems.

Mission:
Transform the Phase I in-memory Todo CLI into a secure, multi-user full-stack web application using Spec-Kit Plus and Claude Code. Development must be spec-driven, agentic, and free of manual coding. Students act as Product Architects, not implementers.

Development Rules:
- Follow Agentic Dev Stack: Write spec → Generate plan → Break into tasks → Implement via Claude Code.
- No code may be written without an approved spec.
- All changes must reference specs using @specs/ paths.
- Specs are the single source of truth.
- Reusable intelligence must be implemented via agents and skills.

Phase II Functional Scope:
Implement all basic Todo features as a web application:
- Add task
- Update task
- Delete task
- View task list
- Toggle complete/incomplete
Each task must belong to an authenticated user and be isolated per user.

Architecture Constraints:
Frontend:
- Next.js 16+ (App Router)
- Responsive UI
- Better Auth for authentication
- JWT attached to every API request via Authorization header
- Centralized API client

Backend:
- FastAPI (Python)
- REST API under /api/
- SQLModel ORM
- Neon Serverless PostgreSQL
- JWT verification middleware
- Enforce task ownership on every operation

Authentication & Security:
- Better Auth issues JWT tokens on frontend
- Backend verifies JWT using shared BETTER_AUTH_SECRET
- All API routes require valid JWT
- Unauthorized requests return 401
- user_id in URL must match authenticated user

API Contract (Must Be Enforced):
- GET    /api/{user_id}/tasks
- POST   /api/{user_id}/tasks
- GET    /api/{user_id}/tasks/{id}
- PUT    /api/{user_id}/tasks/{id}
- DELETE /api/{user_id}/tasks/{id}
- PATCH  /api/{user_id}/tasks/{id}/complete

Repository & Spec-Kit Structure:
- Monorepo required
- Use .spec-kit/config.yaml for structure and phases
- Specs organized under /specs by features, api, database, and ui
- Layered CLAUDE.md files: root, frontend, backend
- Claude Code must always read relevant CLAUDE.md and specs before implementing

Agents & Skills Governance:
- Dedicated agents for frontend, backend CRUD API, authentication, database schema, and API testing
- Agents must use reusable skills
- Responsibilities must not overlap
- Cross-stack changes must be coordinated via specs

Deliverables:
- Updated constitution
- Complete specs in /specs
- /frontend Next.js app
- /backend FastAPI app
- JWT-secured REST API
- Persistent PostgreSQL storage
- README.md
- CLAUDE.md files

Success Criteria:
- Full-stack app runs locally
- Authentication works end-to-end
- Users can only access their own tasks
- All CRUD operations function correctly
- Specs accurately reflect implementation
- System is ready for Phase III evolution
```

## Response snapshot

Updated the project constitution to reflect the new "Evolution of Todo" project requirements for Phase II. The updated constitution includes:

1. Changed project name from "Hackathon Todo App" to "Evolution of Todo"
2. Updated the mission to reflect transformation from CLI to distributed cloud-native AI systems
3. Enhanced the technology stack adherence principle with specific frontend and backend requirements
4. Strengthened authentication & security enforcement with detailed JWT requirements
5. Expanded agent & skill governance with specific responsibilities
6. Updated Phase II scope compliance to include all basic Todo features
7. Added detailed API contract rules with specific endpoints
8. Included repository & structure governance principle
9. Updated forbidden actions and development workflow
10. Updated governance section with mission and theme details
11. Updated version to 1.1.0 with today's date as last amended

The constitution now properly reflects the requirements for transforming the Phase I in-memory Todo CLI into a secure, multi-user full-stack web application.

## Outcome

- ✅ Impact: Updated constitution to align with Phase II requirements
- 🧪 Tests: No tests needed for documentation update
- 📁 Files: Updated .specify/memory/constitution.md
- 🔁 Next prompts: Ready to proceed with spec generation
- 🧠 Reflection: Constitution now accurately reflects project requirements

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A