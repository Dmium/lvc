from FileManager import FileManager
from watchdog.events import FileSystemEventHandler
from TrackedFile import TrackedFile
from TrackedFile import is_dot_file_path

class Handler(FileSystemEventHandler):
    def load_handler(self):
        self.file_manager = FileManager()

    def on_modified(self, event):
        if (not is_dot_file_path(event.src_path) and self.file_manager.check(event.src_path)):
            print("Modded")
            changedFile = TrackedFile.load_file(event.src_path)
            if changedFile is None:
                changedFile = TrackedFile(event.src_path)
            changedFile.update()


    def on_created(self, event):
        print("Created:")
        if not is_dot_file_path(event.src_path) and not self.file_manager.check(event.src_path):
            self.file_manager.track(event.src_path)
