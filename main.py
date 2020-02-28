from Chess.tools import *
from Chess.chessboard import *

chessboard = chess.Board()

def setupWindow():
    pygame.init()
    win = pygame.display.set_mode(WindowSize)
    win.fill(WindowColor)
    pygame.display.set_caption("Chess AI")
    icon = assets["icon"]
    pygame.display.set_icon(icon)
    chessboard.selected = None
    return win

class Game():
    def __init__(self, win):
        self.win = win
        self.refresh()

    @classmethod
    def create(cls):
        return cls(setupWindow())

    def refresh(self):
        rep = chessboard.get_board()
        chessboard.draw_board(self.win)
        pygame.display.update()

    def run(self):
        running = True
        while running and not(chessboard.is_checkmate()):
            pygame.time.wait(100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    absx, absy = event.pos
                    if 0 <= (x:=absx-xmin) and x <= xrang and 0 <= (y:=absy-ymin) and y <= yrang:
                        col, row = int(x//col_len), int(y//row_len)
                        chessboard.select(col,row)
            self.refresh()

def main():
    game = Game.create()
    game.run()

if __name__ == "__main__":
    main()