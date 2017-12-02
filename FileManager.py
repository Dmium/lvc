import os
import json
class FileManager():
    def __init__(self):
        self.path_lists = []
        self.load()

    def load(self):
        if os.path.isfile(".file_list"):# messy should clean
            with open(".file_list", 'r') as f:
                try:
                    self.path_lists = json.load(f)
                except:
                    pass

    def track(self, path):
        self.path_lists.append(path)
        with open(".file_list", 'w') as f:
            json.dump(self.path_lists, f)

    def check(self, path):
        return (path in self.path_lists)
