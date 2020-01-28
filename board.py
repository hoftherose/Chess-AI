from fastcore.all import *
import pygame
import chess

images = {
    "board": pygame.image.load("src/board.jpg"),
    "k": pygame.image.load("src/Piece_King_B.png"),
    "q": pygame.image.load("src/Piece_Queen_B.png"),
    "b": pygame.image.load("src/Piece_Bishop_B.png"),
    "n": pygame.image.load("src/Piece_Knight_B.png"),
    "r": pygame.image.load("src/Piece_Rook_B.png"),
    "p": pygame.image.load("src/Piece_Pawn_B.png"),
    "K": pygame.image.load("src/Piece_King_W.png"),
    "Q": pygame.image.load("src/Piece_Queen_W.png"),
    "B": pygame.image.load("src/Piece_Bishop_W.png"),
    "N": pygame.image.load("src/Piece_Knight_W.png"),
    "R": pygame.image.load("src/Piece_Rook_W.png"),
    "P": pygame.image.load("src/Piece_Pawn_W.png")
}

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
    global images
    img_board = pygame.transform.scale(images["board"], (1000, 1000))
    win.blit(img_board, (0,0))
    x.draw_pieces(win)

@patch
def draw_pieces(x:chess.Board, win):
    global images
    board_rep = x.get_board()
    for r,row in enumerate(board_rep):
        for c,symbol in enumerate(row):
            if symbol==".": continue
            win.blit(images[symbol], (50+50*c,50+50*r))