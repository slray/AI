import pprint

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
        self.postion = 0
        self.ResizeRoom(size)
        self.actions = {"L":self.MoveLeft,"R":self.MoveRight,"S":self.Clean, "N":self.Nothing}
        
    def Nothing(self):
        print "Doing Noithing"
        pass
    
    def Clean(self):
        print "Cleaning"
        self.room[self.postion].SetClean()

    def MoveLeft(self):
        print "Moving Left"
        return self.Move(-1)
    
    def MoveRight(self):
        print "Moving Right"
        return self.Move(1)

    def Move(self, step):
        if (self.postion + step) in range(0,len(self.room),1):
            self.postion += step
            return True
        return False
    
    def RecieveActions(self, actions):
        retVars = []
        for action in actions:
            retVars.append(self.RecieveAction(action))
        return retVars
    
    def RecieveAction(self, action):
        if self.actions.has_key(action):
            return self.actions[action]()
    
    def ResizeRoom(self, size):
        self.postion = 0
        self.room = []
        for i in range(0,size,1):
            self.room.append(Tile(i))
    
    def PrintRooms(self):
        for tile in self.room:
            print tile
            
    def DirtyRoom(self, postion=None):
        if not postion:
            postion = self.postion
        self.room[postion].SetDirty()


## test Sequence
env = Environment(2)
env.DirtyRoom(1)
env.PrintRooms()
l = 'L'
r = "R"
s = "S"
n= "N"
testPercepts = [l,r,s,n]
testPerceptSequence = [l,r,r,s,l,l]
env.RecieveAction(r)
results = env.RecieveActions(testPerceptSequence)
pprint.pprint(results)

env.PrintRooms()
    
