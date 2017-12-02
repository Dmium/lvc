import os
import json
class FileManager():
    def __init__(self):
        self.path_lists = []
        self.load()

    def load(self):
        if os.path.isfile(".file_list"):# messy should clean
            with open(".file_list", 'rb') as f:
                self.path_lists = json.load(f)
        else:
            with open(".file_list", 'wb') as f:
                json.dump(self.path_lists, f)

    def track(self, path):
        self.path_lists.append(path)
        if os.path.isfile(".file_list"):
            with open(".file_list", 'wb') as f:
                json.dump(self.path_lists, f)

    def check(self, path):
        return (path in self.path_lists)
