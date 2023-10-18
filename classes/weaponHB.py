from classes.hitbox import Hitbox

# Class for weapon hitboxes
class WeaponHB(Hitbox):
    def __init__(self, window, x, y, width, height, color):
        super().__init__(window, x, y, width, height, color)
        self.isProjectile = False