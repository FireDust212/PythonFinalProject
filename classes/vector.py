# Imports math
import math

# A vector class to help with vector math
class Vector():
    # Define the initialization
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Define what is printed when print(Vector instance) is called
    def __str__(self):
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
    