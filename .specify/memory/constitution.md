<!--
Sync Impact Report:
- Version change: 1.0.0 → 2.0.0
- Summary: The constitution has been completely rewritten to reflect the project's transition from a simple in-memory CLI app (Phase I) to a full-stack, multi-user web application (Phase II). All principles, standards, and scope definitions have been updated.
- Removed Sections: All sections from v1.0.0.
- Added Sections:
  - Project Purpose (updated)
  - Core Principles
  - Architecture Principles
  - Authentication & Security Rules
  - API Design Rules
  - Data & Persistence Rules
  - Frontend Rules
  - Spec-Kit Rules
  - Out of Scope (Explicitly Forbidden)
  - Quality Standards
  - Success Criteria
- Templates requiring updates:
  - ⚠️ .specify/templates/plan-template.md (Constitution Check is outdated)
  - ⚠️ .specify/templates/spec-template.md (Needs sections for API endpoints, auth)
  - ⚠️ .specify/templates/tasks-template.md (Needs new phases for web development)
  - ⚠️ README.md (Outdated, needs full rewrite for web app)
  - ⚠️ specs/001-todo-console-app/quickstart.md (Outdated, needs full rewrite for web app)
-->

# Phase II – Full-Stack Todo Web Application Constitution

## Project Purpose

Transform the Phase I in-memory console todo app into a modern, production-style full-stack web application with authentication, persistent storage, and a clean API-first architecture using spec-driven development.

## Core Principles

- **Spec-First Development**: No implementation without an explicit spec.
- **Zero Manual Coding**: All code must be generated via the agent based on specs.
- **Separation of Concerns**: Frontend, backend, auth, and database concerns must be clearly separated.
- **User Isolation & Security**: Every operation must be scoped to the authenticated user.
- **Deterministic Behavior**: No guessing, hallucination, or inferred behavior beyond the specs.

## Architecture Principles

- Monorepo structure using Spec-Kit conventions.
- Frontend (Next.js) and Backend (FastAPI) are independent services.
- Communication strictly via REST APIs.
- Authentication handled on frontend, authorization enforced on backend.
- Database is the single source of truth for tasks.

## Authentication & Security Rules

- Better Auth is the only authentication provider.
- JWT-based authentication is mandatory for all API requests.
- Every backend request must:
  - Verify JWT signature using shared secret (BETTER_AUTH_SECRET).
  - Extract authenticated user identity from token.
  - Enforce ownership checks on all task operations.
- Requests without valid JWT must return 401 Unauthorized.
- Users must never access or mutate other users’ tasks.

## API Design Rules

- RESTful endpoints only.
- All endpoints are namespaced under `/api/`.
- All task queries must be filtered by authenticated user ID.
- Consistent request/response schemas using Pydantic models.
- Explicit HTTP status codes for success and error cases.

## Data & Persistence Rules

- Use Neon Serverless PostgreSQL as the database.
- Use SQLModel as the ORM.
- Tasks must be persisted with:
  - user_id (ownership)
  - title
  - description
  - completion status
  - timestamps
- No in-memory or mock storage in Phase II.

## Frontend Rules

- Next.js App Router (16+).
- Responsive UI (desktop + mobile).
- All API calls go through a centralized API client.
- JWT token must be attached to every API request.
- UI must reflect authenticated user state (logged in/out).
- No direct database or backend logic in frontend.

## Spec-Kit Rules

- Every feature must have a corresponding spec file.
- Specs must live under `/specs` following Spec-Kit structure.
- The agent must reference specs using `@specs/...`.
- If behavior changes, specs must be updated before implementation.
- Specs are the source of truth, not the code.

## Out of Scope (Explicitly Forbidden)

- No AI chatbot features in Phase II.
- No natural language task control.
- No background jobs, reminders, or scheduling.
- No business logic inside frontend components.
- No shared sessions or cookies between frontend and backend.

## Quality Standards

- Clean, readable, modular code.
- Predictable API behavior.
- Clear error handling and validation.
- Production-style folder structure.
- Ready for extension in Phase III (chatbot integration).

## Success Criteria

- Multi-user todo app with authentication.
- Persistent task storage in PostgreSQL.
- Secure JWT-based API access.
- Clean separation between frontend, backend, and database.
- Fully spec-driven implementation traceable through Spec-Kit history.

## Governance

This Constitution is the single source of truth for project principles, standards, and scope. It supersedes all other practices and guidance. Amendments require formal review, documentation, and a migration plan for affected artifacts. All development activities, code reviews, and specification changes must verify compliance with this constitution.

**Version**: 2.0.0 | **Ratified**: 2026-01-06 | **Last Amended**: 2026-01-06
