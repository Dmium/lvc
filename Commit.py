from Diffing import Diffing
class Commit():
    def __init__(self, datetime, last_commit, new_file):
        self.datetime = datetime
        if last_commit is None:
            self.line_delta = Diffing.get_delta('', new_file)
        else:
            self.line_delta = Diffing.get_delta(Diffing.get_version(last_commit.line_delta), new_file)

    def get_version(self):
        return Diffing.get_version(self.line_delta)
