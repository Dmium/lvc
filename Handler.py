
from watchdog.events import FileSystemEventHandler
class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        diff.fileopen.(event.src_path)

    def on_created(self, event):
        pass
