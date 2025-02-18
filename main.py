import pygame   #dung pygame de visualize
from board import Board
from ai_solver import AISolver

pygame.init()

CELL_SIZE = 30
WIDTH, HEIGHT = 10, 10

screen = pygame.display.set_mode((WIDTH * CELL_SIZE, HEIGHT * CELL_SIZE + 50))
pygame.display.set_caption("Mine Sweeper AI")

board = Board(WIDTH, HEIGHT, num_mines=15)
ai_solver = AISolver(board, screen)

running = True
ai_running = False
clock = pygame.time.Clock()

while running:
    #ve background va board
    screen.fill((200, 200, 200))
    board.draw_board(screen)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #an space de AI giai tiep hoac dung
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ai_running = not ai_running  

    if ai_running:
        #goi ham de AI hanh dong va cap nhat board
        ai_solver.solve()

    clock.tick(30)

pygame.quit()
