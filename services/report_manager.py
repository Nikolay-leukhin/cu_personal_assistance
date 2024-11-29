from models import FinanceRecord
from copy import deepcopy
from .file_manager import FileManager


class RecordManager:
    def __init__(self, file_path):
        self.file = FileManager()
        self.__file_path = file_path
        self.__record_list: list[FinanceRecord] = self.load_data()

    def add_record(self, record):
        new_id = max([item.id for item in self.__record_list]) + 1 if self.__record_list.__len__() != 0 else 0
        record.id = new_id
        self.__record_list.append(record)
        self.save_data()

    def get_records(self, filter_by_category=None, filter_by_date=None):
        filtered = deepcopy(self.__record_list)

        if filter_by_category is not None:
            filtered = [
                item for item in filtered
                if item.category == filter_by_category
            ]

        if filter_by_date is not None:
            filtered = [
                item for item in filtered
                if item.date == filter_by_date
            ]

        return filtered

    def form_report(self, start, end):
        filtered_by_date = [
            item for item in self.__record_list
            if start <= item.date <= end
        ]

        return filtered_by_date

    def total_balance(self):
        total = sum([
            item.amount for item in self.__record_list
        ])
        return total

    def group_by_category(self):
        categories = list({
            item.category for item in self.__record_list
        })

        data = {}

        for category in categories:
            data_by_category = [
                item for item in self.__record_list
                if item.category == category
            ]
            data[category] = data_by_category

        return data

    def save_data(self):
        raw_tasks = [item.to_json() for item in self.__record_list]
        self.file.save_to_json(raw_tasks, self.__file_path)

    def load_data(self):
        raw_data = self.file.load_from_json(self.__file_path)
        return [FinanceRecord.from_json(json_item) for json_item in raw_data]

