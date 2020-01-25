from fastcore.all import *
import pygame
import chess

img_board = pygame.image.load("src/board.jpg")
img_king = pygame.image.load("src/Piece_King.jpg")
img_queen = pygame.image.load("src/Piece_Queen.jpg")
img_bishop = pygame.image.load("src/Piece_Bishop.jpg")
img_knight = pygame.image.load("src/Piece_Knight.jpg")
img_rook = pygame.image.load("src/Piece_Rook.jpg")
img_pawn = pygame.image.load("src/Piece_Pawn.jpg")

@patch
def get_board(x:chess.Board)->list:
    board_rep = []
    for square in chess.SQUARES_180:
        row_rep = []
        if piece := x.piece_at(square):
            row_rep.append(piece.symbol())
        else:
            row_rep.append(".")
        if chess.BB_SQUARES[square] & chess.BB_FILE_H & square == chess.H1:
            board_rep.append(row_rep)
    return board_rep

@patch
def draw_board(x:chess.Board, win):
    global img_board
    win.blit(img_board, (0,0))
    x.draw_pieces(win)