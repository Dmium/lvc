class Handler(FileSystemEventHandler):
    def on_modified(self, event):
        print(event.src_path)

    def on_created(self, event):
        pass

    def diff(self, path):
        pass
