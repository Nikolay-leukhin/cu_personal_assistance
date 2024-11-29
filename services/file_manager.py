import csv
import json
import os


class FileManager:
    @staticmethod
    def import_from_csv(abs_path: str):
        try:
            if not os.path.exists(abs_path) or os.stat(abs_path).st_size == 0:
                with open(abs_path, 'w', encoding='utf-8'):
                    return []

            with open(abs_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                return [item for item in reader]

        except Exception as ex:
            print(ex)
            return []

    @staticmethod
    def export_to_csv(data, filename: str):
        data = [item.to_json() for item in data]
        try:
            with open(filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(data[0].keys())
                for item in data:
                    writer.writerow(item.values())
        except Exception as ex:
            print("Failure to export data in csv")
            print(f'Cause: {ex}')

    @staticmethod
    def load_from_json(abs_path: str):
        try:
            if not os.path.exists(abs_path) or os.stat(abs_path).st_size == 0:
                with open(abs_path, 'w', encoding='utf-8'):
                    return []
            with open(abs_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return data
        except Exception as ex:
            print("Failure while loading data from json")
            print(f"Casuse: {ex}")

    @staticmethod
    def save_to_json(data, out_filename: str):
        try:
            with open(out_filename, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
        except Exception as ex:
            print(f"Erorr while saving the {out_filename}")
            print(ex)


