# class LineElement():
#     def __init__(self, line_numbers):

# class LineDictionary(Dictionary):
class LineDictionary():
    def __init__(self):
        self.dict = {}

    def add_line(self, line):
        if line in self.dict:
            self.dict[line].append(line_number)
        else:
            self.dict[line] = []
