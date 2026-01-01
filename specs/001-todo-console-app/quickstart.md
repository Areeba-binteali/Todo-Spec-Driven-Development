# Quickstart: In-Memory Todo Console Application

This guide explains how to run the application and use its features.

## Prerequisites

- Python 3.13+
- No external dependencies are required.

## Running the Application

1. Navigate to the `src` directory.
2. Run the main application file:
   ```bash
   python main.py
   ```

## How to Use

The application will present you with a menu of options:

1.  **Add a new task**: Prompts you for a title and an optional description.
2.  **View all tasks**: Displays a list of all tasks with their details.
3.  **Update a task**: Asks for a task ID and then prompts for a new title and/or description.
4.  **Delete a task**: Asks for a task ID and removes the task.
5.  **Mark a task as complete/incomplete**: Asks for a task ID and toggles the completion status.
6.  **Exit**: Exits the application.

### Example Workflow

1. Run `python main.py`.
2. Choose option `1` to add a task.
   - Title: `Buy milk`
   - Description: `From the corner store`
3. Choose option `2` to view all tasks. You should see the "Buy milk" task listed.
4. Choose option `5` to mark the task as complete.
   - Task ID: `1`
5. Choose option `2` again. You should see the "Buy milk" task marked as complete.
6. Choose option `4` to delete the task.
   - Task ID: `1`
7. Choose option `2` again. You should see a message that there are no tasks.
8. Choose option `6` to exit.
