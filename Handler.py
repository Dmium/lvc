from FileManager import FileManager
from watchdog.events import FileSystemEventHandler
class Handler(FileSystemEventHandler):
    def __init__(self):
        super.__init__(self)
        self.file_manager = FileManager()
    def on_modified(self, event):
        with open(".file_list","r") as f:
            contents = f.read()
            pathlist = json.loads(contents)
        if (event.src_path in pathlist):
            changedFile = TrackedFile.load_file(event.src_path)
            changedFile.update()



    def on_created(self, event):
        pass
