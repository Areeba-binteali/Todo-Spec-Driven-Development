---
id: 0002
title: Update Constitution for Phase II Full-Stack App
stage: constitution
date: 2026-01-06
surface: agent
model: gemini
feature: none
branch: main
user: (unknown)
command: /sp.constitution
labels: [constitution, phase-2, architecture]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
  - README.md
  - specs/001-todo-console-app/quickstart.md
tests:
  - null
---

## Prompt

/sp.constitution Project: Phase II – Full-Stack Todo Web Application (Multi-User, Authenticated, Persistent)Purpose:Transform the Phase I in-memory console todo app into a modern, production-style full-stack web application with authentication, persistent storage, and a clean API-first architecture using spec-driven development.Core Principles:- Spec-First Development: No implementation without an explicit spec.- Zero Manual Coding: All code must be generated via Claude Code based on specs.- Separation of Concerns: Frontend, backend, auth, and database concerns must be clearly separated.- User Isolation & Security: Every operation must be scoped to the authenticated user.- Deterministic Behavior: No guessing, hallucination, or inferred behavior beyond the specs.Architecture Principles:- Monorepo structure using Spec-Kit conventions.- Frontend (Next.js) and Backend (FastAPI) are independent services.- Communication strictly via REST APIs.- Authentication handled on frontend, authorization enforced on backend.- Database is the single source of truth for tasks.Authentication & Security Rules:- Better Auth is the only authentication provider.- JWT-based authentication is mandatory for all API requests.- Every backend request must:  - Verify JWT signature using shared secret (BETTER_AUTH_SECRET).  - Extract authenticated user identity from token.  - Enforce ownership checks on all task operations.- Requests without valid JWT must return 401 Unauthorized.- Users must never access or mutate other users’ tasks.API Design Rules:- RESTful endpoints only.- All endpoints are namespaced under `/api/`.- All task queries must be filtered by authenticated user ID.- Consistent request/response schemas using Pydantic models.- Explicit HTTP status codes for success and error cases.Data & Persistence Rules:- Use Neon Serverless PostgreSQL as the database.- Use SQLModel as the ORM.- Tasks must be persisted with:  - user_id (ownership)  - title  - description  - completion status  - timestamps- No in-memory or mock storage in Phase II.Frontend Rules:- Next.js App Router (16+).- Responsive UI (desktop + mobile).- All API calls go through a centralized API client.- JWT token must be attached to every API request.- UI must reflect authenticated user state (logged in/out).- No direct database or backend logic in frontend.Spec-Kit Rules:- Every feature must have a corresponding spec file.- Specs must live under `/specs` following Spec-Kit structure.- Claude Code must reference specs using `@specs/...`.- If behavior changes, specs must be updated before implementation.- Specs are the source of truth, not the code.Out of Scope (Explicitly Forbidden):- No AI chatbot features in Phase II.- No natural language task control.- No background jobs, reminders, or scheduling.- No business logic inside frontend components.- No shared sessions or cookies between frontend and backend.Quality Standards:- Clean, readable, modular code.- Predictable API behavior.- Clear error handling and validation.- Production-style folder structure.- Ready for extension in Phase III (chatbot integration).Success Criteria:- Multi-user todo app with authentication.- Persistent task storage in PostgreSQL.- Secure JWT-based API access.- Clean separation between frontend, backend, and database.- Fully spec-driven implementation traceable through Spec-Kit history.

## Response snapshot

Updated the project constitution to version 2.0.0 to reflect the transition to a full-stack web application (Phase II). The constitution was completely rewritten with new principles for frontend (Next.js), backend (FastAPI), database (PostgreSQL), and authentication. Also updated the main README.md and the quickstart guide for the now-obsolete console app.

## Outcome

- ✅ Impact: Major. Pivoted the project direction from a CLI app to a full-stack web app.
- 🧪 Tests: N/A
- 📁 Files: 3 files updated: constitution, README, and an old quickstart guide.
- 🔁 Next prompts: User may proceed with `/sp.specify` for the new web application feature.
- 🧠 Reflection: The agent correctly identified the need for a major version bump and propagated changes to related documentation. The fallback to agent-native PHR creation worked as designed.

## Evaluation notes (flywheel)

- Failure modes observed: None observed.
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): N/A
