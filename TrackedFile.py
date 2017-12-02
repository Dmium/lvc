class TrackedFile():
    def __init__(self, file_name):
        self.file_name = file_name
        self.commits = []
        self.current_content = ""

    def read_new():
        new_content = current_file
        with open(file_name, 'r') as f:
            new_content = f.read()
        return new_content

    def read_new_into_current():
        current_content = read_new()
