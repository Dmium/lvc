from FileManager import FileManager
from watchdog.events import FileSystemEventHandler
class Handler(FileSystemEventHandler):
    def __init__(self):
        super.__init__(self)
        self.file_manager = FileManager()
    def on_modified(self, event):
        print(event.src_path)

    def on_created(self, event):
        pass

    def diff(self, path):
        pass
