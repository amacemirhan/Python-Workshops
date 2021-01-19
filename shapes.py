# -*- coding: utf-8 -*-
"""
Module containing two classes: Point3 and Rectangle.

Author: Walker M. White (wmw2), Anne Bracy (awb93)
Date:   Feb 14, 2018
"""

 
class Point3():
    """
    An instance is a point in 3D space.
    
    to create a 3D point, type:
    p1 = shapes.Point3(1,2,3)

    """
    
    def __init__(self, x, y, z):
        """
        Creates a new Point with the given coordinates.
        """
        self.x = x
        self.y = y
        self.z = z

    def greet(self):
        """
        Prints a greeting that tells the location of the point.
        """
        print("Hi! I am a 3-dimensional point located at ("+str(self.x)+","+str(self.y)+","+str(self.z)+")")

class Rectangle():
    """
    An instance is a rectangle in 2D space.

    """
    
    # BUILT_IN METHODS
    def __init__(self, left, bottom, right, top):
        """
        Creates a new Rectangle with the given coordinates.
        """
        self.left = left
        self.bottom = bottom
        self.right = right
        self.top = top
        
    def greet(self):
        """
        Prints a greeting that tells the bottom left corner of the rectangle.
        """
        print("Hi, I am a rectangle. My bottom left corner is located at ("+str(self.left)+","+str(self.bottom)+")")
        
