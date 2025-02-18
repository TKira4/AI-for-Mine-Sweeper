import pygame
import random

CELL_SIZE = 30

class Board:
    def __init__(self, width, height, num_mines):
        self.width = width
        self.height = height
        self.num_mines = num_mines
        #dung mang 2 chieu de luu toa do
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]
        self.flags = [[False for _ in range(width)] for _ in range(height)]
        
        self.place_mines()
        self.calculate_numbers()

    def place_mines(self):
        mines_placed = 0
        while mines_placed < self.num_mines:
            x, y = random.randint(0, self.height - 1), random.randint(0, self.width - 1)
            if self.grid[x][y] == 0:
                self.grid[x][y] = -1
                mines_placed += 1

    def calculate_numbers(self):
        for x in range(self.height):
            for y in range(self.width):
                if self.grid[x][y] == -1:
                    continue
                count = 0
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < self.height and 0 <= ny < self.width and self.grid[nx][ny] == -1:
                            count += 1
                self.grid[x][y] = count

    def draw_board(self, window):
        for x in range(self.height):
            for y in range(self.width):
                rect = pygame.Rect(y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(window, (150, 150, 150), rect, 2)

                if self.flags[x][y]:
                    #ve flag
                    pygame.draw.rect(window, (255, 0, 0), rect)

                if self.revealed[x][y]:
                    #o dau tien da mo
                    pygame.draw.rect(window, (200, 200, 200), rect)
                    if self.grid[x][y] == -1:
                        #ve bomb
                        pygame.draw.circle(window, (0, 0, 0), rect.center, CELL_SIZE // 3)
                    elif self.grid[x][y] > 0:
                        font = pygame.font.Font(None, 24)
                        text = font.render(str(self.grid[x][y]), True, (0, 0, 0))
                        window.blit(text, (y * CELL_SIZE + 10, x * CELL_SIZE + 5))

    def reveal(self, x, y):
        if self.revealed[x][y] or self.flags[x][y]:
            return  #neu o da mo thi se khong lam gi

        stack = [(x, y)]
        self.revealed[x][y] = True  #danh dau khi dua vao stack

        while stack:
            cx, cy = stack.pop()
            #neu o hien tai la blank thi mo rong ra cac o xung quanh nhu water blood
            if self.grid[cx][cy] == 0:
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        nx, ny = cx + dx, cy + dy
                        if 0 <= nx < self.height and 0 <= ny < self.width:
                            if not self.revealed[nx][ny] and not self.flags[nx][ny]:
                                self.revealed[nx][ny] = True  #danh dau de khong bi lap lai
                                stack.append((nx, ny))

    def is_solved(self):
        #tra ve true neu tat ca cac o da duoc cam co hoac da mo
        for x in range(self.height):
            for y in range(self.width):
                if self.grid[x][y] == -1 and not self.flags[x][y]:
                    return False
        return True
