import pygame
from classes.vector import Vector

# Declare the class - extends the pygame.Rect class, giving us some pre-declared functions
class Hitbox(pygame.Rect):

    # Define the initialization function (called when a new object of the class is created)
    def __init__(self, window, x, y, width, height, color):
        # Call the parent class's initialization function
        super().__init__(x, y, width, height)

        # Set up other attributes
        self.color = color
        self.window = window
        
        # Bool to track if the hitbox should be deleted
        self.deleteMe = False
    
    # Define string representation for hitbox
    def __str__(self):
        return f"This hitbox has position (x,y) of: ({self.x}, {self.y}). It is colored {self.color} on the window {self.window}"
    
    # Define representation for hitbox
    def __repr__(self):
        return f"Hitbox: x:{self.x}, y:{self.y}, color: {self.color}, window: {self.window}"
    
    # Define a movement function, moves the hitbox towards a target using vector math
    # Also takes a velocity, and a list of other hitboxes to not run into
    def moveTowards(self, target, velocity, hitboxes):
        # Define a vector from the position of the hitbox to the position of the target
        direction = Vector(self.x - target.x, self.y - target.y)
        
        # Get the unit vector in the direction the hitbox will move
        move = direction.getUnitVector()

        # Only move if the move vector exists
        if move != None:
            # Scale up the move vector by the velocity
            move.scaleBy(velocity)

            # NOTE - The move vector will be rounded from here on, preventing some movement issues
            
            # Check to see if the hitboxes will collide
            # Set up a false hitbox for the hitbox's next position
            nextPos = pygame.Rect(self.x, self.y, self.width, self.height)
            nextPos.x -= round(move.x)
            nextPos.y -= round(move.y)

            # Bool for collision
            hit = False

            # Check for collision
            for box in hitboxes:
                if box.colliderect(nextPos):
                    hit = True
                    break
            
            # Move this hitbox if it will not collide
            if hit == False:
                self.x -= round(move.x)
                self.y -= round(move.y)
        # If movement vector does not exist, hitbox is at target
        # Call self.hitTarget(), which can be implemented by classes extenging hitbox
        else:
            self.hitTarget()
    
    # Hit target function called when the hitbox reaches a target in the move funtion
    # this will be used by classes that extend hitbox.
    def hitTarget(self):
        pass

    def draw(self):
        pygame.draw.rect(self.window, self.color, (self.x, self.y, self.width, self.height))