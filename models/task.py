import json


class Task:
    def __init__(self, title, id=None, description=None, priority=None, due_date=None, done=False):
        self.id = id
        self.title = title
        self.description = description
        self.done = done
        self.priority = priority
        self.due_date = due_date

    def __repr__(self):
        return (f"Task(id={self.id}, title='{self.title}', description='{self.description}', "
                f"done={self.done}, priority='{self.priority}', due_date='{self.due_date}')")

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'done': self.done,
            'priority': self.priority,
            'due_date': self.due_date
        }

    @classmethod
    def from_json(cls, json_str):
        return Task(**json_str )


