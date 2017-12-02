class DirectoryChange(Change):
    def __init__(self, id, effect, path):
        super.__init__(id)
        self.effect = effect
        self.path = path
