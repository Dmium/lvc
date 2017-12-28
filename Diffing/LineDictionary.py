# class LineElement():
#     def __init__(self, line_numbers):

# class LineDictionary(Dictionary):
class LineDictionary():
    def __init__(self):
        self.dict = {}

    def add_line(self, line, line_number):
        if line in self.dict:
            self.dict[line].append(line_number)
        else:
            self.dict[line] = [line_number]

    def get_line_numbers(self, line):
        return self.dict[line]
