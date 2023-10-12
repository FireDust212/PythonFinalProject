import pygame

# Constants
PLAYER_HEIGHT, PLAYER_WIDTH = 50, 50
PLAYER_VEL = 5

# Declare the class - extends the pygame.Rect class, giving us some pre-declared functions
class Player(pygame.Rect):

    # Define the initialization function (called when a new object of the class is created)
    def __init__(self, x, y, currentHealth, maxHealth):
        # Call the parent class's initialization function
        pygame.Rect.__init__(self, x, y, PLAYER_WIDTH, PLAYER_HEIGHT)

        # Set our current and max health
        self.currentHealth = currentHealth
        self.maxHealth = maxHealth
    
    # Define string representation for player
    def __str__(self):
        return f"This player has position (x,y) of: ({self.x}, {self.y}). It has {self.currentHealth} out of {self.maxHealth}"
    
    # Define representation for player
    def __repr__(self):
        return f"Player: x:{self.x}, y:{self.y}, currentHealth: {self.currentHealth}, maxHealth: {self.maxHealth}"