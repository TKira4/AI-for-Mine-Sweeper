import pygame
from board import Board

class AISolver:
    def __init__(self, board):
        self.board = board

        
    def solve(self, draw_board):
        stack = []
        for x in range(self.board.height):
            for y in range(self.board.width):
                if not self.board.revealed[x][y]:
                    stack.append((x, y))
                    break
                
            if stack:
                break
            
        while stack:
            pygame.event.pump()
            x, y = stack.pop()
            
            if self.board.revealed[x][y]: #bo qua neu da mo o
                continue
            
            if self.board.is_mine(x, y): #cam flag cho min`
                self.board.flags[x][y] = True
                continue
            
            #mo o
            self.board.reveal(x, y)
            
            draw_board(self.board)
            pygame.display.update()
            pygame.time.delay(200)
            
            if self.board.grid[x][y] == 0:
                directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.board.height and 0 <= ny < self.board.width and not self.board.revealed[nx][ny]:
                        stack.append((nx, ny))
                        
        print("AI has solved Mine Sweeper!")