import pygame   #dung pygame de visualize
from board import Board
from ai_solver import AISolver

#khoi tao pygame
pygame.init()

CELL_SIZE = 30  #kich thuoc o
WIDTH, HEIGHT = 10, 10  #so luong o 10x10

#Ve screen
screen = pygame.display.set_mode((WIDTH * CELL_SIZE, HEIGHT * CELL_SIZE + 50))
pygame.display.set_caption("Mine Sweeper AI")

board = Board(WIDTH, HEIGHT, num_mines=15) #so luong min` la 15
ai_solver = AISolver(board, screen)
def main():
    running = True
    ai_running = False
    clock = pygame.time.Clock()

    while running:
        #ve background va board
        screen.fill((200, 200, 200))
        board.draw_board(screen)
        if not ai_running:
            font = pygame.font.Font(None, 32)
            text = font.render("Press Space to Start", True, (255, 255, 255))
            text_rect = text.get_rect(center=(WIDTH * CELL_SIZE // 2, HEIGHT * CELL_SIZE * 1.1))
            screen.blit(text, text_rect)
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
            state = ai_solver.solve() #tra ve state de khong goi giai thuat nua
            ai_running = state
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()