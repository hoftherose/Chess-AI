import pygame

assets = {
    "board": pygame.image.load("src/board.jpg"),
    "icon": pygame.image.load("src/icon.png"),
    "highlight": pygame.image.load("src/highlight.png"),
    "highlight_legal": pygame.image.load("src/highlight_legal.png"),
    "highlight_attack": pygame.image.load("src/highlight_attack.png"),
    "Pieces": {
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
}

BoardScale = (1000, 1000)

xmin = 455
xmax = 1170
ymin = 139
ymax = 880

xrang = xmax-xmin
yrang = ymax-ymin
col_len = xrang/8
row_len = yrang/8

BoardShift = (300, 0)
BoardCorner = (455,139)

WindowColor = (255,255,255)
WindowSize = (1600,1000)