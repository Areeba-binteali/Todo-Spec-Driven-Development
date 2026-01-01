# Tasks: In-Memory Todo Console Application

**Input**: Design documents from `specs/001-todo-console-app/`
**Prerequisites**: plan.md, spec.md, data-model.md

## Phase 1: Setup (Shared Infrastructure)
**Purpose**: Project initialization and basic structure
- [X] T001 Create project structure: `src/main.py`, `src/models.py`, `src/services.py`

---

## Phase 2: Foundational (Blocking Prerequisites)
**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented
- [X] T002 [US1] Implement the `Task` data model in `src/models.py` with `id`, `title`, `description`, and `completed` attributes.
- [X] T003 [US1] Implement an in-memory task storage collection in `src/services.py`.

---

## Phase 3: User Story 1 - Add a Task (Priority: P1)
**Goal**: Allow users to add a new task.
**Independent Test**: A user can add a task and see it in the list of all tasks.
### Implementation for User Story 1
- [X] T004 [US1] Implement the "add task" service in `src/services.py` to create and store a new task.
- [X] T005 [US1] Implement the CLI command in `src/main.py` to accept a title and optional description for a new task.

---

## Phase 4: User Story 2 - View All Tasks (Priority: P1)
**Goal**: Allow users to view all tasks.
**Independent Test**: After adding tasks, a user can see them listed.
### Implementation for User Story 2
- [X] T006 [US2] Implement the "view tasks" service in `src/services.py` to retrieve all tasks.
- [X] T007 [US2] Implement the CLI command in `src/main.py` to display all tasks with their details.

---

## Phase 5: User Story 3 - Update a Task (Priority: P2)
**Goal**: Allow users to update an existing task.
**Independent Test**: A user can update a task's title or description.
### Implementation for User Story 3
- [X] T008 [US3] Implement the "update task" service in `src/services.py` to locate a task by ID and update its attributes.
- [X] T009 [US3] Implement the CLI command in `src/main.py` to accept a task ID and the new title/description.

---

## Phase 6: User Story 4 - Mark a Task as Complete (Priority: P2)
**Goal**: Allow users to mark a task as complete or incomplete.
**Independent Test**: A user can toggle the completion status of a task.
### Implementation for User Story 4
- [X] T010 [US4] Implement the "toggle task completion" service in `src/services.py`.
- [X] T011 [US4] Implement the CLI command in `src/main.py` to accept a task ID and toggle its completion status.

---

## Phase 7: User Story 5 - Delete a Task (Priority: P3)
**Goal**: Allow users to delete a task.
**Independent Test**: A user can delete a task, and it will no longer be visible.
### Implementation for User Story 5
- [X] T012 [US5] Implement the "delete task" service in `src/services.py`.
- [X] T013 [US5] Implement the CLI command in `src/main.py` to accept a task ID and delete the corresponding task.

---

## Phase 8: Polish & Cross-Cutting Concerns
**Purpose**: Finalize the application and create documentation.
- [X] T014 Implement the main application loop in `src/main.py` to allow for repeated operations.
- [X] T015 Generate `README.md` with setup and execution instructions.
- [X] T016 Generate `GEMINI.md` describing the spec-driven development process.
- [X] T017 Manually validate all features and test edge cases.

---

## Dependencies & Execution Order
- **Phase 1** must be completed before all other phases.
- **Phase 2** must be completed before Phases 3-7.
- **Phases 3-7** can be implemented in any order after Phase 2 is complete, but following the priority order is recommended.
- **Phase 8** should be completed last.
