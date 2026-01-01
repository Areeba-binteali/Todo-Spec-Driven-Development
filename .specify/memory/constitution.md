<!--
Sync Impact Report:
- Version change: 0.0.0 → 1.0.0
- Added sections:
  - Project Purpose
  - Core Principles
  - Key Standards
  - Functional Scope (Phase I only)
  - Data Constraints
  - Technical Constraints
  - Project Structure Requirements
  - Out of Scope (explicitly excluded)
- Templates requiring updates:
  - ✅ .specify/templates/plan-template.md
  - ✅ .specify/templates/spec-template.md
  - ✅ .specify/templates/tasks-template.md
-->

# Phase I – In-Memory Todo Console Application Constitution

## Project Purpose

Build a foundational command-line Todo application that demonstrates spec-driven, agentic software development using Claude Code and Spec-Kit Plus. This phase focuses strictly on core CRUD functionality and clean architecture, serving as the base for future evolutionary phases.

## Core Principles

### I. Spec-First Development
No implementation before finalized specifications.

### II. Agentic Workflow
All development to follow spec → plan → tasks → implementation via Claude Code.

### III. No Manual Coding
All code must be generated through Claude Code.

### IV. Simplicity, Clarity, and Correctness
Prioritize simplicity, clarity, and correctness over feature richness.

### V. Clean Code
Code must be clean, readable, and maintainable Python code.

## Key Standards

- All features must be explicitly defined in specifications before coding.
- Each module must have a single responsibility.
- Business logic must be separated from CLI input/output.
- Task identifiers must be unique and stable during runtime.
- All user-facing messages must be clear and deterministic.
- Invalid operations must be safely handled with informative errors.

## Functional Scope (Phase I only)

- Add a task with title and optional description.
- View all tasks with clear status indicators.
- Update task title and/or description by ID.
- Delete a task by ID.
- Mark a task as complete or incomplete.

## Data Constraints

- Tasks are stored in memory only.
- No file system persistence.
- No database usage.
- Data resets on every application restart.

## Technical Constraints

- Language: Python 3.13+
- Runtime: Console / CLI
- Environment: UV + WSL 2 (Linux)
- External services: None
- No network or API calls.

## Project Structure Requirements

- `/src` directory for Python source code.
- Clear separation between models, services, and CLI entry point.
- `specs/history` directory containing all specification iterations.
- `README.md` with setup and execution instructions.
- `CLAUDE.md` documenting Claude Code usage and prompts.

## Out of Scope (explicitly excluded)

- Priorities, tags, or categories.
- Search, filtering, or sorting.
- Due dates, reminders, or recurring tasks.
- AI, chatbot, or natural language interfaces.
- Persistence, cloud deployment, or containers.

## Governance

This Constitution is the single source of truth for project principles, standards, and scope. It supersedes all other practices and guidance. Amendments require formal review, documentation, and a migration plan for affected artifacts. All development activities, code reviews, and specification changes must verify compliance with this constitution.

**Version**: 1.0.0 | **Ratified**: 2026-01-02 | **Last Amended**: 2026-01-02