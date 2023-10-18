from classes.weaponHB import WeaponHB

# Class for projectile weapon hitboxes
class Projectile(WeaponHB):
    def __init__(self, window, x, y, width, height, color, target, speed):
        super().__init__(window, x, y, width, height, color)
        self.isProjectile = True
        self.target = target
        self.speed = speed

    # Movement function
    def move(self):
        super().moveTowards(self.target, self.speed, [])
    
    # Implement the hitbox's unused hit target funtion
    # When this reaches its target, tell the client to dispose of it
    def hitTarget(self):
        self.deleteMe = True