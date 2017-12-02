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



    # saves a TrackedFile class to a binary file, and return the dot_file_path
    def SaveFile(self):
        file_path = get_dot_file_path(self.file_name)
        with open(file_path, 'wb') as f:
            dumped = pickle.dump(self, f)
            return file_path

    # takes the path of the file whose TrackedFile class should be loaded
    def LoadFile(file_path):
        dot_file_path = get_dot_file_path(file_path)
        with open(dot_file_path, 'rb') as f:
            loaded_file = pickle.load(f)
            return loaded_file
        return None


# converts a file path to its corresponding dot file path, eg C:\example\foo.txt to C:\example\.foo.txt
def get_dot_file_path(file_path):
    # I am so, so sorry
    file_name = file_path
    last_fslash_index = file_path.rfind("/")
    last_bslash_index = file_path.rfind("\\")
    if last_fslash_index != -1:
        file_name = file_path[:last_fslash_index+1] + "." +\
         file_path[last_fslash_index+1:]
    elif last_bslash_index != -1:
        file_name = file_path[:last_bslash_index+1] + "." +\
         file_path[last_bslash_index+1:]
    else:
        file_name = "." + file_path
    return file_name
