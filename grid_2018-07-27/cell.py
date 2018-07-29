

class Cell():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "Cell(%i,%i)" % (self.x, self.y)
    
    def set_neighbors(self, neighbors):
        self.neighbors = neighbors
    
    