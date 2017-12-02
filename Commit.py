from Diffing import Diffing
class Commit():
    def __init__(self, id, datetime, last_commit, current_file):
        self.id = id
        self.datetime = datetime
        self.line_delta = Diffing.get_delta(Diffing.get_version(last_commit.line_delta), current_file)

    def get_version(self):
        return Diffing.get_version(self.line_delta)
