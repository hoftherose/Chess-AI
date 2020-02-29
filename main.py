from Chess.tools import *
from Chess.chessboard import *
from Chess.player import *

def setupWindow():
    pygame.init()
    win = pygame.display.set_mode(WindowSize)
    win.fill(WindowColor)
    pygame.display.set_caption("Chess AI")
    icon = assets["icon"]
    pygame.display.set_icon(icon)
    return win

class Game():
    def __init__(self, win:pygame.Surface, player1:Player, player2:Player):
        store_attr(self, "win,player1,player2")
        self.board = chess.Board()
        self.board.selected = None
        self.refresh()

    @classmethod
    def create(cls, player1:Player, player2:Player):
        return cls(setupWindow(), player1, player2)

    def refresh(self):
        rep = self.board.get_board()
        self.board.draw_board(self.win)
        pygame.display.update()

    def run(self):
        running = True
        while running and not(self.board.is_checkmate()):
            pygame.time.wait(100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    absx, absy = event.pos
                    if 0 <= (x:=absx-xmin) and x <= xrang and 0 <= (y:=absy-ymin) and y <= yrang:
                        col, row = int(x//col_len), int(y//row_len)
                        self.board.select(col,row)
            self.refresh()

def main():
    whitePlayer, blackPlayer = PlayerHuman("Whites", True), PlayerHuman("Blacks", False)
    game = Game.create(whitePlayer, blackPlayer)
    game.run()

if __name__ == "__main__":
    main()