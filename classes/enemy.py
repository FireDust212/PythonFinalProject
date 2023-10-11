import pygame
import math

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

    # Define a movement function, moves the enemy towards a target using vector math
    # Also takes a list of the other enemies
    def moveTowards(self, target, enemies):
        # Define a vector from the position of the enemy to the position of the target
        movementVector = {"x":self.x - target.x, "y":self.y - target.y}
        
        # Take the magnitude of the movement vector (Used to find the unit vector in the same direction)
        vectorMagnitude = math.sqrt((movementVector['x'] ** 2) + (movementVector['y'] ** 2))
        if vectorMagnitude == 0:
            vectorMagnitude = 1
        
        # Add the components of the unit vector in the direction of the movement vector to the enemy's position
        # These components are scaled up by the enemy's velocity (ENEMY_VEL)
        move = {'x': round((movementVector['x'] * ENEMY_VEL) / vectorMagnitude),"y": round((movementVector['y'] * ENEMY_VEL) / vectorMagnitude)}
        
        # Check to see if the enemies will collide
        # Set up a false hitbox for the enemy's next position
        nextPos = pygame.Rect(self.x, self.y, ENEMY_WIDTH, ENEMY_HEIGHT)
        nextPos.x -= move["x"]
        nextPos.y -= move['y']

        hit = False

        for en in enemies:
            if en.colliderect(nextPos):
                hit = True
        
        if hit == False:
            self.x -= move["x"]
            self.y -= move['y']