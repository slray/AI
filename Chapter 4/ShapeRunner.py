import sys
import xml.etree.ElementTree as ET
from pprint import pprint
from PyQt4 import QtGui, QtCore

def get_pixel_color(i_x, i_y):
	#import PyQt4.QtGui # python-qt4
	app = QtGui.QApplication([])
	long_qdesktop_id = QtGui.QApplication.desktop().winId()
	long_color = QtGui.QPixmap.grabWindow(long_qdesktop_id, i_x, i_y, 1, 1).toImage().pixel(0, 0)
	i_colour = int(long_color)
	return ((i_colour >> 16) & 0xff), ((i_colour >> 8) & 0xff), (i_colour & 0xff)

class Point(object):
    def __init__(self,node):        
        if node.tag == "point":
            xy = str(node.text).split(",")
            self.x = int(xy[0])
            self.y = int(xy[1])
        self.point=(self.x,self.y)
        
    def __str__(self):
        return "x={0} y={1}".format(self.x, self.y)
        

class Shape(object):
    def __init__(self, node):
        self.points = []
        
        for child in node:
            self.points.append(Point(child))
                
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
        self.initUI()
        

    def initUI(self):
        
        self.setGeometry(40, 40, self.size[0], self.size[1] )
        self.setWindowTitle(str(self.__class__.__name__) + ": " + self.name)
        self.setWindowIcon(QtGui.QIcon('web.png'))        
    
        self.show()
        
    def initMap(self, XMLMap):
        tree = None
        root = None
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
        #print get_pixel_color(self.target.x, self.target.y)
        
        if self.grabPixel:
            long_color = QtGui.QPixmap.grabWindow(self.long_qdesktop_id, self.start.x, self.start.y, 1, 1).toImage().pixel(0, 0)
            i_colour = int(long_color)
            print ((i_colour >> 16) & 0xff), ((i_colour >> 8) & 0xff), (i_colour & 0xff)
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
                
    def getPoint(self, node):
        retVar = None
        for child in node:
            if str(child.tag) == "point":
                retVar =   Point(child)
        return retVar
    
    def DrawStart(self,qpainter):
        pen = QtGui.QPen(QtCore.Qt.blue)
        self.DrawPoint(qpainter,pen,self.start)
        
    def DrawTarget(self,qpainter):
        pen = QtGui.QPen(QtCore.Qt.red)
        self.DrawPoint(qpainter,pen,self.target)
        
    def DrawPoint(self,qpainter, pen, point):
        qpainter.setPen(pen)
        qpainter.drawPoint(point.x, point.y) 
    
        
    

def main():
    app = QtGui.QApplication(sys.argv)
    ex = ShapeRunner("Maps\One.xml",app)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()    