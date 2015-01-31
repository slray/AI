#!/usr/bin/env python
from copy import deepcopy
from random import shuffle
import math

class EightSquares:
    #code

    def __init__(self):
        self.state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.hole = 0
        self.TurnSignal = 0
        self.children = []
              
    def FindTheHole(self):
        for i in range(0,9):
            print "Checking for hole ", self.state[i]
            if (self.state[i]==0):
                self.hole = i
                print "\nHole found at ", self.hole
                return i
            
 #   def __str__(self):
 #      return self.state[0], self.state[1], self.state[2] + "\n"
    
    def StringSwap(self, i, j):
        print "Swapping ", i, j
        nodetemp = self.state[i]
        self.state[i] = self.state[j]
        self.state[j] = nodetemp
         
        
    def MakeNextStates(self):
        self.FindTheHole()
        print self.state, self.hole, self.TurnSignal
        self.children = []
        if (self.hole == 0):
            child1 = deepcopy(self)
            child2 = deepcopy(self)
            child1.StringSwap(0,1)
            child2.StringSwap(0,3)
            self.children.append(child1)
            self.children.append(child2)
        elif (self.hole == 1):
            child1 = deepcopy(self)
            child2 = deepcopy(self)
            child3 = deepcopy(self)
            child1.StringSwap(0,1)
            child2.StringSwap(1,2)
            child3.StringSwap(1,4)
            self.children.append(child1)
            self.children.append(child2)
            self.children.append(child3)
        elif (self.hole == 2):
            child1 = deepcopy(self)
            child2 = deepcopy(self)
            child1.StringSwap(2,1)
            child2.StringSwap(2,5)
            self.children.append(child1)
            self.children.append(child2)
        elif (self.hole == 3):
            child1 = deepcopy(self)
            child2 = deepcopy(self)
            child3 = deepcopy(self)
            child1.StringSwap(0,3)
            child2.StringSwap(3,4)
            child3.StringSwap(3,6)
            self.children.append(child1)
            self.children.append(child2)
            self.children.append(child3)
        elif (self.hole == 4):
            child1 = deepcopy(self)
            child2 = deepcopy(self)
            child3 = deepcopy(self)
            child4 = deepcopy(self)
            child1.StringSwap(1,4)
            child2.StringSwap(3,4)
            child3.StringSwap(4,5)
            child4.StringSwap(4,7)
            self.children.append(child1)
            self.children.append(child2)
            self.children.append(child3)
            self.children.append(child4)
        elif (self.hole == 5):
            child1 = deepcopy(self)
            child2 = deepcopy(self)
            child3 = deepcopy(self)
            child1.StringSwap(3,5)
            child2.StringSwap(4,5)
            child3.StringSwap(5,8)
            self.children.append(child1)
            self.children.append(child2)
            self.children.append(child3)
        elif (self.hole == 6):
            child1 = deepcopy(self)
            child2 = deepcopy(self)
            child1.StringSwap(3,6)
            child2.StringSwap(6,7)
            self.children.append(child1)
            self.children.append(child2)
        elif (self.hole == 7):
            child1 = deepcopy(self)
            child2 = deepcopy(self)
            child3 = deepcopy(self)
            child1.StringSwap(4,7)
            child2.StringSwap(6,7)
            child3.StringSwap(7,8)
            self.children.append(child1)
            self.children.append(child2)
            self.children.append(child3)
        elif (self.hole == 8):
            child1 = deepcopy(self)
            child2 = deepcopy(self)
            child1.StringSwap(5,8)
            child2.StringSwap(7,8)
            self.children.append(child1)
            self.children.append(child2)
 
Problem = EightSquares()
shuffle(Problem.state)
print "New problem"
print Problem.state
#PrintMe(Problem)
print "\n"
Problem.MakeNextStates()
print Problem.state
print "Children\n"
for child in Problem.children:
    print child.state
    print "\n"

    
     
    
