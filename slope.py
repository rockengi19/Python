# -*- coding: utf-8 -*-

"""
This Python code calculates the slope of a line which is between the origin
of the axes and a point
"""

import math

class Point:
    def __init__(self,initX,initY):
        self.x = initX
        self.y = initY
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return((self.x**2)+(self.y**2))**0.5
        
    def distanceFromPoint(self,otherP):
        dx = (otherP.getX() - self.x)
        dy = (otherP.getY() - self.y)
        return math.sqrt(dy**2 + dx**2)
    
    def slopeFromOrigin(self):
        px = self.x
        py = self.y
        if self.x == 0:
            return None
        else:
            return py/px
        
b = Point(6,14)
print("The slope of the line is",round(b.slopeFromOrigin(),3),"cm")
