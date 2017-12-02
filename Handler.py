
from watchdog.events import FileSystemEventHandler
class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        if (evnt.src_path in trackedFiles)
            changedFile = TrackedFile.load_file(event.src_path)
            changedFile.update()



    def on_created(self, event):
        pass
