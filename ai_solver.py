import pygame
import random

class AISolver:
    def __init__(self, board, screen):
        self.board = board
        self.screen = screen

    def get_neighbors(self, x, y):
        #tra ve cac o lan can trong board
        neighbors = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.board.height and 0 <= ny < self.board.width:
                    neighbors.append((nx, ny))
        return neighbors

    def update_display(self):
        #step by step visualize
        self.board.draw_board(self.screen)
        pygame.display.flip()
        pygame.time.delay(300) #delay cho de nhin

    def flag_sure_mines(self):
        #dat co vao o chac chan la min
        changed = False
        for x in range(self.board.height):
            for y in range(self.board.width):
                if self.board.revealed[x][y] and self.board.grid[x][y] > 0:
                    neighbors = self.get_neighbors(x, y)
                    hidden = [n for n in neighbors if not self.board.revealed[n[0]][n[1]]]
                    flagged = [n for n in neighbors if self.board.flags[n[0]][n[1]]]

                    #neu cac o chua mo + so flag xung quanh thi cac o do la bomb
                    if len(hidden) > 0 and len(hidden) + len(flagged) == self.board.grid[x][y]:
                        for nx, ny in hidden:
                            if not self.board.flags[nx][ny]:
                                self.board.flags[nx][ny] = True
                                print(f"🚩Flagging ({nx}, {ny})")
                                self.update_display()
                                changed = True
        return changed

    def reveal_safe_cells(self):
        #mo cac o an toan sau khi da cam co
        changed = False
        for x in range(self.board.height):
            for y in range(self.board.width):
                if self.board.revealed[x][y] and self.board.grid[x][y] > 0:
                    neighbors = self.get_neighbors(x, y)
                    hidden = [n for n in neighbors if not self.board.revealed[n[0]][n[1]]]
                    flagged = [n for n in neighbors if self.board.flags[n[0]][n[1]]]

                    #neu da cam flag du voi so bomb tuong ung thi co the mo nhung o con lai
                    if len(flagged) == self.board.grid[x][y]:
                        for nx, ny in hidden:
                            if not self.board.revealed[nx][ny]:
                                self.board.reveal(nx, ny)
                                print(f"--Open cell: --({nx}, {ny})")
                                self.update_display()
                                changed = True
        return changed

    def solve(self):
        moves_made = False

        #first move (nuoc di dau tien)
        if not any(cell for row in self.board.revealed for cell in row):
            for x in range(self.board.height):
                for y in range(self.board.width):
                    if self.board.grid[x][y] != -1:
                        self.board.reveal(x, y)
                        print(f"🟢 AI start at ({x}, {y})")
                        self.update_display()
                        moves_made = True
                        break
                if moves_made:
                    break

        #main loop
        while True:
            changed1 = self.flag_sure_mines()
            changed2 = self.reveal_safe_cells()
            if changed1 or changed2:
                moves_made = True
                continue
            else:
                #neu khong co nuoc di an toan, se suy luan don gian
                candidates = []
                for x in range(self.board.height):
                    for y in range(self.board.width):
                        if not self.board.revealed[x][y] and not self.board.flags[x][y]:
                            candidates.append((x, y))
                if candidates:
                    move = random.choice(candidates)
                    self.board.reveal(move[0], move[1])
                    print(f"!!Guess move!! ({move[0]}, {move[1]})")
                    self.update_display()
                    moves_made = True
                    continue
                else:
                    break

        if not moves_made:
            print("❌Khong du du kien de hanh dong tiep!!!")
        else:
            print("✅AI da giai xong bai toan!")
