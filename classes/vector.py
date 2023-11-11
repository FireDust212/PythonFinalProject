# Imports math
import math

# A vector class to help with vector math
class Vector():
    # Define the initialization
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Define string representation for vectors
    def __str__(self):
        return f"This Vector has x of: {self.x}, and y of: {self.y}"
    
    # Define representation for Vectors
    def __repr__(self):
        return f"Vector: x:{self.x}, y:{self.y}"
    
    # Define a scaling function
    def scaleBy(self, scalor):
        self.x = self.x * scalor
        self.y = self.y * scalor
    
    # Define gettor for magnitute of vector
    def getMagnitude(self):
        return math.sqrt((self.x ** 2) + (self.y ** 2))
    
    # Define getter for unit vector in direction of this vector
    def getUnitVector(self):
        magn = self.getMagnitude()
        if magn == 0:
            return None
        else:
            unitV = Vector(self.x/magn, self.y/magn)
            return unitV
    
    # Distance to another vector
    def distTo(self, target):
        return math.sqrt(abs((self.x-target.x)**2 + (self.y-target.y)**2))