from .tools import *
from .utils import *


@patch
def select(board:chess.Board, col:int, row:int):
    coords = (col,row)
    if board.selected is not None:
        if board.selected != coords:
            uci = coord2uci(board.selected, coords)
            move = chess.Move.from_uci(uci)
            if board.is_legal(move):
                board.push(move)
        board.selected=None
    elif board.legal_piece(coords):
        board.selected = coords

@patch
def legal_piece(board:chess.Board, coords):
    num = coords[0]*8+coords[1]
    if board.piece_at(num) is not None:
        return board.piece_at(num).color == board.turn

@patch
def highlight(board:chess.Board, win:pygame.Surface):
    global assets
    select_effect = pygame.transform.scale(assets["highlight"], (int(col_len), int(row_len)))
    win.blit(select_effect, board.get_selected_coord())

@patch
def get_selected_coord(board:chess.Board):
    CellShift=[prod(values) for values in zip((col_len,row_len),board.selected)]
    return [sum(values) for values in zip(BoardCorner,CellShift)]