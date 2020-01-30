from Chess.global_settings import *
import chess
import pygame
import board

chessboard = chess.Board()

def setup():
    global chessboard
    pygame.init()
    win = pygame.display.set_mode(WindowSize)
    win.fill(WindowColor)
    pygame.display.set_caption("Chess AI")
    icon = assets["icon"]
    pygame.display.set_icon(icon)
    rep = chessboard.get_board()
    chessboard.draw_board(win)

def run():
    global chessboard
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
                    col, row = int(x//col_len), int(y//row_len)
                    print(col, row)
                    print(chessboard.get_board()[row][col])

def main():
    setup()
    run()
    pygame.quit()

if __name__ == "__main__":
    main()