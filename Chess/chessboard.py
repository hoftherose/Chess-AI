from .chessvisuals import *
from .tools import *

@patch
def get_board(board:chess.Board)->list:
    board_rep = []
    row_rep = []
    for square in chess.SQUARES_180:
        if piece := board.piece_at(square):
            row_rep.append(piece.symbol())
        else:
            row_rep.append(".")
        if square%8 == 7:
            board_rep.append(row_rep)
            row_rep = []
    return board_rep

@patch
def draw_board(board:chess.Board, win:pygame.Surface):
    global assets
    img_board = pygame.transform.scale(assets["board"], BoardScale)
    win.blit(img_board, BoardShift)
    board.draw_pieces(win)
    if board.selected is not None:
        board.highlight(win)
        board.highlight_moves(win)

@patch
def draw_pieces(board:chess.Board, win:pygame.Surface):
    global assets
    board_rep = board.get_board()
    for c,col in enumerate(board_rep[::-1]):
        for r,symbol in enumerate(col):
            if symbol==".": continue
            win.blit(assets["Pieces"][symbol], (xmin+col_len*c,ymin+row_len*r))
