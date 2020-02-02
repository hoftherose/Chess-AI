from .global_settings import *
from .utils import *
from fastcore.all import patch
import pygame
import chess

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

@patch
def draw_pieces(board:chess.Board, win:pygame.Surface):
    global assets
    board_rep = board.get_board()
    for c,col in enumerate(board_rep[::-1]):
        for r,symbol in enumerate(col):
            if symbol==".": continue
            win.blit(assets["Pieces"][symbol], (xmin+col_len*c,ymin+row_len*r))

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
    else:
        board.selected = coords

@patch
def highlight(board:chess.Board, win:pygame.Surface):
    global assets
    select_effect = pygame.transform.scale(assets["highlight"], (int(col_len), int(row_len)))
    win.blit(select_effect, board.get_selected_coord())

@patch
def get_selected_coord(board:chess.Board):
    CellShift=[prod(values) for values in zip((col_len,row_len),board.selected)]
    return [sum(values) for values in zip(BoardCorner,CellShift)]