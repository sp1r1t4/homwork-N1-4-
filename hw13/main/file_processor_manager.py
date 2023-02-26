import os
class FileProcessorManager:
    def __init__(self, directory_path, file_processors):
        self.directory_path = directory_path
        self.file_processors = file_processors

    def process_files(self):
        for file_name in os.listdir(self.directory_path):
            file_path = os.path.join(self.directory_path, file_name)
            for file_processor in self.file_processors:
                if file_processor.can_process(file_path):
                    data_entry = file_processor.read_file(file_path)
                    file_processor.save_file(data_entry, file_path)


