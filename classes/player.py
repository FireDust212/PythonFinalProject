import pygame
from classes.hitbox import Hitbox

# Constants
PLAYER_HEIGHT, PLAYER_WIDTH = 50, 50
PLAYER_VEL = 5

# Declare the class - extends the pygame.Rect class, giving us some pre-declared functions
class Player(Hitbox):

    # Define the initialization function (called when a new object of the class is created)
    def __init__(self, window, x, y, currentHealth, maxHealth, weapons):
        # Call the parent class's initialization function
        super().__init__(window, x, y, PLAYER_WIDTH, PLAYER_HEIGHT, "blue")

        # Set our current and max health
        self.currentHealth = currentHealth
        self.maxHealth = maxHealth

        # Set player's weapons
        self.weapons = weapons
    
    # Define string representation for player
    def __str__(self):
        return f"This player has position (x,y) of: ({self.x}, {self.y}). It has {self.currentHealth} out of {self.maxHealth}"
    
    # Define representation for player
    def __repr__(self):
        return f"Player: x:{self.x}, y:{self.y}, currentHealth: {self.currentHealth}, maxHealth: {self.maxHealth}"
    

    # Add weapons to the player
    def addWeapon(self, weapon):
        self.weapons.append(weapon)

    # Player draw function - adds a healthbar
    def draw(self):
        pygame.draw.rect(self.window, self.color, (self.x, self.y, self.width, self.height))
        if self.currentHealth < self.maxHealth:
            pygame.draw.rect(self.window, "grey", (self.x - (self.width/10), self.y - (self.height/5), self.width + (self.width/5), (self.height/10)))
            pygame.draw.rect(self.window, "green", (self.x - (self.width/10), self.y - (self.height/5), (self.currentHealth / self.maxHealth) * (self.width + (self.width/5)), (self.height/10)))