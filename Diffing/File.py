class File():
    def apply_delta(self, delta):
        # Apply changes to file from a delta
        
        for lineno, change in delta:

        pass

    def apply_deltas(self, deltas):
        for delta in deltas:
            self.apply_delta(delta)
    def compare(self, other):
        # Compare to files and return a delta
        pass
