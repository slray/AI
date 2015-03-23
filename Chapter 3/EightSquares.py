#!/usr/bin/env python
from copy import deepcopy
from random import shuffle
import math

class EightSquares:
    def __init__(self):
        self.Arrangement = TileConfiguration()
        self.Arrangement.Randomize()
        self.children = []
        self.parent = None
        self.Generation = 0
                   
    def AddChild(self, i, j):
        OffSpring = deepcopy(self)
        OffSpring.parent = self
        nodeTemp = OffSpring.state[i]
        OffSpring.state[i] = OffSpring.state[j]
        OffSpring.state[j] = nodeTemp
        if self.Generation > 0:
            GrandParent = self.parent
            if GrandParent.SameState(OffSpring):
                return
        OffSpring.Generation = self.Generation+1
        print OffSpring.state
#        OffSpring.away = OffSpring.SolutionProximity()
#       print OffSpring.state, OffSpring.away
#        if (OffSpring.away < self.away):
        if (self.SolutionProximity() >= OffSpring.SolutionProximity()):
            self.children.append(OffSpring)
            print "Better Answer  ", OffSpring.state
                
    def RemoveChild(self, i):
        if (self.HowManyChildren() < i):
            return 0
        else:
            del self.children[i]
            return 1
        
    def GetChild(self, i):
        if (len(self.children) < i):
            return self
        else:
            return self.children[i]
               
    def MakeNextStates(self):
        hole = self.Arrangement.FindTheBlank()
        if (self.hole == 0):
            self.AddChild(0,1)
            self.AddChild(0,3)
        elif (self.hole == 1):
            self.AddChild(0, 1)
            self.AddChild(1, 2)
            self.AddChild(1, 4)
        elif (self.hole == 2):
            self.AddChild(2,1)
            self.AddChild(2,5)
        elif (self.hole == 3):
            self.AddChild(0, 3)
            self.AddChild(3, 4)
            self.AddChild(3, 6)
        elif (self.hole == 4):
            self.AddChild(1, 4)
            self.AddChild(3, 4)
            self.AddChild(4, 5)
            self.AddChild(4, 7)
        elif (self.hole == 5):
            self.AddChild(3, 5)
            self.AddChild(4, 5)
            self.AddChild(5, 8)
        elif (self.hole == 6):
            self.AddChild(3, 6)
            self.AddChild(6, 7)
        elif (self.hole == 7):
            self.AddChild(4, 7)
            self.AddChild(6, 7)
            self.AddChild(7, 8)
        elif (self.hole == 8):
            self.AddChild(5, 8)
            self.AddChild(7, 8)
            

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
        for i in range(0, 9):
            HowMuch += LUT[i][self.state[i]]
#            print HowMuch, i, self.state[i], LUT[i][self.state[i]]
        return HowMuch
    
    def Randomize(self):
        shuffle.shuffle(self.state)
        
    def TileSwapper(self, i, j):
        temp = state[i]
        state[i] = state[j]
        state[j] = temp
        
    def SameTiles(self, other):
        for i in range(9):
            if self.state[i] != other.state[i]:
                return 0
        return 1
    
    def FindTheBlank(self):
        for i in range(9):
            if self.state[i] == 0:
                return i
 
                           
Problem = EightSquares()
print Problem
#Problem.Arrangement.Randomize()

print Problem.Arrangement