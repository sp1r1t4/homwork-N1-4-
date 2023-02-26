from hw13.main.json_file_processor import JSONFileProcessor
from hw13.main.csv_file_processor import CSVFileProcessor
from hw13.main.file_processor_manager import FileProcessorManager

# Создание объектов классов для чтения и записи файлов
json_file_processor = JSONFileProcessor('file.json')
csv_file_processor = CSVFileProcessor('file.csv')

# Создание объекта класса FileProcessorManager, который будет обрабатывать файлы
file_processor_manager = FileProcessorManager([json_file_processor, csv_file_processor])

# Обработка файлов
file_processor_manager.process_files()