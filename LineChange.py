class LineChange(Change):
    def __init__(self, add, lineno, line):
        self.add = add
        self.lineno = lineno
        self.line = line
