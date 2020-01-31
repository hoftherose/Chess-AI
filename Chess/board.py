from .global_settings import *
from .utils import *
from fastcore.all import patch
import pygame
import chess

@patch
def get_board(x:chess.Board)->list:
    board_rep = []
    row_rep = []
    for square in chess.SQUARES_180:
        if piece := x.piece_at(square):
            row_rep.append(piece.symbol())
        else:
            row_rep.append(".")
        if square%8 == 7:
            board_rep.append(row_rep)
            row_rep = []
    return board_rep

@patch
def draw_board(x:chess.Board, win:pygame.Surface):
    global assets
    img_board = pygame.transform.scale(assets["board"], BoardScale)
    win.blit(img_board, BoardShift)
    x.draw_pieces(win)

@patch
def draw_pieces(x:chess.Board, win:pygame.Surface):
    global assets
    board_rep = x.get_board()
    for c,col in enumerate(board_rep[::-1]):
        for r,symbol in enumerate(col):
            if symbol==".": continue
            win.blit(assets["Pieces"][symbol], (xmin+col_len*c,ymin+row_len*r))

@patch
def select(x:chess.Board, col:int, row:int):
    uci = conv2uci(col,row)
    if x.selected is not None:
        if x.selected != uci:
            move = chess.Move.from_uci(x.selected+uci)
            if x.is_legal(move):
                x.push(move)
        x.selected=None
    else:
        x.selected = uci
