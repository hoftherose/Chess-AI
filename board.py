from Chess.global_settings import *
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
def draw_board(x:chess.Board, win):
    global assets
    img_board = pygame.transform.scale(assets["board"], BoardScale)
    win.blit(img_board, BoardShift)
    x.draw_pieces(win)

@patch
def draw_pieces(x:chess.Board, win):
    global assets
    board_rep = x.get_board()
    for r,row in enumerate(board_rep):
        for c,symbol in enumerate(row):
            if symbol==".": continue
            win.blit(assets["Pieces"][symbol], (450+89.5*c,135+92.75*r))