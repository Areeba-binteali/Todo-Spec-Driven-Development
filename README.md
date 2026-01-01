# In-Memory Todo Console Application

This is a simple command-line interface (CLI) Todo application developed as part of a spec-driven, agentic workflow. The application allows users to manage tasks directly from their terminal, with features to add, list, update, toggle completion status, and delete tasks. All tasks are stored in memory and will be reset upon application restart.

## Features

- **Add Task**: Create a new task with a title and an optional description.
- **List Tasks**: View all existing tasks with their completion status and details.
- **Update Task**: Modify the title or description of an existing task using its ID.
- **Toggle Completion**: Mark a task as complete or incomplete.
- **Delete Task**: Remove a task from the list.

## Environment Setup

This application is developed using Python. It is recommended to use a virtual environment for dependency management.

### Prerequisites

- **Python 3.13+**: Ensure you have Python 3.13 or a newer version installed. You can download it from [python.org](https://www.python.org/downloads/).
- **uv (Optional but Recommended)**: `uv` is a fast Python package installer and resolver. While not strictly required, it is recommended for managing dependencies.
  ```bash
  pip install uv
  ```
- **WSL (Windows Subsystem for Linux - for Windows users)**: If you are on Windows, using WSL can provide a more Linux-like development environment, which is often preferred for Python development. Instructions for installing WSL can be found on the [Microsoft Docs](https://docs.microsoft.com/en-us/windows/wsl/install).

### Installation

1. **Clone the repository (if applicable):**
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Create a virtual environment:**
   Using `uv` (recommended):
   ```bash
   uv venv
   ```
   Or using `python -m venv`:
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment:**
   On macOS/Linux:
   ```bash
   source .venv/bin/activate
   ```
   On Windows (Command Prompt):
   ```bash
   .venv\Scripts\activate.bat
   ```
   On Windows (PowerShell):
   ```bash
   .venv\Scripts\Activate.ps1
   ```

4. **Install dependencies:**
   This project currently has no external dependencies. If it did, you would install them here:
   ```bash
   # uv pip install -r requirements.txt
   # pip install -r requirements.txt
   ```

## How to Run

1. **Activate your virtual environment** (if not already active, see Installation steps above).
2. **Navigate to the project root directory.**
3. **Run the main application file:**
   ```bash
   python src/main.py
   ```

### Using the Application

Once the application is running, you will see a `>` prompt. Type `help` and press Enter to see the available commands.

**Example Usage:**

```
> help

Todo CLI Application
Commands:
  add <title> [description] - Add a new task
  list                      - List all tasks
  update <id> [title] [description] - Update a task
  toggle <id>               - Toggle task completion status
  delete <id>               - Delete a task
  help                      - Display this help message
  exit                      - Exit the application

> add Buy groceries
Added task: Buy groceries (ID: 6a3b0a6e6f1a4e7b9c8d0e1f2a3b4c5d)
> add Write report "Draft the quarterly financial report"
Added task: Write report (ID: 1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d)
> list
[ ] Buy groceries (ID: 6a3b0a6e6f1a4e7b9c8d0e1f2a3b4c5d)
[ ] Write report (Draft the quarterly financial report) (ID: 1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d)
> toggle 6a3b0a6e6f1a4e7b9c8d0e1f2a3b4c5d
Task 'Buy groceries' marked as completed.
> list
[✓] Buy groceries (ID: 6a3b0a6e6f1a4e7b9c8d0e1f2a3b4c5d)
[ ] Write report (Draft the quarterly financial report) (ID: 1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d)
> exit
Exiting Todo CLI. Goodbye!
```