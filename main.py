import chess
import pygame

def main():
    pygame.init()
    win = pygame.display.set_mode((500,500))
    pygame.display.set_caption("Chess AI")
    running = True
    while running:
        pygame.time.wait(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

if __name__ == "__main__":
    main()