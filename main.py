import pygame
from board import Board
from ai_solver import AISolver

#khoi tao pygame va setting
pygame.init()
WIDTH, HEIGHT = 400, 400
GRID_SIZE = 10
CELL_SIZE = WIDTH // GRID_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

#cua so game
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mine Sweeper")

def draw_board(board):
    window.fill(WHITE)
    font = pygame.font.Font(None, 36)
    
    for x in range(board.height):
        for y in range(board.width):
            rect = pygame.Rect(y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(window, BLACK, rect, 1)
            
            if board.revealed[x][y]:
                pygame.draw.rect(window, GRAY, rect)
                if board.grid[x][y] > 0:
                    text = font.render(str(board.grid[x][y]), True, BLACK)
                    window.blit(text, (y * CELL_SIZE + 10, x * CELL_SIZE + 5))
            elif board.flags[x][y]:
                pygame.draw.rect(window, RED, rect)
    
    pygame.display.update()
    
if __name__ == "__main__":
    board = Board(width=GRID_SIZE, height=GRID_SIZE, num_mines=10)
    draw_board(board)
    ai = AISolver(board)
    
    running = True
    while running:
        draw_board(board)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  #press space to start
                    ai.solve(draw_board)
                elif event.key == pygame.K_q:  #press 'Q' to quit
                    running = False
                    
    pygame.quit()