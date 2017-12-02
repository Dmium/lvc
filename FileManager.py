class FileManager():
    def __init__(self):
        self.path_lists = []
        load()

    def load(self):
        if not os.path.isfile(".file_list"):# messy should clean
            with open(".file_list", 'wb') as f:
                json.dumps(self.path_lists, f)
        else:
            with open(".file_list", 'rb') as f:
                self.path_lists = json.load(f)

    def track(self, path):
        self.path_lists.append(path)
        with open(".file_list", 'wb') as f:
            json.dump(self.path_lists, f)
