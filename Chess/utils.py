from fastcore.all import *

def uci(col:int, row:int):
    letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
    return letters[row]+str(col+1)

def coord2uci(Piece:Tuple(int,int), Dest:Tuple(int,int)):
    return uci(*Piece)+uci(*Dest)