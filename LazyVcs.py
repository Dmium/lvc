import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler


class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        print(event.src_path)

    def on_created(self, event):
        pass

    def diff(self, path):
        pass

class Change():
    def __init__(self, id):
        self.id = id

class Line_Change(Change):
    def __init__(self, add, lineno, line):
        self.add = add
        self.lineno = lineno
        self.line = line


class Dir_Change(Change):
    def __init__(self, id, effect, path):
        super.__init__(id)
        self.effect = effect
        self.path = path


class Commit():
    def __init__(self, id):
        self.id = id
        self.line_changes = []
        self.dir_changes = []


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = Handler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
