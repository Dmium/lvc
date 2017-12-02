from difflib import Differ
from difflib import restore
class Diffing():
    # Note: Delta is reversed so we work backwards
    def get_delta(current_file, new_file):
        current_file = current_file.splitlines(keepends=True)
        new_file = new_file.splitlines(keepends=True)
        return list(Differ().compare(current_file, new_file))

    def get_version(delta):
        return ''.join(restore(delta, 2))
