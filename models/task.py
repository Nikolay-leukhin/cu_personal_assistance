class Task:
    def __init__(self, id, title, description=None, priority=None, due_date=None, done=False):
        self.id = id
        self.title = title
        self.description = description
        self.done = done
        self.priority = priority
        self.due_date = due_date

    def __repr__(self):
        return (f"Task(id={self.id}, title='{self.title}', description='{self.description}', "
                f"done={self.done}, priority='{self.priority}', due_date='{self.due_date}')")
