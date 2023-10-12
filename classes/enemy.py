import pygame
import math
from classes.vector import Vector

# Constants
ENEMY_HEIGHT, ENEMY_WIDTH = 35, 35
ENEMY_VEL = 1
ENEMY_DAMAGE = 10

# Declare the class - extends the pygame.Rect class, giving us some pre-declared functions
class Enemy(pygame.Rect):

    # Define the initialization function (called when a new object of the class is created)
    def __init__(self, x, y, currentHealth, maxHealth):
        # Call the parent class's initialization function
        pygame.Rect.__init__(self, x, y, ENEMY_WIDTH, ENEMY_HEIGHT)

        # Set our current and max health
        self.currentHealth = currentHealth
        self.maxHealth = maxHealth

    # Define string representation for enemies
    def __str__(self):
        return f"This enemy has position (x,y) of: ({self.x}, {self.y}). It has {self.currentHealth} out of {self.maxHealth}"
    
    # Define representation for enemies
    def __repr__(self):
        return f"Enemy: x:{self.x}, y:{self.y}, currentHealth: {self.currentHealth}, maxHealth: {self.maxHealth}"

    # Define a movement function, moves the enemy towards a target using vector math
    # Also takes a list of the other enemies
    def moveTowards(self, target, enemies):
        # Define a vector from the position of the enemy to the position of the target
        direction = Vector(self.x - target.x, self.y - target.y)
        
        # Get the unit vector in the direction the enemy will move
        move = direction.getUnitVector()

        # Only procede if the move vector exists
        if move != None:
            # Scale up the move vector by the velocity
            move.scaleBy(ENEMY_VEL)

            # NOTE - The move vector will be rounded from here on, preventing some movement issues
            
            # Check to see if the enemies will collide
            # Set up a false hitbox for the enemy's next position
            nextPos = pygame.Rect(self.x, self.y, ENEMY_WIDTH, ENEMY_HEIGHT)
            nextPos.x -= round(move.x)
            nextPos.y -= round(move.y)

            # Bool for collision
            hit = False

            # Check for collision
            for en in enemies:
                if en.colliderect(nextPos):
                    hit = True
                    break
            
            # Move this enemy if it will not collide with another
            if hit == False:
                self.x -= round(move.x)
                self.y -= round(move.y)