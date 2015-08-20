from pprint import pprint
from random import shuffle
import copy

import random
class bank:
    def __init__(self,side=None, missionaries=0,cannibals=0,boat=False):
        self.side = side
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat
        
    def __str__(self ):
        if self.boat:
            return "Side: " + str(self.side) +" :: M: "+str(self.missionaries)+ " C: "+str(self.cannibals)+" Boat: True "
        return "Side: " + str(self.side) +" :: M: "+str(self.missionaries)+ " C: "+str(self.cannibals)+" Boat: False"
        
    
    def isValid(self):
        if self.missionaries in range(0,4,1) and self.cannibals in range(0,4,1):
            if not self.missionaries:
                if not self.cannibals:
                    if self.boat:
                        return False
                return True
            if self.missionaries >= self.cannibals:
                return True
        return False
    

class tiles:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.buildTiles()
        self.solvable()
        pprint(self.findLocation())
    
    def buildTiles(self):
        pieces = (range(0,self.height*self.width,1))
        random.shuffle(pieces)
        self.flat = pieces
        self.tiles = list(chunks(pieces,self.width))
        
        print (2,2)+(2,2)
        
    def solvable(self):
        temp = copy.deepcopy(self.flat)
        pprint(temp)
        for i in range( len(temp)-1,-1,-1):
            if temp[i] == 0 :
                del temp[i]
        pprint(temp)
        total = 0
        for i in range(0, len(temp),1):
            total += i+temp[i]
        print total
        
    def findLocation(self, value=0):
        x = 0
        y = 0
        for row in self.tiles:
            x = 0
            for column in row:
                if self.tiles[y][x] == value:
                    return (y,x)
                x += 1
            y += 1
                
            
        
        

    #code

class state:
    def __init__(self, east=None, west=None, parent = None):
        self.eastBank = east
        if not self.eastBank:
            self.eastBank = bank("E")
            
        self.westBank = west
        if not self.westBank:
            self.westBank = bank("W")
        
        self.parent = parent
    
    def __str__(self):
        return "State: " + str(self.eastBank) + " |::| " + str(self.westBank)
    
    def __eq__(self,other):
        return str(self) == str(other)
    
    
    def isValid(self):
        return self.eastBank.isValid() and self.westBank.isValid()
    
    def spawnAllChildren(self):
        moves = [[0,1],[1,0],[1,1], [0,2], [2,0]]
        self.children = []
        for move in moves:
            newChild = self.spawnChild(move)
            if newChild.isValid():
                if newChild.checkParents(newChild.parent):
                    #print "Unique Valid Child:\n\t", newChild,"\n"
                    self.children.append(newChild)
                else:
                    pass
                    #print "Non-Unique Valid Child:\n\t", newChild,"\n"
            else:
                pass
                #print "Non-Unique Non-Valid Child:\n\t", newChild,"\n"
        return self.children

    def spawnChild(self, crossedMissionaries=0, crossedCannibals=0):
        
        if type(crossedMissionaries) == type([0,0]):
            crossedCannibals = crossedMissionaries[-1]
            crossedMissionaries = crossedMissionaries[0]
            
        if self.westBank.boat:
            crossedCannibals = crossedCannibals*-1
            crossedMissionaries = crossedMissionaries*-1
        
        return state(
            bank(self.eastBank.side,self.eastBank.missionaries-crossedMissionaries,self.eastBank.cannibals-crossedCannibals, not self.eastBank.boat),\
            bank(self.westBank.side,self.westBank.missionaries+crossedMissionaries,self.westBank.cannibals+crossedCannibals, not self.westBank.boat),\
            self)
    
    def checkParents(self, parent):
        if parent == None:
            return True
        if self == parent:
            return False
        return self.checkParents(parent.parent)
    
    
    def getSolution(self, goal):
        if self == goal:
            print "GOAL FOUND"
            return self
        for child in self.spawnAllChildren():
            solution = child.getSolution(goal)
            if solution:
                return solution
        return None
    
    def printSolution(self):
        if self.parent:
            self.parent.printSolution()
        print self
        
class Missionaries:
    def __init__(self):
        self.initialState   =   state(bank("E",3,3,True),bank("W",0,0,False))
        self.finialState    =   state(bank("E",0,0,False),bank("W",3,3,True))
        
def chunks(lst, size):
    for i in xrange(0, len(lst), size):
        yield lst[i:i+size]


problem = tiles(3,3)