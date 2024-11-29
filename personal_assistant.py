from lexicon import Lexicon as lx
from services import TaskManager, NoteManager, ContactManager, RecordManager
from models import Task, Note, Contact, FinanceRecord
from calculator import Calculator
import os

tasks = [
    Task(title="Buy groceries", description="Milk, Bread, Eggs", priority="High", due_date="01-10-2023 14:30:00", done=False),
    Task(title="Finish project report", description="Complete the final report for the project", priority="Medium", due_date="02-10-2023 09:00:00", done=False),
    Task(title="Call the doctor", description="Schedule an appointment for a check-up", priority="Low", due_date="03-10-2023 11:15:00", done=False),
    Task(title="Attend meeting", description="Weekly team meeting", priority="High", due_date="04-10-2023 10:00:00", done=False),
]


def main():
    path_to_tasks = os.getcwd() + '/assets/tasks.json'
    path_to_notes = os.getcwd() + '/assets/notes.json'
    path_to_contacts = os.getcwd() + '/assets/contacts.json'
    path_to_records = os.getcwd() + '/assets/records.json'

    task_manager = TaskManager(path_to_tasks)
    note_manager = NoteManager(path_to_notes)
    contact_manager = ContactManager(path_to_contacts)
    records_manager = RecordManager(path_to_records)

    calc = Calculator()

    while True:
        act = int(input(lx.choose_action))

        match act:
            case 1:
                note_action = int(input(lx.choose_note_action))
                match note_action:
                    case 1:
                        title = input(lx.enter_note_title)
                        content = input(lx.enter_note_content)
                        timestamp = input(lx.enter_note_timestamp)
                        note_manager.add_note(Note(title, content, timestamp))
                        print(lx.add_note_success)
                    case 2:
                        note_id = int(input(lx.enter_note_id))
                        title = input(lx.enter_note_edit_title)
                        content = input(lx.enter_note_edit_content)
                        note_manager.edit_note(note_id, title, content)
                        print(lx.edit_note_success)
                    case 3:
                        note_id = int(input(lx.enter_note_id_delete))
                        note_manager.delete_note(note_id)
                        print(lx.delete_note_success)
                    case 4:
                        notes = note_manager.get_notes()
                        for note in notes:
                            print(note)

            case 2:
                task_action = int(input(lx.choose_task_action))
                match task_action:
                    case 1:
                        title = input(lx.enter_task_title)
                        description = input(lx.enter_task_description)
                        priority = input(lx.choose_task_priority)
                        due_date = input(lx.enter_task_due_date)
                        task_manager.add_task(Task(title, description, priority, due_date))
                        print(lx.add_task_success)
                    case 2:
                        task_id = int(input(lx.enter_task_id))
                        task_manager.mark_as_completed(task_id)
                        print(lx.mark_task_completed)
                    case 3:
                        task_list = task_manager.get_tasks()
                        for task in task_list:
                            print(task)
                    case 4:
                        task_id = int(input(lx.enter_task_id_edit))
                        title = input(lx.enter_task_title)
                        description = input(lx.enter_task_description)
                        priority = input(lx.choose_task_priority)
                        due_date = input(lx.enter_task_due_date)
                        task_manager.edit_task(task_id, title, description, priority, due_date)
                        print(lx.edit_task_success)
                    case 5:
                        task_id = int(input(lx.enter_task_id_delete))
                        task_manager.delete_task(task_id)
                        print(lx.delete_task_success)
            case 3:
                contact_action = int(input(lx.choose_contact_action))
                match contact_action:
                    case 1:
                        name = input(lx.enter_contact_name)
                        phone = input(lx.enter_contact_phone)
                        email = input(lx.enter_contact_email)
                        contact_manager.add_contact(Contact(name, phone, email))
                        print(lx.add_contact_success)
                    case 2:
                        contact_id = int(input(lx.enter_contact_id))
                        name = input(lx.enter_contact_name)
                        phone = input(lx.enter_contact_phone)
                        email = input(lx.enter_contact_email)
                        contact_manager.edit_contact(contact_id, name, phone, email)
                        print(lx.edit_contact_success)
                    case 3:
                        contact_id = int(input(lx.enter_contact_id_delete))
                        contact_manager.delete_contact(contact_id)
                        print(lx.delete_contact_success)
                    case 4:
                        name = input(lx.enter_contact_name)
                        print(contact_manager.find_by_name(name))
                    case 5:
                        phone = input(lx.enter_contact_phone)
                        print(contact_manager.find_by_phone(phone))
            case 4:
                finance_action = int(input(lx.choose_record_action))
                match finance_action:
                    case 1:
                        amount = int(input(lx.enter_record_amount))
                        category = input(lx.enter_record_category)
                        date = input(lx.enter_record_date)
                        description = input(lx.enter_record_description)
                        records_manager.add_record(FinanceRecord(
                            amount=amount,
                            category=category,
                            date=date,
                            description=description
                        ))
                        print(lx.add_record_success)
                    case 2:
                        for item in records_manager.get_records():
                            print(item)
                    case 3:
                        print(lx.enter_record_filter_date)
                        start = input(lx.enter_report_start_date)
                        end = input(lx.enter_report_end_date)
                        records_manager.form_report(start, end)
            case 5:
                operation = int(input(lx.calc_enter_operation))
                if operation not in [1, 2, 3, 4]:
                    raise ValueError(lx.incorrect_command)
                a = float(input(lx.calc_enter_first_arg))
                b = float(input(lx.calc_enter_second_arg))

                match operation:
                    case 1:
                        print(calc.plus(a, b))
                    case 2:
                        print(calc.minus(a, b))
                    case 3:
                        print(calc.mult(a, b))
                    case 4:
                        print(calc.div(a, b))
            case 6:
                break
            case _:
                print(lx.no_such_action)


if __name__ == '__main__':
    main()
