from PIL import Image


size = 256,256

pointA = 50,89

pointB = 224,36

im = Image.new("RGB",size,"white")

black   =   (0,0,0)
blue    =   (0,0,255)
red      =      (255,0,0)
green =     (0,255,0)


def drawLine(im, pointA, pointB):
    
    line = Line(pointA,pointB)
    for index in range(pointA[0],pointB[0],1):
        y = int(line.getValue(index))
        im.putpixel((index,y),blue)
        
        
        
class Trapazoid():
    def __init__(self):
        self.vetrexs = []
        self.center = 0,0
        
    def addVertex(self, vertex):
        if vertex not in self.vetrexs:
            self.vetrexs.append(vertex)
            
    def addVertexs(self, vetrexs):
        for vertex in vetrexs:
            self.addVertex(vertex)
        self.getCenter()
            
    def drawShape(self, im):
        for index in range(0,len(self.vetrexs),1):
            line = Line(self.vetrexs[index],self.vetrexs[(index+1)%len(self.vetrexs)])
            print line
            line.Draw(im)
            
        im.putpixel(self.center,black)
            
    def getCenter(self):
        sumX  = 0
        sumY =  0
        for vertex in self.vetrexs:
            sumX += vertex[0]
            sumY += vertex[1]
        self.center = int(sumX/len(self.vetrexs)),int(sumY/len(self.vetrexs))
            
class Line:
    #y= mx+b
    def __init__(self, pointA=None, pointB=None):
        self.pointA = pointA
        self.pointB = pointB
        self.m = None
        self.b = None
        
        if (pointA and pointB):
            self.getLine(pointA,pointB)
        
    def getLine(self, pointA, pointB ):
        try:
            self.m  =   float((pointA[1]-pointB[1]))/float(((pointA[0])-pointB[0]))
        except:
            self.m = 99999999999999999
        self.b  =   pointA[1]+(float((self.m*-1)*pointA[0]))
        
    def __str__(self):
        return "Line  y=mx+b m: "+ str(self.m) +" b: " + str(self.b)
    
    def getValue(self,x):
        return (self.m * x) + self.b
    
    def getX(self,y):
        try:
            return (y-self.b)/self.m
        except:
            return None
    
    def Draw(self,im):
        left = self.pointA[0]
        right = self.pointB[0]
        if left > right:
            left = right
            right = self.pointA[0]
            
        top = self.pointA[1]
        bottom = self.pointB[1]
        if top > bottom:
           top = bottom
           bottom = self.pointA[1]
        
        #print  "left",left,"right",right,"top",top,"bottom",bottom
            
        #print "draw X"
        
        for index in range(left,right,1):
            y = (self.getValue(index))
            #print "X",index,"Y",y
            if y != None:
                im.putpixel((index,int(y)),green)
        
        #print "draw Y"
        for index in range(top,bottom,1):
            x = (self.getX(index))
            if x != None:
                im.putpixel((int(x),index),green)
    



#drawLine(im, pointA, pointB)
trap = Trapazoid()


cornerA     = 195,40
cornerB     = 195,195
cornerC     =  45,195
cornerD     =  45,40

trap.addVertexs([cornerA,cornerB,cornerC,cornerD ])
trap.drawShape(im)

im.save("test.png")