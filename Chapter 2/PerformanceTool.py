import vacuum
import Environment
import math

class PerformanceTool:
    def __init__(self):
        self.HowGood = 0.0
        self.Ticks = 0
        self.HowLong = 100
        self.Space = Environment.Environment()
        self.Hoover = vacuum.vacuum(self.Space)    
    def Measure1(self):
        self.HowGood = (self.Hoover.GoodSucks / self.Hoover.SuckUps + math.exp(10.0 *(-self.Hoover.Moves / self.Ticks))) / 2
        print(self.HowGood)
        print(self.Hoover.GoodSucks,  self.Hoover.SuckUps,  self.Hoover.Moves,  self.Ticks)
        pass 

    def Run(self):
        for i in range(0,self.HowLong,1):
            self.Hoover.ReflexAction()
            self.Space.RandomDirty()
            self.Ticks += 1
        self.Measure1()
        
pTool = PerformanceTool()
pTool.Run()
#this a comment
#this is a bad line
