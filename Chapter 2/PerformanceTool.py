import vacuum
import Environment

class PerformanceTool:
    def __init__(self):
        self.HowGood = 0.0
        self.Ticks = 0
        self.Space = Environment.Environment()
        self.Hoover = vacuum.vacuum(self.Space)    
    def Measure1(self):
        HowGood = (self.Hoover.GoodSucks / self.Hoover.SuckUps + exp(10.0 *(-self.Hoover.Moves / self.Ticks))) / 2
        pass 


#this a comment
#this is a bad line
