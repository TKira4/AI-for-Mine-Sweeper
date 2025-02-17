import random

class Board:
    def __init__(self, width, height, num_mines): #khoi tao gia tri ban dau
        self.width = width
        self.height = height
        self.num_mines = num_mines
        #khoi tao bang
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]
        self.flags = [[False for _ in range(width)] for _ in range(height)]
        
        #dat min ngau nhien
        self._place_mines()
        self._caculate_numbers()
        
    def _place_mines(self): #dat min ngau nhien tren bang
        mine_placed = 0
        while mine_placed < self.num_mines:
            x,y = random.randint(0, self.height -1), random.randint(0, self.width - 1)
            if self.grid[x][y] == 0: #kiem tra xem da co min` chua
                self.grid[x][y] = -1 #-1 la min`
                mine_placed += 1
                
    def _caculate_numbers(self): #tinh toan so luong min xung quanh moi o da duoc mo
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for x in range(self.height):
            for y in range(self.width):
                #bo qua o co min
                if self.grid[x][y] == -1:
                    continue 
                count = sum(1 for dx, dy in directions 
                            if 0 <= x + dx < self.height 
                            and 0 <= y + dy < self.width 
                            and self.grid[x + dx][y + dy] == -1)
                self.grid[x][y] = count
                
    def reveal(self, x, y):
        if self.revealed[x][y]: #bo qua o da mo
            return
        self.revealed[x][y] = True
        
        if self.grid[x][y] == 0:
            directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.height and 0 <= ny < self.width and not self.revealed[nx][ny]:
                    self.reveal(nx, ny) #goi de quy DFS
                    
    def is_mine(self, x, y):
        return self.grid[x][y] == -1
    
    def is_solved(self):
        #kiem tra xem da mo het o khong phai min` chua
        for x in range(self.height):
            for y in range(self.width):
                if self.grid[x][y] != -1 and not self.revealed[x][y]:
                    return False
        
        return True
    
        