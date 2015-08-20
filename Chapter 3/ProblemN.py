from PIL import Image
from pprint import pprint

startingColor   =   (255,0,0)
targetColor     =   (0,0,255)

currentLocation =   (0,0)
endLocation     =   (0,0)

initalMap = "Map2.png"

im = Image.open(initalMap)

bigMap = {}

class shape:
    def __init__(self):
        self.points = []
    
    def addPoint(self, x,y):
        if (x,y) not in self.points:
            self.points.add((x,y))


shapeMap = {}



def SetValue(row, col, value):
    if not bigMap.has_key(col):
        bigMap[col] = {}
    bigMap[col][row] = value

def getPoints(img):
    imageSize = img.size
    start   =   None
    target  =   None
    for col in range(0, imageSize[1],1):
        for row in range(0, imageSize[0],1):
            if im.getpixel((row,col)) == startingColor:
                start   =   (row,col)
                #print "found start"
            if im.getpixel((row,col))== targetColor:
                target  =   (row,col)
                #print "found target"
            if(start and target):
                return(start,target)   
    
    
start = getPoints(im)

#print im.getpixel((44,228))
pprint(start)