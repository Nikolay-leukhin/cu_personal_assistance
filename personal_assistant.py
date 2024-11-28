from lexicon import Lexicon as lx
from services import TaskManager
from models import Task
import os

tasks = [
    Task(title="Buy groceries", description="Milk, Bread, Eggs", priority="High", due_date="01-10-2023 14:30:00", done=False),
    Task(title="Finish project report", description="Complete the final report for the project", priority="Medium", due_date="02-10-2023 09:00:00", done=False),
    Task(title="Call the doctor", description="Schedule an appointment for a check-up", priority="Low", due_date="03-10-2023 11:15:00", done=False),
    Task(title="Attend meeting", description="Weekly team meeting", priority="High", due_date="04-10-2023 10:00:00", done=False),
]



def main():
    path_to_tasks = os.getcwd() + '/assets/tasks.json'
    task_manager = TaskManager(path_to_tasks)
    task_manager.add_task(tasks[0])


    # print(lx.welcome)
    # while True:
    #     act = int(input('lx.choose_act'))
    #
    #     match act:
    #         case 1:
    #             ...
    #         case 2:
    #             ...
    #         case 3:
    #             ...
    #         case 4:
    #             ...
    #         case 5:
    #             ...
    #         case 6:
    #             break
    #         case _:
    #             print(lx.no_such_action)


if __name__ == '__main__':
    main()