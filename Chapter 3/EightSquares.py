#!/usr/bin/env python
from copy import deepcopy
from random import shuffle
from random import randint
import math

class EightSquares:
    def __init__(self):
        self.Arrangement = TileConfiguration()
        self.PreviousMove = [-1, -1]
        
    def MakeNextMove(self):
        hole = self.Arrangement.FindTheBlank()
        Move = TileConfiguration()
        BestCost = 2000
        Cost = 4000
        if (hole == 0):
            if self.PreviousMove[0] == 1 and self.PreviousMove[1] == 0:
                BestCost = 1000
                SwapID = 0
            else:
                Move.state = deepcopy(self.Arrangement.state)
                Move.TileSwapper(0,1)
                BestCost = Move.SolutionDistance()
                SwapID = 0
            if (self.PreviousMove[0] != 3 or self.PreviousMove[1] != 0):
                Move = deepcopy(self.Arrangement)
                Move.TileSwapper(0,3)
                Cost = Move.SolutionDistance()
            if (Cost < BestCost or (Cost == BestCost and randint(0,1) == 0)):
                BestCost = Cost
                SwapID = 1
            if (SwapID == 0):
                self.Arrangement.TileSwapper(0, 1)
                self.PreviousMove = [0, 1]
            else:
                self.Arrangement.TileSwapper(0, 3)
                self.PreviousMove = [0, 3]
                
        elif (hole == 1):
            if (self.PreviousMove[0] == 0 and self.PreviousMove[1] == 1):
                BestCost = 1000
                SwapID = 0
            else:
                Move.state = deepcopy(self.Arrangement.state)
                Move.TileSwapper(1, 0)
                BestCost = Move.SolutionDistance()
                SwapID = 0
            if (self.PreviousMove[0] != 2 or self.PreviousMove[1] != 1):
                Move.state = deepcopy(self.Arrangement.state)
                Move.TileSwapper(1, 2)
                Cost = Move.SolutionDistance()
            if (Cost < BestCost):
                BestCost = Cost
                SwapID = 1
            if (self.PreviousMove[0] != 4 or self.PreviousMove[1] != 1):
                Move.state = deepcopy(self.Arrangement.state)
                Move.TileSwapper(1, 4)
                Cost = Move.SolutionDistance()
            if (Cost < BestCost):
                BestCost = Cost
                SwapID = 2
                
            if (SwapID == 0):
                self.Arrangement.TileSwapper(1, 0)
                self.PreviousMove = [1, 0]
            elif(SwapID == 1):
                self.Arrangement.TileSwapper(1, 2)
                self.PreviousMove = [1, 2]
            elif(SwapID == 2):
                self.Arrangement.TileSwapper(1, 4)
                self.PreviousMove = [1, 4]
                
        elif (hole == 2):
            if (self.PreviousMove[0] == 1 and self.PreviousMove[1] == 2):
                BestCost = 1000
                SwapID = 0
            else:
                Move.state = deepcopy(self.Arrangement.state)
                Move.TileSwapper(2, 1)
                BestCost = Move.SolutionDistance()
                SwapID = 0
            if (self.PreviousMove[0] != 5 or self.PreviousMove[1] != 2):
                Move.state = deepcopy(self.Arrangement.state)
                Move.TileSwapper(2, 5)
                Cost = Move.SolutionDistance()
            if (Cost < BestCost or (Cost == BestCost and randint(0,1) == 0)):
                BestCost = Cost
                SwapID = 1
            if (SwapID == 0):
                self.Arrangement.TileSwapper(2, 1)
                self.PreviousMove = [2, 1]
            elif (SwapID == 1):
                self.Arrangement.TileSwapper(2, 5)
                self.PreviousMove = [2, 5]

        elif (hole == 3):
            if (self.PreviousMove[0] == 0 and self.PreviousMove[1] == 3):
                BestCost = 1000
                SwapID = 0
            else:
                Move.state = deepcopy(self.Arrangement.state)
                Move.TileSwapper(3, 0)
                BestCost = Move.SolutionDistance()
                SwapID = 0
            if (self.PreviousMove[0] != 4 or self.PreviousMove[1] != 3):
                Move.state = deepcopy(self.Arrangement.state)
                Move.TileSwapper(3, 4)
                Cost = Move.SolutionDistance()
            if (Cost < BestCost or (Cost == BestCost and randint(0,1) == 0)):
                BestCost = Cost
                SwapID = 1
            if (self.PreviousMove[0] != 6 or self.PreviousMove[1] != 3):
                Move.state = deepcopy(self.Arrangement.state)
                Move.TileSwapper(3, 6)
                Cost = Move.SolutionDistance()
            if (Cost < BestCost or (Cost == BestCost and randint(0,1) == 0)):
                BestCost = Cost
                SwapID = 2
                
            if (SwapID == 0):
                self.Arrangement.TileSwapper(3, 0)
                self.PreviousMove = [3, 0]
            elif(SwapID == 1):
                self.Arrangement.TileSwapper(3, 4)
                self.PreviousMove = [3, 4]
            elif(SwapID == 2):
                self.Arrangement.TileSwapper(3, 6)
                self.PreviousMove = [3, 6]
                
        elif (hole == 4):
            if (self.PreviousMove[0] == 1 and self.PreviousMove[1] == 4):
                BestCost = 1000
                SwapID = 0
            else:
                Move.state = deepcopy(self.Arrangement.state)
                Move.TileSwapper(4, 1)
                BestCost = Move.SolutionDistance()
                SwapID = 0
            if (self.PreviousMove[0] != 3 or self.PreviousMove[1] != 4):
                Move.state = deepcopy(self.Arrangement.state)
                Move.TileSwapper(4, 3)
                Cost = Move.SolutionDistance()
            if (Cost < BestCost or (Cost == BestCost and randint(0,1) == 0)):
                BestCost = Cost
                SwapID = 1
            if (self.PreviousMove[0] != 5 or self.PreviousMove[1] != 4):
                Move.state = deepcopy(self.Arrangement.state)
                Move.TileSwapper(4, 5)
                Cost = Move.SolutionDistance()
            if (Cost < BestCost or (Cost == BestCost and randint(0,1) == 0)):
                BestCost = Cost
                SwapID = 2
            if (self.PreviousMove[0] != 7 or self.PreviousMove[1] != 4):
                Move.state = deepcopy(self.Arrangement.state)
                Move.TileSwapper(4, 7)
                Cost = Move.SolutionDistance()
            if (Cost < BestCost or (Cost == BestCost and randint(0,1) == 0)):
                BestCost = Cost
                SwapID = 3
                
            if (SwapID == 0):
                self.Arrangement.TileSwapper(4, 1)
                self.PreviousMove = [4, 1]
            elif(SwapID == 1):
                self.Arrangement.TileSwapper(4, 3)
                self.PreviousMove = [4, 3]
            elif(SwapID == 2):
                self.Arrangement.TileSwapper(4, 5)
                self.PreviousMove = [4, 5]
            elif(SwapID == 3):
                self.Arrangement.TileSwapper(4, 7)
                self.PreviousMove = [4, 7]

        elif (hole == 5):
            if (self.PreviousMove[0] == 2 and self.PreviousMove[1] == 5):
                BestCost = 1000
                SwapID = 0
            else:
                Move.state = deepcopy(self.Arrangement.state)
                Move.TileSwapper(5, 2)
                BestCost = Move.SolutionDistance()
                SwapID = 0
            if (self.PreviousMove[0] != 4 or self.PreviousMove[1] != 5):
                Move.state = deepcopy(self.Arrangement.state)
                Move.TileSwapper(5, 4)
                Cost = Move.SolutionDistance()
            if (Cost < BestCost or (Cost == BestCost and randint(0,1) == 0)):
                BestCost = Cost
                SwapID = 1
            if (self.PreviousMove[0] != 8 or self.PreviousMove[1] != 5):
                Move.state = deepcopy(self.Arrangement.state)
                Move.TileSwapper(5, 8)
                Cost = Move.SolutionDistance()
            if (Cost < BestCost or (Cost == BestCost and randint(0,1) == 0)):
                BestCost = Cost
                SwapID = 2
                
            if (SwapID == 0):
                self.Arrangement.TileSwapper(5, 2)
                self.PreviousMove = [5, 2]
            elif(SwapID == 1):
                self.Arrangement.TileSwapper(5, 4)
                self.PreviousMove = [5, 4]
            elif(SwapID == 2):
                self.Arrangement.TileSwapper(5, 8)
                self.PreviousMove = [5, 8]

        elif (hole == 6):
            if (self.PreviousMove[0] == 3 and self.PreviousMove[1] == 6):
                BestCost = 1000
                SwapID = 0
            else:
                Move.state = deepcopy(self.Arrangement.state)
                Move.TileSwapper(6, 3)
                BestCost = Move.SolutionDistance()
                SwapID = 0
            if (self.PreviousMove[0] != 7 or self.PreviousMove[1] != 6):
                Move.state = deepcopy(self.Arrangement.state)
                Move.TileSwapper(6, 7)
                Cost = Move.SolutionDistance()
            if (Cost < BestCost or (Cost == BestCost and randint(0,1) == 0)):
                BestCost = Cost
                SwapID = 1
            if (SwapID == 0):
                self.Arrangement.TileSwapper(6, 3)
                self.PreviousMove = [6, 3]
            elif(SwapID == 1):
                self.Arrangement.TileSwapper(6, 7)
                self.PreviousMove = [6, 7]

        elif (hole == 7):
            if (self.PreviousMove[0] == 4 and self.PreviousMove[1] == 7):
                BestCost = 1000
                SwapID = 0
            else:
                Move.state = deepcopy(self.Arrangement.state)
                Move.TileSwapper(7, 4)
                BestCost = Move.SolutionDistance()
                SwapID = 0
            if (self.PreviousMove[0] != 6 or self.PreviousMove[1] != 7):
                Move.state = deepcopy(self.Arrangement.state)
                Move.TileSwapper(7, 6)
                Cost = Move.SolutionDistance()
            if (Cost < BestCost or (Cost == BestCost and randint(0,1) == 0)):
                BestCost = Cost
                SwapID = 1
            if (self.PreviousMove[0] != 8 or self.PreviousMove[1] != 7):
                Move.state = deepcopy(self.Arrangement.state)
                Move.TileSwapper(7, 8)
                Cost = Move.SolutionDistance()
            if (Cost < BestCost or (Cost == BestCost and randint(0,1) == 0)):
                BestCost = Cost
                SwapID = 2
                
            if (SwapID == 0):
                self.Arrangement.TileSwapper(7, 4)
                self.PreviousMove = [7, 4]
            elif(SwapID == 1):
                self.Arrangement.TileSwapper(7, 6)
                self.PreviousMove = [7, 6]
            elif(SwapID == 2):
                self.Arrangement.TileSwapper(7, 8)
                self.PreviousMove = [7, 8]
                
        elif (hole == 8):
            if (self.PreviousMove[0] == 5 and self.PreviousMove[1] == 8):
                BestCost = 1000
                SwapID = 0
            else:
                Move.state = deepcopy(self.Arrangement.state)
                Move.TileSwapper(8, 5)
                BestCost = Move.SolutionDistance()
                SwapID = 0
            if (self.PreviousMove[0] != 7 or self.PreviousMove[1] != 8):
                Move.state = deepcopy(self.Arrangement.state)
                Move.TileSwapper(8, 7)
                Cost = Move.SolutionDistance()
            if (Cost < BestCost or (Cost == BestCost and randint(0,1) == 0)):
                BestCost = Cost
                SwapID = 1
            if (SwapID == 0):
                self.Arrangement.TileSwapper(8, 5)
                self.PreviousMove = [8, 5]
            elif(SwapID == 1):
                self.Arrangement.TileSwapper(8, 7)
                self.PreviousMove = [8, 7]

            

class TileConfiguration:
    def __init__(self):
        self.state = [0,1,2,3,4,5,6,7,8]
    
    def SolutionDistance(self):
        HowMuch = 0
        LUT = [[0 for x in range(9)] for y in range(9)]
        LUT[0] = [0, 0, 1,  2, 1, 3,  2, 3, 4]
        LUT[1] = [0, 1, 0,  1, 2, 2,  3, 2, 3]
        LUT[2] = [0, 2, 1,  0, 3, 1,  4, 3, 2]
        LUT[3] = [0, 1, 2,  3, 0, 2,  1, 2, 3]
        LUT[4] = [0, 2, 1,  2, 1, 1,  2, 1, 2]
        LUT[5] = [0, 3, 2,  1, 2, 0,  3, 2, 1]
        LUT[6] = [0, 2, 3,  4, 1, 3,  0, 1, 2]
        LUT[7] = [0, 3, 2,  3, 2, 2,  1, 0, 1]
        LUT[8] = [0, 4, 3,  2, 3, 1,  2, 1, 0]
 #       print self.state
        for i in range(0, 9):
            HowMuch += LUT[i][self.state[i]]
 #           print HowMuch, i, self.state[i], LUT[i][self.state[i]]
        return HowMuch
    
    def Randomize(self):
        shuffle(self.state)
        
    def TileSwapper(self, i, j):
        temp = self.state[i]
        self.state[i] = self.state[j]
        self.state[j] = temp
        
    def SameTiles(self, other):
        for i in range(9):
            if self.state[i] != other.state[i]:
                return 0
        return 1
    
    def FindTheBlank(self):
        for i in range(9):
            if self.state[i] == 0:
                return i
    
    def Orientation(self):
        Flipper = 0
        Mirror = deepcopy(self)
        for i in range(9):
            for j in range(8):
                if (Mirror.state[j] > Mirror.state[j+1]):
                    Mirror.TileSwapper(j,j+1)
                    if Mirror.state[j] != 0 :
                        Flipper = Flipper+1
        return Flipper%2
        
Problem = EightSquares()
parity = 1
while (parity == 1):
    Problem.Arrangement.Randomize()
    parity = Problem.Arrangement.Orientation()
    
Current = Problem
print "Current Table \n", Current.Arrangement.state[0], Current.Arrangement.state[1], Current.Arrangement.state[2]
print Current.Arrangement.state[3], Current.Arrangement.state[4], Current.Arrangement.state[5]
print Current.Arrangement.state[6], Current.Arrangement.state[7], Current.Arrangement.state[8]
print "Distance = ", Current.Arrangement.SolutionDistance()
Attempts = 0
while (Current.Arrangement.SolutionDistance() > 0 and Attempts < 1000):
    Current.MakeNextMove()
    print "Current Table \n", Current.Arrangement.state[0], Current.Arrangement.state[1], Current.Arrangement.state[2]
    print Current.Arrangement.state[3], Current.Arrangement.state[4], Current.Arrangement.state[5]
    print Current.Arrangement.state[6], Current.Arrangement.state[7], Current.Arrangement.state[8]
    print "Distance = ", Current.Arrangement.SolutionDistance()
    Attempts = Attempts+1
 
    
if (Attempts < 1000):
    print "Success in ", Attempts, "tries"
else:
    print "I give up"
