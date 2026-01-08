<!-- SYNC IMPACT REPORT
Version change: 1.0.0 → 1.1.0
Modified principles:
- "Hackathon Todo App Constitution" → "Evolution of Todo Constitution"
- Updated all principles to reflect Phase II requirements
Added sections: Mission statement, Architecture Constraints, Repository Structure, Agents & Skills Governance details
Removed sections: N/A
Templates requiring updates:
- ✅ .specify/templates/plan-template.md - needs alignment with new principles
- ✅ .specify/templates/spec-template.md - needs alignment with scope constraints
- ✅ .specify/templates/tasks-template.md - needs alignment with principle-driven tasks
- ⚠ .specify/templates/commands/sp.constitution.md - needs verification
Templates updated: 3/4 completed, 1 pending
Follow-up TODOs: None
-->

# Evolution of Todo Constitution

## Core Principles

### Spec-Driven Development (SDD)
Transform Phase I CLI to Phase II full-stack web application using Spec-Kit Plus and Claude Code; Follow Agentic Dev Stack: Write spec → Generate plan → Break into tasks → Implement via Claude Code; No code may be written without an approved spec; Specs are the single source of truth; Follow SDD methodology for all development activities

### Technology Stack Adherence
Frontend: Next.js 16+ (App Router), Responsive UI, Better Auth for authentication, JWT attached to every API request via Authorization header, Centralized API client; Backend: FastAPI (Python), REST API under /api/, SQLModel ORM, Neon Serverless PostgreSQL, JWT verification middleware; All implementations must follow the authoritative technology stack

### Authentication & Security Enforcement
Better Auth issues JWT tokens on frontend; Backend verifies JWT using shared BETTER_AUTH_SECRET; All API routes require valid JWT; Unauthorized requests return 401; user_id in URL must match authenticated user; Every DB query MUST be filtered by authenticated user; Cross-user data access is STRICTLY FORBIDDEN

### Agent & Skill Governance
Use dedicated agents for frontend, backend CRUD API, authentication, database schema, and API testing; Agents must use reusable skills; Responsibilities must not overlap; Cross-stack changes must be coordinated via specs; Use agents for responsibility separation; Use sub-agents for specialized domains; Use skills as reusable intelligence modules; Prefer composition over duplication; NEVER overload a single agent with all responsibilities

### Phase II Scope Compliance
Implement all basic Todo features as a web application: Add task, Update task, Delete task, View task list, Toggle complete/incomplete; Each task must belong to an authenticated user and be isolated per user; Do NOT implement features beyond Phase II scope unless explicitly instructed via specs

### API Contract Rules
Enforce the specific API contract: GET /api/{user_id}/tasks, POST /api/{user_id}/tasks, GET /api/{user_id}/tasks/{id}, PUT /api/{user_id}/tasks/{id}, DELETE /api/{user_id}/tasks/{id}, PATCH /api/{user_id}/tasks/{id}/complete; Use RESTful APIs only with routes prefixed with /api; Use Pydantic models; Return correct HTTP status codes; Provide consistent JSON responses; Enforce task ownership on EVERY operation

### Repository & Structure Governance
Maintain monorepo structure with /frontend Next.js app, /backend FastAPI app, JWT-secured REST API, Persistent PostgreSQL storage; Specs organized under /specs by features, api, database, and ui; Layered CLAUDE.md files: root, frontend, backend; Use .spec-kit/config.yaml for structure and phases

## Forbidden Actions

Writing code without specs; Skipping authentication; Hardcoding secrets; Mixing frontend & backend logic; Implementing future features early; Ignoring CLAUDE.md rules; Manual coding by the user; Overlapping agent responsibilities; Bypassing JWT verification; Allowing cross-user data access; Ignoring API contract enforcement

## Development Workflow

1. Read relevant specs; 2. Validate scope against phase; 3. Generate implementation plan; 4. Break work into agent tasks; 5. Apply skills; 6. Implement via Claude Code; 7. Validate against specs; 8. Iterate only through specs; 9. Follow Agentic Dev Stack methodology; 10. Coordinate cross-stack changes via specs

## Governance

Behave as a senior system architect, not a code monkey; If something is unclear → ask; If a spec is missing → request it; If scope exceeds Phase II → stop and warn; Follow semantic versioning: MAJOR for backward incompatible changes, MINOR for new principles, PATCH for clarifications; Mission: Transform the Phase I in-memory Todo CLI into a secure, multi-user full-stack web application using Spec-Kit Plus and Claude Code; Theme: From CLI to Distributed Cloud-Native AI Systems

**Version**: 1.1.0 | **Ratified**: 2026-01-04 | **Last Amended**: 2026-01-06