from classes.hitbox import Hitbox

# Constants
ENEMY_HEIGHT, ENEMY_WIDTH = 35, 35
ENEMY_VEL = 1
ENEMY_DAMAGE = 10

# Declare the class - extends the pygame.Rect class, giving us some pre-declared functions
class Enemy(Hitbox):

    # Define the initialization function (called when a new object of the class is created)
    def __init__(self, window, x, y, currentHealth, maxHealth):
        # Call the parent class's initialization function
        Hitbox.__init__(self, window, x, y, ENEMY_WIDTH, ENEMY_HEIGHT, "red")

        # Set our current and max health
        self.currentHealth = currentHealth
        self.maxHealth = maxHealth

    # Define string representation for enemies
    def __str__(self):
        return f"This enemy has position (x,y) of: ({self.x}, {self.y}). It has {self.currentHealth} out of {self.maxHealth}"
    
    # Define representation for enemies
    def __repr__(self):
        return f"Enemy: x:{self.x}, y:{self.y}, currentHealth: {self.currentHealth}, maxHealth: {self.maxHealth}"
