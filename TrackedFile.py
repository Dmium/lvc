import pickle
import json

class TrackedFile():
    def __init__(self, file_path):
        self.file_path = file_path
        self.commits = []
        self.current_content = ""

    # read and return the contents of the file
    def read_new(self):
        new_content = self.current_content
        with open(self.file_path, 'r') as f:
            new_content = f.read()
        return new_content

    # read the contents of the file and store them in self.current_content
    def read_new_into_current(self):
        self.current_content = read_new()

    # saves a TrackedFile class to a binary file, and return the dot_file_path
    def save_file(self):
        dot_file_path = get_dot_file_path(self.file_path)
        with open(dot_file_path, 'wb') as f:
            dumped = pickle.dump(self, f)
            return dot_file_path

    # takes the path of the file whose TrackedFile class should be loaded
    def load_file(file_path):
        dot_file_path = get_dot_file_path(file_path)
        with open(dot_file_path, 'rb') as f:
            loaded_file = pickle.load(f)
            return loaded_file
        return None

    # returns a json object containing the content of each commit stored in commits
    def get_json(self):
        commit_data = []
        for commit in self.commits:
            # TODO: add timestamp to returned data
            content = "debug content for commit ID %s" % str(commit.id)
            # content = Diffing.get_version(""" some magic bullshit """, commit.id)
            commit_data.append({'content': content})
        commit_json = json.dumps(commit_data)
        return commit_json


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
