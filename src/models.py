import uuid

class Task:
    def __init__(self, title: str, description: str = None, completed: bool = False):
        self.id = uuid.uuid4().hex
        self.title = title
        self.description = description
        self.completed = completed

    def __repr__(self):
        status = "✓" if self.completed else " "
        desc = f" ({self.description})" if self.description else ""
        return f"[{status}] {self.title}{desc} (ID: {self.id})"

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
        }
