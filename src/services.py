from src.models import Task

class TaskService:
    def __init__(self):
        self.tasks = {} # Stores Task objects, keyed by ID

    def add_task(self, title: str, description: str = None) -> Task:
        task = Task(title, description)
        self.tasks[task.id] = task
        return task

    def get_all_tasks(self) -> list[Task]:
        return list(self.tasks.values())

    def get_task_by_id(self, task_id: str) -> Task | None:
        return self.tasks.get(task_id)

    def update_task(self, task_id: str, title: str = None, description: str = None) -> Task | None:
        task = self.get_task_by_id(task_id)
        if task:
            if title is not None:
                task.title = title
            if description is not None:
                task.description = description
        return task

    def toggle_task_completion(self, task_id: str) -> Task | None:
        task = self.get_task_by_id(task_id)
        if task:
            task.completed = not task.completed
        return task

    def delete_task(self, task_id: str) -> bool:
        if task_id in self.tasks:
            del self.tasks[task_id]
            return True
        return False
