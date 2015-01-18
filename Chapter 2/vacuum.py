from Environment import Environment

class vacuum:
    #static variables
        
    #constructor
    def __init__(self, Environment = None):
        #class variables
        self.environment = Environment
        if not self.environment:
            self.environment = Environment()
        self.Moves = 0
        self.SuckUps = 0
        self.GoodSucks = 0
     
    def left(self):
        self.Moves += 1
        self.environment.MoveLeft()
        pass
    
    def right(self):
        self.Moves += 1
        self.environment.MoveRight()
        pass
    
    def suck(self):
        if (self.environment.CheckRoom()):
            self.GoodSucks += 1
        self.SuckUps += 1
        self.environment.Action("S")
        pass
    
    def NoOp(self):
        pass