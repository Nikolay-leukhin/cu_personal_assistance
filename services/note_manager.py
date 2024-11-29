from models import Note
from .file_manager import FileManager


class NoteManager:
    def __init__(self, file_path):
        self.file = FileManager()
        self.__file_path = file_path
        self.__note_list: list[Note] = self.load_data()

    def add_note(self, note: Note):
        new_id = max([item.id for item in self.__note_list]) + 1 if self.__note_list.__len__() != 0 else 0
        note.id = new_id
        self.__note_list.append(note)
        self.save_data()

    def get_notes(self):
        return self.__note_list

    def get_note_details(self, note_id):
        note = self.find_note(note_id)
        print(note)
        return note

    def edit_note(self, note_id, title=None, content=None, timestamp=None):
        note = self.find_note(note_id)

        note.title = title if title is not None else note.title
        note.content = content if content is not None else note.content
        note.timestamp = timestamp if timestamp is not None else note.timestamp

        self.save_data()

    def delete_note(self, note_id):
        self.__note_list = list(filter(lambda note: note.id != note_id, self.__note_list))
        self.save_data()

    def find_note(self, note_id):
        note = next((item for item in self.__note_list if item.id == note_id), None)
        if note is None:
            raise Exception("No such note in note list")
        return note

    def save_data(self):
        raw_tasks = [item.to_json() for item in self.__note_list]
        self.file.save_to_json(raw_tasks, self.__file_path)

    def import_from_csv(self, abs_path):
        return [Note.from_json(item) for item in self.file.import_from_csv(abs_path)]

    def export_to_csv(self, data, abs_path):
        return self.file.export_to_csv(data, abs_path)

    def load_data(self):
        raw_data = self.file.load_from_json(self.__file_path)
        return [Note.from_json(json_item) for json_item in raw_data]


