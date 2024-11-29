from models import Note
from .file_manager import FileManager


class NoteManager:
    def __init__(self, file_path):
        self.file = FileManager()
        self.__file_path = file_path
        self.__note_list: list[Note] = self.load_data()

    def add_note(self, note: Note):
        ...

    def get_notes(self):
        ...

    def get_note_details(self):
        ...

    def edit_note(self):
        ...

    def delete_note(self):
        ...

    def load_data(self):
        raw_data = self.file.load_from_json(self.__file_path)
        return [Note.from_json(json_item) for json_item in raw_data]


