# This is a weaponHitbox class
# It is (will be) used by our weapon class to keep track of individual hitboxes of a weapon
class WeaponHitBoxFrame():
    # initialize
    def __init__(self, x, y, width, height, startTick, duration, isProjectile, targetKey, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        # Set up start tick: the tick multiples when the weaponHitbox will damage enemies
        self.startTick = startTick
        # Set up duration - the number of ticks the hitbox will be active for
        self.duration = duration
        # Set up isProjectile
        self.isProjectile = isProjectile
        # The key for what the target of the projectile should be set to
        self.targetKey = targetKey
        # The speed of the projectile
        self.speed = speed
        # Set up bool to track if a projectile has hit its target (and should be removed)
        self.deleteMe = False
    
    # Function to check if a hitbox should be spawned
    def isActive(self, tick):
        return(tick % self.startTick < self.duration)
    