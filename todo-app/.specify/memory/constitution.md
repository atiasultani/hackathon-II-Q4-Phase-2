<!-- SYNC IMPACT REPORT
Version change: N/A (initial version) → 1.0.0
Modified principles: N/A
Added sections: All principles and sections (initial creation)
Removed sections: N/A
Templates requiring updates:
- ✅ .specify/templates/plan-template.md - needs alignment with new principles
- ✅ .specify/templates/spec-template.md - needs alignment with scope constraints
- ✅ .specify/templates/tasks-template.md - needs alignment with principle-driven tasks
- ⚠ .specify/templates/commands/sp.constitution.md - needs verification
Templates updated: 3/4 completed, 1 pending
Follow-up TODOs: None
-->

# Hackathon Todo App Constitution

## Core Principles

### Spec-Driven Development (SDD)
Follow specs before writing or generating any code; Use agents and skills as reusable intelligence; Enforce clean separation of frontend, backend, and specs; Maintain professional, production-grade structure

### Technology Stack Adherence
Use Next.js 16+ (App Router), TypeScript, Tailwind CSS for frontend; Python FastAPI, SQLModel ORM for backend; Neon Serverless PostgreSQL for database; Better Auth for authentication; All implementations must follow the authoritative technology stack

### Authentication & Security Enforcement
All API endpoints REQUIRE JWT authentication; JWT must be sent as Authorization: Bearer <token>; JWT must be verified using BETTER_AUTH_SECRET; Every DB query MUST be filtered by authenticated user; Cross-user data access is STRICTLY FORBIDDEN

### Agent & Skill Governance
Use agents for responsibility separation; Use sub-agents for specialized domains; Use skills as reusable intelligence modules; Prefer composition over duplication; NEVER overload a single agent with all responsibilities

### Phase II Scope Compliance
Implement only Basic Level features (Add Task, Delete Task, Update Task, View Task List, Mark Task as Complete); Do NOT implement Intermediate, Advanced, or Exceptional features unless explicitly instructed via specs

### API Contract Rules
Use RESTful APIs only with routes prefixed with /api; Use Pydantic models; Return correct HTTP status codes; Provide consistent JSON responses; Enforce task ownership on EVERY operation

## Forbidden Actions

Writing code without specs; Skipping authentication; Hardcoding secrets; Mixing frontend & backend logic; Implementing future features early; Ignoring CLAUDE.md rules; Manual coding by the user

## Development Workflow

1. Read relevant specs; 2. Validate scope against phase; 3. Generate implementation plan; 4. Break work into agent tasks; 5. Apply skills; 6. Implement via Claude Code; 7. Validate against specs; 8. Iterate only through specs

## Governance

Behave as a senior system architect, not a code monkey; If something is unclear → ask; If a spec is missing → request it; If scope exceeds Phase II → stop and warn; Follow semantic versioning: MAJOR for backward incompatible changes, MINOR for new principles, PATCH for clarifications

**Version**: 1.0.0 | **Ratified**: 2026-01-04 | **Last Amended**: 2026-01-04