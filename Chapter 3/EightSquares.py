#!/usr/bin/env python
from copy import deepcopy
from random import shuffle
import math

class EightSquares:
    #code

    def __init__(self):
        self.state = "012345678"
        self.hole = 0
        self.TurnSignal = 0
        self.children = []
    
    def Shuffle(self):
        temp = list(self.state)
        shuffle(temp)
        self.state = "".join(temp)
            
    def FindTheHole(self):
        temp = list(self.state)
        for i in range(9):
            print "Checking for hole #", i
            if (temp[i]==str(0)):
                self.hole = i
                print "Hole found at ", self.hole
                return i
            
    def __str__(self):
        return self.state + "\n" + self.state[0:3] + "\n" + self.state[3:6] + "\n" + self.state[6:9] + "\n"
    
    def StringSwap(self, i, j):
        temp = list(self.state)
        chartemp = temp[i]
        temp[i] = temp[j]
        temp[j] = chartemp
        self.state = "".join(temp)
        
    def TurnLeft(self):
        temp = deepcopy(self)
        temp.state[0] = self.state[6]
        temp.state[1] = self.state[3]
        temp.state[2] = self.state[0]
        temp.state[3] = self.state[7]
        temp.state[5] = self.state[1]
        temp.state[6] = self.state[8]
        temp.state[7] = self.state[5]
        temp.state[8] = self.state[2]
        temp.TurnSignal -= 1;
        self = deepcopy(temp)
        del temp
        
    def TurnRight(self):
        temp = deepcopy(self)
        temp.state[0] = self.state[2]
        temp.state[1] = self.state[5]
        temp.state[2] = self.state[8]
        temp.state[3] = self.state[1]
        temp.state[5] = self.state[7]
        temp.state[6] = self.state[0]
        temp.state[7] = self.state[3]
        temp.state[8] = self.state[6]
        temp.TurnSignal += 1
        self = deepcopy(temp)
        del temp
    
    def ReturnHome(self):
        while (self.TurnSignal != 0):
            if (self.TurnSignal > 0):
                self.Turnleft()
            else:    self.TurnRight()
        
    def MakeNextStates(self):
        self.FindTheHole()
        print self.state, self.hole, self.TurnSignal
        self.children = []
        if (self.hole%2 == 1):  #hole in odd position
            if (self.hole == 3): self.TurnRight()
            if (self.hole == 5): self.TurnLeft()
            if (self.hole == 7):
                self.TurnLeft()
                self.TurnLeft()
            child1 = deepcopy(self)
            child1.StringSwap(0,1)
            child1.ReturnHome()
            self.children.append(child1)
            
            child2 = deepcopy(self)
            child2.StringSwap(1,2)
            child2.ReturnHome()
            self.children.append(child2)
            
            child3 = deepcopy(self)
            child3.StringSwap(1,4)
            child3.ReturnHome()
            self.children.append(child3)
                
        elif (self.hole%2 == 0 and self.hole != 4):  #hole in even position, but not the center
            if (self.hole == 2): self.TurnLeft()
            if (self.hole == 6): self.TurnRight()
            if (self.hole == 8):
                self.TurnLeft()
                self.TurnLeft()
            child1 = deepcopy(self)
            child1.StringSwap(0,1)
            child1.ReturnHome()
            self.children.append(child1)
           
            child2 = deepcopy(self)
            child2.StringSwap(0,3)
            child2.ReturnHome()                
            self.children.append(child2) 
               
        elif (self.hole == 4):  #hole in the center
            child1 = deepcopy(self)
            child1.StringSwap(1,4)
            child1.ReturnHome()
            self.children.append(child1)
       
            child2 = deepcopy(self)
            child2.StringSwap(3,4)
            child2.ReturnHome()
            self.children.append(child2)
            
            child3 = deepcopy(self)
            child3.StringSwap(4,5)
            child3.ReturnHome()
            self.children.append(child3)
            
            child4 = deepcopy(self)
            child4.StringSwap(4,7)
            child4.ReturnHome()
            self.children.append(child4)

Problem = EightSquares()
Problem.Shuffle()
print Problem
Problem.MakeNextStates()
for child in Problem.children:
    print child

    
     
    
