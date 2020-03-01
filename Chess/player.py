from .tools import *
from datetime import timedelta

class Player():
    def __init__(self, name:str, color:bool, time:int=1800, elo:int=1200):
        store_attr(self, "name,color,time,elo")
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return f"Player Name: {self.name} with {self.elo} ELO, playing {'whites' if self.color else 'blacks'}. Time remaining {timedelta(seconds=self.time)}."
    
    def selectMove(self, board):
        raise NotImplementedError

class PlayerHuman(Player):
    def selectMove(self, board):
        pygame.time.wait(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                absx, absy = event.pos
                if 0 <= (x:=absx-xmin) and x <= xrang and 0 <= (y:=absy-ymin) and y <= yrang:
                    col, row = int(x//col_len), int(y//row_len)
                    board.select(col,row)

class PlayerModel(Player):
    def __init__(self, name:str, color:bool, model:callable, time:int=1800, elo:int=1200, *args, **kwargs):
        super.__init__(name,color,time,elo)
        store_attr(self, "model,args,kwargs")

    def selectMove(self, board):
        getMoves = self.getPosibleMoves(board)
        nextMove = self.getPred(board, moves:list)
        board.push(nextMove)

    def getPosibleMoves(self, board):
        raise NotImplementedError

    def getPred(self, board, moves:list):
        raise NotImplementedError
