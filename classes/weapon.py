# from classes.weaponHitboxFrame import WeaponHitBoxFrame
from classes.projectile import Projectile
from classes.weaponHB import WeaponHB

# Weapon class, contains a list of weapon hitboxes
class Weapon():
    def __init__(self, window, color, hitboxSetup, damage, player):
        # Window to draw this weapon on
        self.window = window

        # Color of this weapon's hitboxes
        self.color = color

        # The damage this weapon does
        self.damage = damage

        # Seting up this weapon's hitboxes
        self.hitboxes = []
        self.hitboxSetup = hitboxSetup  # Used to create new hitboxes

        # The player this weapon should base its x and y values on
        self.player = player
        
    # Class called every tick:
    #   -   Remove old hitboxes
    #   -   Add active hitboxes
    #   -   Move projectiles
    def update(self, tick):
        # Remove old non-projectile hitboxes (loop though a copy) and projectiles that have hit their target
        for hitBox in self.hitboxes[:]:
            if hitBox.isProjectile == False:
                self.hitboxes.remove(hitBox)
            else:
                if hitBox.deleteMe:
                    self.hitboxes.remove(hitBox)

        # Loop though the weapon's hitboxSetup, checking for hitboxes to activate 
        for setup in self.hitboxSetup:
            # Make hitboxes if it is time to do so
            if setup.isActive(tick):
                # Make projectiles
                if setup.isProjectile:
                    self.hitboxes.append(Projectile(self.window, self.player.x + setup.x, self.player.y + setup.y, setup.width, setup.height, self.color, setup.target, setup.speed))
                # Make other hitboxes
                else:
                    self.hitboxes.append(WeaponHB(self.window, self.player.x + setup.x, self.player.y + setup.y, setup.width, setup.height, self.color))
        
        # Move projectiles
        for hitbox in self.hitboxes:
            if hitbox.isProjectile:
                hitbox.move()
