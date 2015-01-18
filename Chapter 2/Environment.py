import pprint
import random

class Tile :
    def  __init__(self, Location):
        self.location = Location
        self.clean = True
    
    def __str__(self):
        return "Tile: "+str(self.location)+" Clean: "+str(self.clean)
        
    def SetClean(self):
        self.clean = True
        
    def SetDirty(self):
        self.clean = False
        
    def isDirty(self):
        return not self.clean
    
class Environment:
    def __init__ (self, size = 2):
        self.position = 0
        self.ResizeRoom(size)
        self.actions = {"L":self.MoveLeft,"R":self.MoveRight,"S":self.Clean, "N":self.Nothing,"C":self.CheckRoom}
        
    def Nothing(self):
        print "Doing Nothing"
        pass
    
    def Clean(self):
        print "Cleaning"
        self.room[self.position].SetClean()

    def MoveLeft(self):
        print "Moving Left"
        return self.Move(-1)
    
    def MoveRight(self):
        print "Moving Right"
        return self.Move(1)
        
    def CheckRoom(self):
        "Checking Room"
        return self.room[self.position].isDirty()

    def Move(self, step):
        if (self.position + step) in range(0,len(self.room),1):
            self.position += step
            return True
        return False
    
    def ReceiveActions(self, actions):
        retVars = []
        for action in actions:
            retVars.append(self.Action(action))
        return retVars
    
    def Action(self, action):
        if self.actions.has_key(action):
            return self.actions[action]()
    
    def ResizeRoom(self, size):
        self.position = random.randint(0, size-1)
        self.room = []
        for i in range(0,size,1):
            self.room.append(Tile(i))
    
    def PrintRooms(self):
        for tile in self.room:
            print tile
            
    def DirtyRoom(self, position=None):
        if not position:
            position = self.position
        self.room[position].SetDirty()
    
    def RandomDirty(self):
        for tile in self.room:
            if random.randint(1,100) < 5: tile.SetDirty()
        


## test Sequence

def test(): 
    env = Environment(2)
    env.DirtyRoom(1)
    env.PrintRooms()
    l = 'L'
    r = "R"
    s = "S"
    n = "N"
    c = "C"
    testPercepts = [l,r,s,n,c]
    testPerceptSequence = [l,r,r,s,l,l]
    env.Action(r)
    results = env.ReceiveActions(testPerceptSequence)
    pprint.pprint(results)
    env.RandomDirty()
    env.PrintRooms()
    
