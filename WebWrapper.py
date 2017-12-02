from FileManager import FileManager
from TrackedFile import TrackedFile
import json

class WebWrapper():
    def __init__(self):
        pass

    # returns a json object containing the each tracked path, with the most recent modification date
    def get_paths_list(self):
        # each path, with most recent modification
        file_manager = FileManager()
        paths = file_manager.path_lists
        pairs = []
        for path in paths:
            tracked_file = TrackedFile.load_file(path)
            pairs.append({path: tracked_file.commits[-1].datetime})
        return json.dumps(pairs)
