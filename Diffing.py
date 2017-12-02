import difflib
class Diffing():
    def getDelta(current_file, new_file):
        current_file = current_file.splitlines(keepends=True)
        new_file = new_file.splitlines(keepends=True)
        return list(Differ().compare(current_file, new_file)

    def reverseDelta(current_file, delta):
        pass
