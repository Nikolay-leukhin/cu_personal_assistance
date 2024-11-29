from models import Task
from .file_manager import FileManager
from copy import deepcopy


class TaskManager:
    def __init__(self, file_path: str):
        self.file = FileManager()
        self.__file_path = file_path
        self.__task_list: list[Task] = self.load_data()

    def add_task(self, task: Task):
        new_id = max([item.id for item in self.__task_list]) + 1 if self.__task_list.__len__() != 0 else 0
        task.id = new_id
        self.__task_list.append(task)
        self.save_data()

    def get_tasks(self, priority: str = None, done: bool = None , due: str = None):
        filtered = deepcopy(self.__task_list)
        if priority is not None:
            filtered = [
                item for item in filtered
                if item.priority == priority
            ]
        if done is not None:
            filtered = [
                item for item in filtered
                if item.done == done
            ]

        if due is not None:
            filtered = [
                item for item in filtered
                if item.due_date == due
            ]

        for item in filtered:
            print(item)

        return filtered

    def mark_as_completed(self, task_id):
        task = self.find_task(task_id)
        task.done = True

        self.save_data()

    def edit_task(self, task_id, title=None, description=None, done=None, priority=None, due_data=None):
        task = self.find_task(task_id)

        task.title = title if title is not None else task.title
        task.description = description if description is not None else task.description
        task.done = done if done is not None else task.done
        task.priority = priority if priority is not None else task.priority
        task.due_data = due_data if due_data is not None else task.due_data

        self.save_data()

    def delete_task(self, task_id):
        filtered_tasks = list(filter(lambda t: t.id != task_id, self.__task_list))
        self.__task_list = filtered_tasks
        self.save_data()

    def find_task(self, task_id):
        task = next((item for item in self.__task_list if item.id == task_id), None)
        if task is None:
            raise Exception("No such task in task list")
        return task

    def save_data(self):
        raw_tasks = [item.to_json() for item in self.__task_list]
        self.file.save_to_json(raw_tasks, self.__file_path)

    def import_from_csv(self, abs_path):
        return self.file.import_from_csv(abs_path)

    def export_to_csv(self, data, abs_path):
        return self.file.export_to_csv(data, abs_path)

    def load_data(self):
        raw_data = self.file.load_from_json(self.__file_path)
        return [Task.from_json(json_item) for json_item in raw_data]
