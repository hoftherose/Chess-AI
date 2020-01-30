from Chess.global_settings import *
import chess
import pygame
import board

def setup():
    pygame.init()
    win = pygame.display.set_mode(WindowSize)
    win.fill(WindowColor)
    pygame.display.set_caption("Chess AI")
    icon = assets["icon"]
    pygame.display.set_icon(icon)
    board = chess.Board()
    rep = board.get_board()
    board.draw_board(win)

def run():
    running = True
    while running:
        pygame.time.wait(100)
        # refresh_board()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                absx, absy = event.pos
                if 0 <= (x:=absx-xmin) and x <= xrang and 0 <= (y:=absy-ymin) and y <= yrang:
                    print((x//col_len,y//row_len))

def main():
    setup()
    run()
    pygame.quit()

if __name__ == "__main__":
    main()