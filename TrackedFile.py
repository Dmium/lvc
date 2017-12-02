class TrackedFile():
    def __init__(self, file_name):
        self.file_name = file_name
        self.commits = []
        self.current_content = ""
        read_new_into_current()

    def read_new_into_current():
        new_content = current_file
        with open(file_name, 'r') as f:
            new_content = f.read()
