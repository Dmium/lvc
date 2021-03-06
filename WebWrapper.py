from FileManager import FileManager
from TrackedFile import TrackedFile
import json

class WebWrapper():
    def __init__(self):
        pass

    # returns a json object containing the each tracked path, with the most recent modification date
    def get_paths_list_json(self):
        # each path, with most recent modification
        file_manager = FileManager()
        paths = file_manager.path_lists
        pairs = {}
        for path in paths:
            tracked_file = TrackedFile.load_file(path)
            pairs[path] = tracked_file.commits[-1].datetime
        return json.dumps(pairs)

    def get_paths_list(self):
        file_manager = FileManager()
        paths = file_manager.path_lists
        pairs = {}
        for path in paths:
            tracked_file = TrackedFile.load_file(path)
            pairs[path] = tracked_file.commits[-1].datetime
        return pairs

    # returns a json object containing the content of each commit stored in commits for a given file
    def get_commits_for_path(self, path):
        file_manager = FileManager()
        print(file_manager.path_lists)
        if file_manager.check(path):
            json_data = TrackedFile.load_file(path).get_json()
            return json_data
        return json.dumps([])

    def get_number_commits_for_path(self, path):
        file_manager = FileManager()
        if file_manager.check(path):
            result = TrackedFile.load_file(path).get_num_commits()
            return result
        return 0

    def get_commit_for_index(self, index, path):
        file_manager = FileManager()
        if file_manager.check(path) and index < self.get_number_commits_for_path(path):
            return TrackedFile.load_file(path).get_commit(index).get_version()
        return ""
