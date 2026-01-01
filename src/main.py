from src.services import TaskService

def display_help():
    print("\nTodo CLI Application")
    print("Commands:")
    print("  add <title> [description] - Add a new task")
    print("  list                      - List all tasks")
    print("  update <id> [title] [description] - Update a task")
    print("  toggle <id>               - Toggle task completion status")
    print("  delete <id>               - Delete a task")
    print("  help                      - Display this help message")
    print("  exit                      - Exit the application")

def main():
    task_service = TaskService()
    print("Welcome to Todo CLI! Type 'help' for commands.")

    while True:
        command = input("> ").strip().split(maxsplit=1)
        action = command[0].lower()
        args = command[1] if len(command) > 1 else ""

        if action == "exit":
            print("Exiting Todo CLI. Goodbye!")
            break
        elif action == "help":
            display_help()
        elif action == "add":
            title = input("Enter task title: ").strip()
            if not title:
                print("Error: Task title cannot be empty.")
                continue
            description = input("Enter task description (optional): ").strip()
            if not description:
                description = None # Set to None if empty string is entered

            task = task_service.add_task(title, description)
            print(f"Added task: {task.title} (ID: {task.id})")
        # Placeholder for other commands
        elif action == "list":
            tasks = task_service.get_all_tasks()
            if not tasks:
                print("No tasks yet. Add one with 'add <title> [description]'.")
                continue
            for task in tasks:
                status = "✓" if task.completed else " "
                desc = f" ({task.description})" if task.description else ""
                print(f"[{status}] {task.title}{desc} (ID: {task.id})")
        elif action == "update":
            parts = args.split(maxsplit=1) # Only split for ID, rest is ignored initially
            if not parts:
                print("Error: Usage: update <id>")
                continue
            
            task_id = parts[0]
            task = task_service.get_task_by_id(task_id) # Get existing task to show current values
            if not task:
                print(f"Error: Task with ID '{task_id}' not found.")
                continue

            print(f"Updating task (ID: {task.id}): '{task.title}'")
            print(f"Current Description: '{task.description if task.description else '(none)'}'")

            new_title_input = input(f"Enter new title (current: '{task.title}', leave empty to keep): ").strip()
            new_description_input = input(f"Enter new description (current: '{task.description if task.description else '(none)'}', leave empty to keep/clear): ").strip()

            title_to_set = task.title
            if new_title_input: # If user typed something for title, use it
                title_to_set = new_title_input

            description_to_set = task.description
            if new_description_input: # If user typed something for description, use it
                description_to_set = new_description_input
            elif new_description_input == "": # If user explicitly entered empty string, clear description
                description_to_set = None

            updated_task = task_service.update_task(
                task_id,
                title=title_to_set,
                description=description_to_set
            )

            if updated_task:
                print(f"Updated task: {updated_task.title} (ID: {updated_task.id})")
            else:
                # This case should ideally not be reached if task was found earlier
                print(f"Error: Failed to update task with ID '{task_id}'.")
        elif action == "toggle":
            parts = args.split(maxsplit=1)
            if not parts:
                print("Error: Usage: toggle <id>")
                continue
            task_id = parts[0]
            task = task_service.toggle_task_completion(task_id)
            if task:
                status = "completed" if task.completed else "incomplete"
                print(f"Task '{task.title}' marked as {status}.")
            else:
                print(f"Error: Task with ID '{task_id}' not found.")
        elif action == "delete":
            parts = args.split(maxsplit=1)
            if not parts:
                print("Error: Usage: delete <id>")
                continue
            task_id = parts[0]
            if task_service.delete_task(task_id):
                print(f"Task with ID '{task_id}' deleted.")
            else:
                print(f"Error: Task with ID '{task_id}' not found.")
        else:
            print(f"Unknown command: '{action}'. Type 'help' for commands.")

if __name__ == "__main__":
    main()
