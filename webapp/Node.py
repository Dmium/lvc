import datetime

class Node:
    url = ""
    name = ""
    timestamp = 0

    def __init__(self, url, name, timestamp):
        self.url = url
        self.name = name
        self.timestamp = timestamp

    def get_date(self):
        return datetime.datetime.fromtimestamp(self.timestamp).strftime('%Y-%m-%d %H:%M:%S')
