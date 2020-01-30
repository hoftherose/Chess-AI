import pygame
__all__ = ["assets", "BoardScale", "BoardRange", "BoardShift", "WindowColor", "WindowSize"]

assets = {
    "board": pygame.image.load("src/board.jpg"),
    "icon": pygame.image.load("src/icon.png"),
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
BoardRange = {"xmin": 154, "xmax": 870, "xrang": 716, "ymin": 138, "ymax": 880, "yrang": 742}
BoardShift = (300, 0)

WindowColor = (255,255,255)
WindowSize = (1600,1000)