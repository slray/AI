#!/usr/bin/env python
import EightSquare

class GameTree:
    def __init__(self, parent, Board = None):
        self.parent = parent
        self.Tiles = Board
        self.Moves = []
        if parent is None:
            self.BirthOrder = 0
        else:
            self.BirthOrder= len(parent.Moves)
            parent.Moves.append(self)
        
    def Population(self):
        return len(self.Moves)
    
    def NthMove(self, n):
        return self.Move[n]
    
    def GetNthChild(self,n ):
        return self.Moves[n]
    


