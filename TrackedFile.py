
import pickle
import json
from Commit import Commit
import time
import os

class TrackedFile():
    def __init__(self, file_path):
        self.file_path = file_path
        self.commits = []

    # read and return the contents of the file
    def read_new(self):
        with open(self.file_path, 'r') as f:
            new_content = f.read()
        return new_content

    # saves a TrackedFile class to a binary file, and return the dot_file_path
    def save_file(self):
        dot_file_path = get_dot_file_path(self.file_path)
        with open(dot_file_path, 'wb') as f:
            dumped = pickle.dump(self, f)
            return dot_file_path

    # takes the path of the file whose TrackedFile class should be loaded
    def load_file(file_path):
        dot_file_path = get_dot_file_path(file_path)
        if os.path.isfile(dot_file_path):
            with open(dot_file_path, 'rb') as f:
                loaded_file = pickle.load(f)
                return loaded_file
        return None

    def get_num_commits(self):
        return len(self.commits)

    def get_commit(self, index):
        return self.commits[index]
    
    # returns a json object containing the content of each commit stored in commits
    def get_json(self):
        commit_data = []
        for commit in self.commits:
            content = commit.get_version()
            commit_data.append({'timestamp': commit.datetime, 'content': content})
        commit_json = json.dumps(commit_data)
        return commit_json

    # create and store a new commit and save file to binary
    def update(self):
        if (len(self.commits) == 0):
            self.commits.append(Commit(time.time(), None, self.read_new()))
        else:
            self.commits.append(Commit(time.time(), self.commits[-1], self.read_new()))
        self.save_file()


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

def is_dot_file_path(file_path):
    # I am still so, so sorry
    last_fslash_index = file_path.rfind("/")
    last_bslash_index = file_path.rfind("\\")
    if last_fslash_index != -1:
        if file_path[last_fslash_index + 1] == ".":
            return True
    elif last_bslash_index != -1:
        if file_path[last_bslash_index + 1] == ".":
            return True
    else:
        if file_path[0] == ".":
            return True
    return False
