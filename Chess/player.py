from .tools import *
from datetime import timedelta

class Player():
    def __init__(self, name:str, color:bool, time:int=1800, elo:int=1200):
        store_attr(self, "name,color,time,elo")
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return f"Player Name: {self.name} with {self.elo} ELO, playing {'whites' if self.color else 'blacks'}. Time remaining {timedelta(seconds=self.time)}."
    
    def selectMove(self):
        raise NotImplementedError

class PlayerHuman(Player):
    def selectMove(self):
        pass