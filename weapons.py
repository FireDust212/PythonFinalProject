# This is just a file to hold the possible weapons

# imports
from classes.weapon import Weapon
from classes.weaponHitboxFrame import WeaponHitBoxFrame
from classes.vector import Vector
from classes.player import PLAYER_WIDTH, PLAYER_HEIGHT


# Set up the target for the projectile. Changing this will change the projectile target
target = Vector(0,0) 

# Set up the weapon hitboxes
# x, y, width, height, startTick, duration, isProjectile, target, speed)
WEAPONHITBOXES = {
    "sword":    {
                    'color':'white', 
                    'damage': 10,
                    'hbs':  [
                                WeaponHitBoxFrame(PLAYER_WIDTH, -PLAYER_HEIGHT, 10, 2*PLAYER_HEIGHT, 60, 30, False, None, None)
                            ],
                },
    "gun":      {
                    'color':'black', 
                    'damage': 5,
                    'hbs':  [
                                WeaponHitBoxFrame(PLAYER_WIDTH/2, PLAYER_HEIGHT/2, 10, 20, 120, 1, True, target, 2)
                            ],
                },
    "shield":   {
                    'color':'green', 
                    'damage': 5,
                    'hbs':  [
                                # WeaponHitBoxFrame(-2*PLAYER_WIDTH, -2*PLAYER_HEIGHT, PLAYER_WIDTH*5, 5, 30, 10, False, None, None),
                                # WeaponHitBoxFrame(-2*PLAYER_WIDTH, -2*PLAYER_HEIGHT, 5, PLAYER_HEIGHT*5, 30, 10, False, None, None),
                                # WeaponHitBoxFrame(3*PLAYER_WIDTH, -2*PLAYER_HEIGHT, 5, PLAYER_HEIGHT*5+5, 30, 10, False, None, None),
                                # WeaponHitBoxFrame(-2*PLAYER_WIDTH, 3*PLAYER_HEIGHT, PLAYER_WIDTH*5, 5, 30, 10, False, None, None),

                                # WeaponHitBoxFrame(-PLAYER_WIDTH, -PLAYER_HEIGHT, PLAYER_WIDTH*3, 5, 30, 10, False, None, None),
                                # WeaponHitBoxFrame(-PLAYER_WIDTH, -PLAYER_HEIGHT, 5, PLAYER_HEIGHT*3, 30, 10, False, None, None),
                                # WeaponHitBoxFrame(2*PLAYER_WIDTH, -PLAYER_HEIGHT, 5, PLAYER_HEIGHT*3+5, 30, 10, False, None, None),
                                # WeaponHitBoxFrame(-PLAYER_WIDTH, 2*PLAYER_HEIGHT, PLAYER_WIDTH*3, 5, 30, 10, False, None, None),
                                
                                WeaponHitBoxFrame(0, 0, PLAYER_WIDTH, 5, 30, 10, False, None, None),
                                WeaponHitBoxFrame(0, 0, 5, PLAYER_HEIGHT, 30, 10, False, None, None),
                                WeaponHitBoxFrame(PLAYER_WIDTH, 0, 5, PLAYER_HEIGHT+5, 30, 10, False, None, None),
                                WeaponHitBoxFrame(0, PLAYER_HEIGHT, PLAYER_WIDTH, 5, 30, 10, False, None, None)
                            ],
                }
}