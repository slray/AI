#!/usr/bin/env python
#Problem 3.15
import random


class Vertex:
    def __init__(self):
        self.x = 0
        self.y = 0
        
class ConvexPolygon:
    def __init__(self):
        self.Vertices = []
        self.HowManyVertices = 0
        
    def MakeConvex(self):
 # need to add code to check for cases with fewer than four vertices
        lowindex = 0
        highindex = 0
        rightindex = 0
        leftindex = 0
        for i in range (1, self.HowManyVertices):
            print self.Vertices[i]
            if (self.Vertices[i].x < self.Vertices[lowindex].x):
                lowindex = i
            if (self.Vertices[i].x > self.Vertices[highindex].x):
                highindex = i
            if (self.Vertices[i].y < self.Vertices[leftindex].y):
                leftindex = i
            if (self.Vertices[i].y > self.Vertices[rightindex].y):
                rightindex = i
            print i, ": ", lowindex, highindex, leftindex, rightindex
        Hull = ConvexPolygon()
        Hull.Vertices.append(self.Vertices[highindex])
        Hull.Vertices.append(self.Vertices[leftindex])
        Hull.Vertices.append(self.Vertices[lowindex])
        Hull.Vertices.append(self.Vertices[rightindex])
        Hull.HowManyVertices = 4
        print Hull.Vertices
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
Point = Vertex()
for i in range(0,10):
    Point.x = random.randint(10, 100)
    Point.y = random.randint(120, 130)
    print Point.x, Point.y
    Barriers.Vertices.append(Point)
Barriers.HowManyVertices = 10
Barriers.MakeConvex()


