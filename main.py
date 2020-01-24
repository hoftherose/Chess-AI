import chess
import pygame

def setup():
    pygame.init()
    win = pygame.display.set_mode((500,500))
    pygame.display.set_caption("Chess AI")
    pygame.image.load("chess.png")

def run():
    running = True
    while running:
        pygame.time.wait(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

def main():
    setup()
    run()
    pygame.quit()

if __name__ == "__main__":
    main()