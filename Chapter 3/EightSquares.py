#!/usr/bin/env python
from copy import deepcopy
from random import shuffle
import math

class Arbor:
    def __init__(self):
        self.Configuration = EightSquares()
        print self.Configuration.state
        shuffle(self.Configuration.state)
        print self.Configuration.state
        if (self.Configuration.GoalState()):
            print "Found a solution"
        else:
            print "No solution yet"       
        self.Configuration.MakeNextStates()
        self.CurrentBranch = self.Configuration
     
    def GetRoot(self):
        return self.CurrentBranch
    
    def GetChild(self):
        if (self.CurrentNode.HowManyChildren() == 0):
            return CurrentBranch
        else:
            return CurrentBranch.children[0]
     
    def RemoveChild(self, i):
        if (self.CurrentNode.HowManyChildren() < i):
            return
        else:
            del self.CurrentNode.children[i]
    
        
class EightSquares:
    #code

    def __init__(self):
        self.state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.hole = 0
        self.children = []
        self.parent = self
            
    def FindTheHole(self):
        for i in range(0,9):
            if (self.state[i]==0):
                self.hole = i
                return i
        return -1
    
    def HowManyKids(self):
        Offspring = 0
        for child in self.children:
            Offspring += 1
        return Offspring
        
    def StringSwap(self, i, j):
        nodetemp = self.state[i]
        self.state[i] = self.state[j]
        self.state[j] = nodetemp
    
    def GoalState(self):
        for i in range (0,9):
            if (self.state[i] != i):
                return 0
        return 1
    
    def SameState(Mate):
        for i in range (0, 9):
            if (self.state[i] != Mate.state[i]):
                return 0
        return 1
    
    def AddChild(self, i, j):
        OffSpring = deepcopy(self)
        OffSpring.parent = self
        nodeTemp = OffSpring.state[i]
        OffSpring.state[i] = OffSpring.state[j]
        OffSpring.state[j] = nodeTemp
        self.children.append(OffSpring)
        
    def MakeNextStates(self):
        self.FindTheHole()
        self.children = []
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
 
print "\n\nStarting a new Problem"
Problem = Arbor()
CurrentNode = Problem.GetRoot()
Kids = CurrentNode.HowManyKids()
#del Problem.children[Kids-1]
#Kids = Problem.HowManyKids()
print "Kids = ", Kids

    
     
    
