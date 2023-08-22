class IntDataFrame():
    def __init__(self, column):
      self.column = column
      self.int()
    
    def int(self):
        self.column = [int(elem) for elem in self.column]
    
    def count(self):
        f = lambda x: x != 0
        return len(list(filter(f, self.column)))
    
    def unique(self):
        return len(set(self.column))