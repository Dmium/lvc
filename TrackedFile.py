import pickle

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

    def SaveFile(self):
        file_name = ""
        last_fslash_index = self.file_name.rfind("/")
        last_bslash_index = self.file_name.rfind("\\")
        if last_fslash_index != -1:
            file_name = self.file_name[:last_fslash_index] + "." +\
             self.file_name[last_fslash_index:]
        elif last_bslash_index != -1:
            file_name = self.file_name[:last_bslash_index] + "." +\
             self.file_name[last_bslash_index:]
        else:
            file_name = "." + self.file_name

        with open(file_name, 'wb') as f:
            dumped = pickle.dump(self, f)
            return file_name

    def LoadFile(file_name):
        with open(file_name, 'rb') as f:
            loaded_file = pickle.load(f)
            return loaded_file
        return None
