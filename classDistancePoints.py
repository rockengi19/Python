# -*- coding: utf-8 -*-

"""
This Python code uses a class to calculate the distance between two points
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
        return ((self.x**2)+(self.y**2))**0.5
    
    def distanceFromPoint(self,otherP):
        dx = (otherP.getX() - self.x)
        dy = (otherP.getY() - self.y)
        return math.sqrt(dy**2 + dx**2)
    
p = Point(3,3)
q = Point(6,7)

print("The distance between p and q is",p.distanceFromPoint(q),"cm")
