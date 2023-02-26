class FileProcessor:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        raise NotImplementedError

    def save_file(self, data_entry):
        raise NotImplementedError
