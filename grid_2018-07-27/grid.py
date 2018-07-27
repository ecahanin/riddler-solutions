from cell import Cell


class Grid:
    def __init__(self, width, height):
        grid.width = width
        grid.height = height
        grid.size = width * height
        grid.cells = []
        self.build_cells()
        
    
    def build_cells(self):
        for x in range(0, width):
            self.cells[x] = []
            for y in range(0, height):
                self.cells[x][y] = Cell(x,y)
                
    def assign_neighbors(self):
        for row in self.cells:
            for cell in row:
                neighbors = []
                #horizontal neighbor:
                if 0 <= cell.x + 3 < self.width:
                    neighbors.append(self.cells[cell.x+3][cell.y])
                
                
    def find_path(self):
        for cell in self.cells:
            path = []
            unvisited = self.cells
            path.append(cell)
                
                
                
    
