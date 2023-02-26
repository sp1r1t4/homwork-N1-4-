import csv
from hw13.main.data_entry import DataEntry
from hw13.main.file_processor import FileProcessor

class CSVFileProcessor(FileProcessor):
    def can_process(self, file_path):
        return file_path.endswith('.csv')
    def read_file(self):
        with open(self.file_path, 'r') as file:
            reader = csv.reader(file)
            data = []
            for row in reader:
                data.append(row)
        return DataEntry(data)

    def save_file(self, data_entry):
        with open(self.file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data_entry.data)
