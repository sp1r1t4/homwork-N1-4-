import csv
import json

class DataEntry:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return str(self.data)

class FileProcessor:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        raise NotImplementedError

    def save_file(self, data_entry):
        raise NotImplementedError

class JSONFileProcessor(FileProcessor):
    def read_file(self):
        with open(self.file_path, 'r') as file:
            data = json.load(file)
        return DataEntry(data)

    def save_file(self, data_entry):
        with open(self.file_path, 'w') as file:
            json.dump(data_entry.data, file)

class CSVFileProcessor(FileProcessor):
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

class FileProcessorManager:
    def __init__(self, file_processors):
        self.file_processors = file_processors

    def process_files(self):
        for file_processor in self.file_processors:
            data_entry = file_processor.read_file()
            file_processor.save_file(data_entry)

# Пример использования классов
if __name__ == '__main__':
    # Создание объектов классов для чтения и записи файлов
    json_file_processor = JSONFileProcessor('file.json')
    csv_file_processor = CSVFileProcessor('file.csv')

    # Создание объекта класса FileProcessorManager, который будет обрабатывать файлы
    file_processor_manager = FileProcessorManager([json_file_processor, csv_file_processor])

    # Обработка файлов
    file_processor_manager.process_files()


