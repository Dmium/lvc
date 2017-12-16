import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler
from Handler import Handler
import os.path
import json
from webapp import Server

path_lists = []
if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = Handler()
    event_handler.load_handler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    if(len(sys.argv) < 4):
        print("Please specify a host and port")
        exit()
    try:
        Server.start(sys.argv[len(sys.argv) - 2], sys.argv[len(sys.argv) - 1])
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
