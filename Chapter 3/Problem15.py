#!/usr/bin/env python
#Problem 3.15
import random
from pprint import pprint

class Vertex:
    def __init__(self):
        self.x = 0
        self.y = 0
    
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
    
    def Same(self, other):
        print self, other
        if (self.x != other.x):
            return 0
        if (self.y != other.y):
            return 0
        return 1

    def Area(self, a, b):
        area = 0.5 * abs(self.x*(a.y-b.y) - self.y*(a.x-b.x) + (a.x*b.y-a.y*b.x))
        return area
        
    def InsideTriangle(self, a, b, c):
        TriArea = a.Area(b,c)
        a1 = self.Area(a,b)
        a2 = self.Area(b,c)
        a3 = self.Area(c,a)
        CumulativeArea = self.Area(a,b) + self.Area(b,c) + self.Area(c,a)
        
        print "\n", self, a, b, c
        print TriArea, a1, a2, a3, CumulativeArea
        Test = 0
        if (CumulativeArea<=TriArea):
            Test = 1
        return Test
    
        
class ConvexPolygon:
    def __init__(self):
        self.Vertices = []
        
    def Inside(self, a):
        print "\n\n New attempt ", a
        for i in range (1, len(self.Vertices)-1):
            print "Trying the triangle", i
            if (self.Vertices[0].InsideTriangle(self.Vertices[i], self.Vertices[i+1], a) == 1):
                print "Incribing triangle ", self.Vertices[0], self.Vertices[i], self.Vertices[i+1]
                return 1
        print "Not in Polygon"
        return 0
        
    def MakeConvex(self):
 # need to add code to check for cases with fewer than four vertices
        index = 0
        Hull = ConvexPolygon()
        for i in range (0, len(self.Vertices)):
            if (self.Vertices[i].x < self.Vertices[index].x):
                index = i
        Hull.Vertices.append(self.Vertices[index])
        del self.Vertices[index]
        
        index = 0
        for i in range (0, len(self.Vertices)):
            if (self.Vertices[i].y < self.Vertices[index].y):
                index = i
        Hull.Vertices.append(self.Vertices[index])
        del self.Vertices[index]
        
        index = 0
        for i in range (0, len(self.Vertices)):
            if (self.Vertices[i].x > self.Vertices[index].x):
                index = i
        Hull.Vertices.append(self.Vertices[index])
        del self.Vertices[index]
        
        index = 0
        for i in range (0, len(self.Vertices)):
            if (self.Vertices[i].y > self.Vertices[index].y):
                index = i
        Hull.Vertices.append(self.Vertices[index])
        del self.Vertices[index]
        
        print "vertices in Hull"
        for element in Hull.Vertices:
            print(element)
        for i in range(1, len(Hull.Vertices)):
            Bubble = Hull.Vertices[i]
            if (Hull.Vertices[0].Same(Bubble) == 1):
                del Hull.Vertices[i]
                break
        print "Length = ", len(self.Vertices)
        for i in range (len(self.Vertices)-1,-1,-1):
            if (Hull.Inside(self.Vertices[i]) == 1):
                print "Killed it ", self.Vertices[i]
                del self.Vertices[i]
            else:
                print "Outside ", self.Vertices[i]
# Need to check if there are any collinear cases
        
class Grid:
    def __init__(self):
        self.Area = []
        self.Height = 100
        self.Width  = 100
        self.Obstacles = []

    def SizeGrid(self, w, h):
        self.Height = h
        self.Width = w
        self.Area = [[0 for x in range(h)] for y in range(w)]
        
PlayGround = Grid()
PlayGround.SizeGrid(512, 512)
Barriers = ConvexPolygon()
for i in range(0,20):
    Point = Vertex()
    Point.x = random.randint(0, 20)
    Point.y = random.randint(0, 20)
    Barriers.Vertices.append(Point)
Barriers.MakeConvex()
print "left in Barriers"
for element in Barriers.Vertices:
    print(element)


