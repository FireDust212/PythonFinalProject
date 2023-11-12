import pygame
from classes.hitbox import Hitbox
from classes.levelUpOption import LevelUpOption

# Constants
PLAYER_HEIGHT, PLAYER_WIDTH = 50, 50
PLAYER_VEL = 5

# Declare the class - extends the pygame.Rect class, giving us some pre-declared functions
class Player(Hitbox):

    # Define the initialization function (called when a new object of the class is created)
    def __init__(self, window, x, y, currentHealth, maxHealth, weapons):
        # Call the parent class's initialization function
        super().__init__(window, x, y, PLAYER_WIDTH, PLAYER_HEIGHT, "blue")

        # Set our current and max health, and health regen
        self.currentHealth = currentHealth
        self.maxHealth = maxHealth
        self.regen = 5/60

        # Set player's weapons
        self.weapons = weapons

        # Set player level to 0
        self.level = 0
    
    # Define string representation for player
    def __str__(self):
        return f"This player has position (x,y) of: ({self.x}, {self.y}). It has {self.currentHealth} out of {self.maxHealth}"
    
    # Define representation for player
    def __repr__(self):
        return f"Player: x:{self.x}, y:{self.y}, currentHealth: {self.currentHealth}, maxHealth: {self.maxHealth}"
    

    # Add weapons to the player
    def addWeapon(self, weapon):
        self.weapons.append(weapon)
    
    # Player update function
    def update(self, tick):
        super().update(tick)
        if self.currentHealth < self.maxHealth: self.currentHealth += self.regen

    # Player draw function - adds a healthbar
    def draw(self):
        pygame.draw.rect(self.window, self.color, (self.x, self.y, self.width, self.height))
        if self.currentHealth < self.maxHealth:
            pygame.draw.rect(self.window, "grey", (self.x - 5, self.y - 5, self.width + 10, 5))
            pygame.draw.rect(self.window, "green", (self.x - 5, self.y - 5, (self.currentHealth / self.maxHealth) * (self.width + 10), 5))


    # Get next level function: returns a levelUpOption
    def getNextLevel(self):
        return LevelUpOption(self.window, 'Player', self.level+1, ["Heal 10% HP","HP +10", "Regen/second +1", "All Weapon Damage +10%"],self)
    
    # Level Up player
    def levelUp(self):
        self.currentHealth += .1*self.maxHealth
        self.regen = (self.regen*60 + 1) / 60
        self.maxHealth += 10

        for weapon in self.weapons:
            weapon.damage *= 1.1
        
        self.level += 1
