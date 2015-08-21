import sys
import xml.etree.ElementTree as ET
from pprint import pprint
from PyQt4 import QtGui, QtCore
from ConvexHull import Point, Hull
import copy


def get_pixel_color(i_x, i_y):
	#import PyQt4.QtGui # python-qt4
	app = QtGui.QApplication([])
	long_qdesktop_id = QtGui.QApplication.desktop().winId()
	long_color = QtGui.QPixmap.grabWindow(long_qdesktop_id, i_x, i_y, 1, 1).toImage().pixel(0, 0)
	i_colour = int(long_color)
	return ((i_colour >> 16) & 0xff), ((i_colour >> 8) & 0xff), (i_colour & 0xff)

class	Segment(object):
	def __init__(self, startPoint=None, endPoint=None):
		self.start	= 	startPoint
		self.end	=	endPoint
	
	def __str__(self):
		return 'start: ' + str(self.start) +', end: ' + str(self.end)
	
	def drawSegment(self,qpainter,pen=None):
		qpainter.setPen(pen)
		qpainter.drawLine(self.start.x,self.start.y,self.end.x,self.end.y)
		
	@property
	def midpoint(self):
		return Point((self.start.x+self.end.x)/2, (self.start.y+self.end.y)/2)

class Solution(object):
	def __init__(self, startingPoint,target):
		self.points = [target]
		self.currentLoction = startingPoint
		self.target = target
		self.lstOfSegments = []
		
	def addSegment(self,endPoint):
		self.lstOfSegments.append(Segment(self.currentLoction,endPoint))
		self.currentLoction = endPoint
		self.points.append(endPoint)
		
	def __str__(self):
		return '\n'.join([str(x) for x in self.lstOfSegments])
	
	def __len__(self):
		return len(self.lstOfSegments)
	
	#def __getattr__(self,index):
	#	if index in range(len(self.lstOfSegments)):
	#		return self.lstOfSegments[index]
	
	def solved(self):
		if self.currentLoction == self.target:
			return True
		return False
	
	def draw(self,qpainter, pen=None):
		for i in range(len(self.lstOfSegments)):
			self.lstOfSegments[i].drawSegment(qpainter,pen)
	


class Shape(object):
	def __init__(self, node):
		self.points = []
		self.hull = None
		
		for child in node:
			self.points.append(ShapeRunner.getPoint(child))
			
		self.hull = Hull(copy.deepcopy(self.points))
				
	def drawShape(self,qpainter,pen=None):
		if not pen:
			pen = QtGui.QPen(QtCore.Qt.black, 3, QtCore.Qt.SolidLine)
		
		qpainter.setPen(pen)
		
		for index in range(0,len(self.points),1):
			startPoint  =   self.points[index]
			endPoint    =   self.points[(index+1)%len(self.points)]
			qpainter.drawLine(startPoint.x,startPoint.y,endPoint.x,endPoint.y)

class ShapeRunner(QtGui.QWidget):
	def __init__(self,XMLMap=None,app=None):
		super(ShapeRunner,self).__init__()
		self.grabPixel = False
		if  app:
			self.long_qdesktop_id = QtGui.QApplication.desktop().winId()
			self.grabPixel = True
		
		self.mapSource  =   XMLMap
		self.name       =   ""
		self.shapes     =   []
		self.size       =   (300,500)
		self.start      =   None
		self.target     =   None
		
		self.initMap(self.mapSource)
		self
		self.initUI()
		
		self.solutions = []
		self.my_solution	=	None
		self.solution_counter = 0

	def initUI(self):
		
		self.setGeometry(40, 40, self.size[0], self.size[1] )
		self.setWindowTitle(str(self.__class__.__name__) + ": " + self.name)
		self.setWindowIcon(QtGui.QIcon('web.png'))        
	
		self.show()
		
	def initMap(self, XMLMap):
		tree = None
		root = None
		print("Map Name",XMLMap)
		if self.mapSource:
			tree = ET.parse(XMLMap)
			root = tree.getroot()
			self.name = str(root.get("title"))
		
		for child in root:
			if child.tag == "shape":
				self.shapes.append(Shape(child))
			elif child.tag == "size":
				self.getMapSize(child)
			elif child.tag == "start":
				self.start  =   self.getPoint(child)
			elif child.tag == "target":
				self.target =   self.getPoint(child)
	
		
	def paintEvent(self,e):
		qpainter = QtGui.QPainter()
		qpainter.begin(self)
		self.DrawMap(qpainter)
		self.DrawStart(qpainter)
		self.DrawTarget(qpainter)
		
		if len(self.my_solution):
			self.DrawSolution(qpainter)
		
		
		#if self.grabPixel:
		#	long_color = QtGui.QPixmap.grabWindow(self.long_qdesktop_id, self.start.x, self.start.y, 1, 1).toImage().pixel(0, 0)
		#	i_colour = int(long_color)
		qpainter.end()
	
	def DrawMap(self,qpainter):
		for item in self.shapes:
			item.drawShape(qpainter)
			
	def getMapSize(self,node):
		for child in node:
			if str(child.tag) == "height":
				self.size = (self.size[0],int(str(child.text)))
			elif str(child.tag) == "width":
				self.size = (int(str(child.text)),self.size[1])
	@staticmethod		
	def getPoint( node):
		retVar = None
		if node.tag == "point":
			xy = str(node.text).split(",")
			retVar =  Point(int(xy[0]),int(xy[1]))
			return retVar
		else:
			for child in node:
					xy = str(child.text).split(",")
					retVar =  Point(int(xy[0]),int(xy[1]))
			return retVar
	
	def DrawStart(self,qpainter):
		pen = QtGui.QPen(QtCore.Qt.blue,10)
		self.DrawPoint(qpainter,pen,self.start)
		
	def DrawTarget(self,qpainter):
		pen = QtGui.QPen(QtCore.Qt.red,10)
		self.DrawPoint(qpainter,pen,self.target)
		
	def DrawPoint(self,qpainter, pen, point):
		qpainter.setPen(pen)
		qpainter.drawPoint(point.x, point.y)
		
	def DrawSolution(self,qpainter):
		pen = QtGui.QPen(QtCore.Qt.green, 7, QtCore.Qt.SolidLine)
		self.my_solution.draw(qpainter,pen)
		
	def RunShape(self,solution):
		if not solution.solved():
			blockingShapes = self.getBlockingShapes(solution.currentLoction)
			if len(blockingShapes) == 0:
				solution.addSegment(self.target)
				self.set_solution(solution)
				return
			nextPoints = []
			for shape in self.shapes:
				for point in shape.points:
					if (solution.currentLoction != point) and (point not in solution.points):
						temp  = self.getBlockingShapes(solution.currentLoction,point)
						temp_seg = Segment(solution.currentLoction,point)
						crossing = shape.hull.InsideHull(temp_seg.midpoint)
						if len(temp) == 0 and not crossing:
							nextPoints.append(point)

			
			for point in nextPoints:
				newSolution = copy.deepcopy(solution)
				newSolution.addSegment(point)
				self.RunShape(newSolution)

	
	def getBlockingShapes(self,currentPoint, target=None):
		retLst = []
		
		if not target:
			target = self.target
		#print target
		for shape in self.shapes:
			if shape.hull.LineIntersection(currentPoint,target):
				retLst.append(shape)
		
		return retLst
		
	
	def Run(self):
		self.solutions = []
		solution = Solution(self.start,self.target)
		self.RunShape(solution)
		
	def set_solution(self, new_solution):
		if self.my_solution == None:
			self.my_solution = copy.deepcopy(new_solution)
		else:
			if len(new_solution) < len(self.my_solution):
				self.my_solution = copy.deepcopy(new_solution)
				

def main():
	app = QtGui.QApplication(sys.argv)
	ex = ShapeRunner("Maps\TwoHull.xml",app)
	ex.Run()
	for seg in ex.my_solution.lstOfSegments:
		print(seg)
	print(len(ex.my_solution))
	
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()    