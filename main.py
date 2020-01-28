import chess
import pygame
import board

def setup():
    pygame.init()
    win = pygame.display.set_mode((1600,1000))
    pygame.display.set_caption("Chess AI")
    icon = pygame.image.load("src/icon.png")
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

def main():
    setup()
    run()
    pygame.quit()

if __name__ == "__main__":
    main()