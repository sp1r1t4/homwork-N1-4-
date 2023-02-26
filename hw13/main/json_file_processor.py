import json
from hw13.main.data_entry import DataEntry
from hw13.main.file_processor import FileProcessor

class JSONFileProcessor(FileProcessor):
    def can_process(self, file_path):
        return file_path.endswith('.json')
    def read_file(self):
        with open(self.file_path, 'r') as file:
            data = json.load(file)
        return DataEntry(data)

    def save_file(self, data_entry):
        with open(self.file_path, 'w') as file:
            json.dump(data_entry.data, file)