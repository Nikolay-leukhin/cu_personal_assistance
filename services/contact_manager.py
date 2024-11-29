from models import Contact
from .file_manager import FileManager


class ContactManager:
    def __init__(self, file_path):
        self.file = FileManager()
        self.__file_path = file_path
        self.__contacts_list: list[Contact] = self.load_data()

    def add_contact(self, contact):
        new_id = max([item.id for item in self.__contacts_list]) + 1 if self.__contacts_list.__len__() != 0 else 0
        contact.id = new_id
        self.__contacts_list.append(contact)
        self.save_data()

    def find_by_name(self, name):
        contact = next((item for item in self.__contacts_list if item.name == name), None)
        if contact is None:
            raise Exception(f'Contact with name {name} not found')
        return contact

    def find_by_phone(self, phone):
        contact = next((item for item in self.__contacts_list if item.phone == phone), None)
        if contact is None:
            raise Exception(f'Contact with phone {phone} not found')
        return contact

    def find_by_id(self, contact_id):
        contact = next((item for item in self.__contacts_list if item.id == id), None)
        if contact is None:
            raise Exception(f'Contact with contact_id {contact_id} not found')
        return contact

    def edit_contact(self, contact_id, name=None, phone=None, email=None):
        contact = self.find_by_id(contact_id)

        contact.name = name if name is not None else contact.name
        contact.phone = phone if phone is not None else contact.phone
        contact.email = email if email is not None else contact.email

        self.save_data()

    def delete_contact(self, contact_id):
        self.__contacts_list = list(filter(lambda cn: cn.id != contact_id, self.__contacts_list))
        self.save_data()

    def save_data(self):
        raw_tasks = [item.to_json() for item in self.__contacts_list]
        self.file.save_to_json(raw_tasks, self.__file_path)

    def import_from_csv(self, abs_path):
        return [Contact.from_json(item) for item in self.file.import_from_csv(abs_path)]

    def export_to_csv(self, data, abs_path):
        return self.file.export_to_csv(data, abs_path)

    def load_data(self):
        raw_data = self.file.load_from_json(self.__file_path)
        return [Contact.from_json(json_item) for json_item in raw_data]

