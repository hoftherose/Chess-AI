from fastcore.all import *

def coord2uci(Piece:Tuple(int,int), Dest:Tuple(int,int)):
    letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
    uci_ify = lambda col,row: letters[row]+str(col+1)
    return uci_ify(*Piece)+uci_ify(*Dest)

def uci2coord(uci:str):
    letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
    coord_ify = lambda uci: ((int(uci[1])-1, letters.index(uci[0])), (int(uci[3])-1, letters.index(uci[2])))
    return coord_ify(uci)

def prod(iterable:tuple):
    mult=lambda x,y: x*y
    return reduce(mult, iterable)