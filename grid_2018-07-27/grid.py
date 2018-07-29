from cell import Cell


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.size = width * height
        self.cells = []
        self.build_cells()
        
    
    def build_cells(self):
        self.cells = [[] for x in range(self.width)]
        for x in range(self.width):
            self.cells[x] = [Cell(x,y) for y in range(self.height)]
                
    def assign_neighbors(self):
        for row in self.cells:
            for cell in row:
                neighbors = []
                if self.in_grid(cell.x-3, cell.y):
                    neighbors.append(self.cells[cell.x-3][cell.y])
                if self.in_grid(cell.x+3, cell.y):
                    neighbors.append(self.cells[cell.x+3][cell.y])
                if self.in_grid(cell.x, cell.y+3):
                    neighbors.append(self.cells[cell.x][cell.y+3])
                if self.in_grid(cell.x, cell.y-3):
                    neighbors.append(self.cells[cell.x][cell.y-3])
                if self.in_grid(cell.x-2, cell.y-2):
                    neighbors.append(self.cells[cell.x-2][cell.y-2])
                if self.in_grid(cell.x-2, cell.y+2):
                    neighbors.append(self.cells[cell.x-2][cell.y+2])
                if self.in_grid(cell.x+2, cell.y-2):
                    neighbors.append(self.cells[cell.x+2][cell.y-2])
                if self.in_grid(cell.x+2, cell.y+2):
                    neighbors.append(self.cells[cell.x+2][cell.y+2])
                cell.set_neighbors(neighbors)
                                   
    def in_grid(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height
                
                
    def find_path(self):
        for cell in self.cells:
            path = []
            unvisited = self.cells
            path.append(cell)
                
                
                
    
