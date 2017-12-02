from FileManager import FileManager
from watchdog.events import FileSystemEventHandler
from TrackedFile import TrackedFile
class Handler(FileSystemEventHandler):
    def load_handler(self):
        self.file_manager = FileManager()

    def on_modified(self, event):
        print("Modded")
        if (self.file_manager.check(event.src_path)):
            changedFile = TrackedFile.load_file(event.src_path)
            if changedFile is None:
                changedFile = TrackedFile(event.src_path)
            changedFile.update()


    def on_created(self, event):
        print("Created:")
        if not self.file_manager.check(event.src_path):
            self.file_manager.track(event.src_path)
