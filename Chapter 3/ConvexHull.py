import random
import copy
import math

class Hull:
	def __init__(self, lstOfPoints=None):
		self.Outline = []
		if lstOfPoints:
			self.Outline = lstOfPoints
	def __len__(self):
		return len(self.Outline)
	
	def get_point(self,index):
		#print type(index),index
		#print type(len(self)),len(self)
		#print(int(index)%len(self))
		
		return self.Outline[index%len(self)]
		
	def InsideHull(self, sample):
		
		for index in range(len(self)):
			#print index
			#print(self.get_point(index))
			#print(self.get_point(index+1))
			if sample.OnYourLeft(self.get_point(index), self.get_point(index+1)) == 0:
				return False
		return True
			
#			
#		return 
#		if len(self) < 3 : return 0
#		Crossings = 0
##        span = len(self.Outline)
#		PolyTemp = []
#		for i in range(len(self.Outline)):
#			PolyTemp.append(self.Outline[i].diff(sample))
#		for i in range(len(PolyTemp)-1):
#			if self.Outline[i].y * self.Outline[i+1].y <= 0:
#				Above = self.Outline[i].x * self.Outline[i+1].y - self.Outline[i].y*self.Outline[i+1].x
#				Below = self.Outline[i+1].x - self.Outline[i].y
#				if Above * Below > 0: Crossings = 1 - Crossings
#		return Crossings
	
	def Convex(self):
		GrahamList = []
		self.Outline.sort(cmp=Point.LowerRight)
#  print "Lower Right", self.Outline[0].x, self.Outline[0].y
		Anchor = copy.deepcopy(self.Outline[0])
		for i in range(len(self.Outline)):
			GrahamList.append(GrahamPoint(self.Outline[i], Anchor))
		GrahamList.sort(cmp=GrahamPoint.GrahamOrder)
		self.Outline = []
		self.Outline.append(GrahamList[len(GrahamList)-1].dot)
		self.Outline.append(GrahamList[0].dot)
		i=1
		while i < len(GrahamList):
			p1 = self.Outline[len(self.Outline)-2]
			p2 = self.Outline[len(self.Outline)-1]
			if p1.OnYourLeft(p2,GrahamList[i].dot):
			  self.Outline.append(GrahamList[i].dot)
			  i += 1
			else:
				if len(self.Outline) > 2:
#                   tail = len(self.Outline)-1
					self.Outline.pop()
				else: i += 1
#     self.Outline.append(GrahamList[i].dot)
		self.Outline.pop(0)
		
	def HullIntersection(self, other):
		for i in range(len(other.Outline)):
			iplus = (i+1)%len(other.Outline)
			for j in range(len(self.Outline)):
				jplus = (j+1)%len(self.Outline)
				if other.Outline[i].CrossedLines(other.Outline[iplus], self.Outline[i], self.Outline[iplus]) : return 1
		return 0
	
	def LineIntersection(self, pt1, pt2):
		for i in range(len(self.Outline)):
			iplus = (i+1)%len(self.Outline)
			if self.Outline[i].CrossedLines(self.Outline[iplus], pt1, pt2):
				return 1
		return 0    
		
class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def __str__(self):
		return "x={0} y={1}".format(self.x, self.y)
	
	def dist(self, other):
		span = Point(self.x - other.x, self.y - other.y)
		gap = math.sqrt(span.x*span.x + span.y*span.y)
		return gap
	
	def LowerRight(self, other):
		if self.y > other.y: return 1
		elif self.y < other.y: return -1
		if self.x < other.x: return 1
		elif self.x > other.x: return -1
		return 0
	
	def OnYourLeft(self, a, b):
		value = self.x * (a.y - b.y) + self.y * (b.x - a.x) + a.x*b.y - b.x*a.y
		if value > 0: return 1
		else: return 0
	
	def diff(self, a):
		return Point(a.x - self.x,a.y - self.y)
	
	def __eq__(self, other):
		if isinstance(other, Point):
			if (self.x == other.x) and (self.y == other.y):
				return True
		return False
			
	def CrossedLines(self, selfEnd, p1, p2):
		#if (self == p1) and (selfEnd == p2):
		#   return 0
		
		a = self.diff(selfEnd)
		b = p1.diff(p2)
		c = p2.diff(selfEnd)
		det = a.x*b.y - a.y*b.x
		if det == 0.0:    #lines are parallel
			#angle = (selfEnd.x-self.x)*(p1.x-self.x) + (selfEnd.y-self.y)*(p1.y-self.y)
			#try:
			#   angle /= math.sqrt((selfEnd.x-self.x)*(selfEnd.x-self.x) + (selfEnd.y-self.y)*(selfEnd.y-self.y))
			#   angle /= math.sqrt((p1.x-self.x)*(p1.x-self.x) + (p1.y-self.y)*(p1.y-self.y))
			#except:
			#   print "Divide by Zero"
			#   print "Self",self
			#   print "S1", selfEnd
			#   print "P1", p1
			#   print "P2", p2
			#if abs(angle) == 1.0: # collinear lines
			#   #if self.x == selfEnd.x:
			#   #   alpha = p1.x/(self.x-selfEnd.x)
			#   #else:
			#   #   alpha = p1.y / (self.y-selfEnd.y)
			#   #if alpha >= 0.0 and alpha <= 1.0:
			#   #   return 1
			#   #if self.x == selfEnd.x:
			#   #   beta = p2.x/(self.x-selfEnd.x)
			#   #else:
			#   #   beta = p1.y / (self.y-selfEnd.y)
			#   #if beta >= 0.0 and beta <= 1.0:
			#   #   return 1
			#   #if alpha*beta > 0:
			#   #   return 0
			#   #else: return 1
			#   return 1
			return 0. # parallel but not collinear, no intersection
		det = 1.0 / det
		m11 = b.y * det
		m12 = -b.x * det
		m21 = -a.y * det
		m22 = a.x * det
		alpha = m11 * c.x + m12 * c.y
		if alpha <= 0 or alpha >= 1.0: return 0
		beta = m21 * c.x + m22 * c.y
		beta *= -1.0
		if beta <= 0 or beta >= 1.0: return 0
		return 1            


class GrahamPoint:
	def __init__(self, point, anchor):
		self.dot = copy.deepcopy(point)
		self.sdist = point.dist(anchor)*point.dist(anchor)
		self.angle = math.atan2(point.y-anchor.y, point.x-anchor.x)
#      print point.x, point.y, anchor.x, anchor.y
	
	def GrahamOrder(self, other):
		if self.angle < other.angle: return -1
		elif self.angle > other.angle : return 1
		if self.sdist < other.sdist: return -1
		if self.sdist > other.sdist: return 1
		return 0
	
#Group = Hull()
#for i in range(10):
#   x = random.randint(-10,10)
#   y = random.randint(-10,10)
#   Group.Outline.insert(i,Point(x,y))
#print "Initial Points"
#for i in range(len(Group.Outline)):
#   print Group.Outline[i].x, Group.Outline[i].y
#print""
#Group.Convex()
#print "After Hull"
#for i in range(len(Group.Outline)):
#   print Group.Outline[i].x, Group.Outline[i].y


