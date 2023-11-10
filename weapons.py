# This is just a file to hold the possible weapons

# imports
from classes.weapon import Weapon
from classes.weaponHitboxFrame import WeaponHitBoxFrame
from classes.vector import Vector
from classes.player import PLAYER_WIDTH, PLAYER_HEIGHT


# Set up the target for the projectile. Changing this will change the projectile target
target = Vector(0,0) 

# Set up the weapons
# Hitboxes: x, y, width, height, startTick, duration, isProjectile, target, speed)

WEAPONSETUP = {
    "sword":    {
                    'color':'white', 
                    'damage': 10,
                    'hbs':  [
                                WeaponHitBoxFrame(PLAYER_WIDTH+10, -PLAYER_HEIGHT/2, 10, PLAYER_HEIGHT, 60, 30, False, None, None)
                            ],
                    'levelUp':[
                        {
                            "description": ["Second Sword", 'Damage +10'],
                            'damage': 10,
                            "cooldown": 0,
                            'duration': 0,
                            'hb': [
                                WeaponHitBoxFrame(-10, -PLAYER_HEIGHT*1.5, 10, PLAYER_HEIGHT, 60, 30, False, None, None)
                            ],
                        },
                        {
                            "description": ['Damage +10', "Cooldown -10", 'Duration +5'],
                            'damage': 10,
                            "cooldown": -10,
                            'duration': 5,
                            'hb': [],
                        },
                        {
                            "description": ["Three Sword Style"],
                            'damage': 20,
                            "cooldown": -20,
                            'duration': 5,
                            'hb': [WeaponHitBoxFrame(PLAYER_WIDTH - (PLAYER_WIDTH/4), -PLAYER_HEIGHT/2, PLAYER_WIDTH, 10, 60, 30, False, None, None)],
                        }
                    ]
                },
    "gun":      {
                    'color':'black', 
                    'damage': 5,
                    'hbs':  [
                                WeaponHitBoxFrame(PLAYER_WIDTH/2, PLAYER_HEIGHT/2, 10, 20, 120, 1, True, target, 2)
                            ],
                    'levelUp':[
                        {
                            "description": ["Damage +10"],
                            'damage': 10,
                            "cooldown": 0,
                            'duration': 0,
                            'hb': [],
                        },
                        {
                            "description": ["Damage +20"],
                            'damage': 20,
                            "cooldown": 0,
                            'duration': 0,
                            'hb': [],
                        },
                        {
                            "description": ["Damage +30"],
                            'damage': 30,
                            "cooldown": 0,
                            'duration': 0,
                            'hb': [],
                        }
                    ]
                },
    "shield":   {
                    'color':'green', 
                    'damage': 5,
                    'hbs':  [
                                WeaponHitBoxFrame(0, 0, PLAYER_WIDTH, 5, 30, 10, False, None, None),
                                WeaponHitBoxFrame(0, 0, 5, PLAYER_HEIGHT, 30, 10, False, None, None),
                                WeaponHitBoxFrame(PLAYER_WIDTH, 0, 5, PLAYER_HEIGHT+5, 30, 10, False, None, None),
                                WeaponHitBoxFrame(0, PLAYER_HEIGHT, PLAYER_WIDTH, 5, 30, 10, False, None, None)
                            ],
                    'levelUp':[
                        {
                            "description": ['Damage +5', 'Cooldown -10', 'Duration +10'],
                            'damage': 5,
                            "cooldown": -10,
                            'duration': 10,
                            'hb': [],
                        },
                        {
                            "description": ["Greater Area", 'Damage +5', 'Cooldown -10', 'Duration -10'],
                            'damage': 5,
                            "cooldown": -10,
                            'duration': -10,
                            'hb': [
                                WeaponHitBoxFrame(-PLAYER_WIDTH, -PLAYER_HEIGHT, PLAYER_WIDTH*3, 5, 40, 10, False, None, None),
                                WeaponHitBoxFrame(-PLAYER_WIDTH, -PLAYER_HEIGHT, 5, PLAYER_HEIGHT*3, 40, 10, False, None, None),
                                WeaponHitBoxFrame(2*PLAYER_WIDTH, -PLAYER_HEIGHT, 5, PLAYER_HEIGHT*3+5, 40, 10, False, None, None),
                                WeaponHitBoxFrame(-PLAYER_WIDTH, 2*PLAYER_HEIGHT, PLAYER_WIDTH*3, 5, 40, 10, False, None, None),
                            ],
                        },
                        {
                            "description": ["Greater Area", 'Damage +5', 'Cooldown -10', 'Duration +10'],
                            'damage': 5,
                            "cooldown": -10,
                            'duration': +10,
                            'hb': [
                                WeaponHitBoxFrame(-2*PLAYER_WIDTH, -2*PLAYER_HEIGHT, PLAYER_WIDTH*5, 5, 50, 10, False, None, None),
                                WeaponHitBoxFrame(-2*PLAYER_WIDTH, -2*PLAYER_HEIGHT, 5, PLAYER_HEIGHT*5, 50, 10, False, None, None),
                                WeaponHitBoxFrame(3*PLAYER_WIDTH, -2*PLAYER_HEIGHT, 5, PLAYER_HEIGHT*5+5, 50, 10, False, None, None),
                                WeaponHitBoxFrame(-2*PLAYER_WIDTH, 3*PLAYER_HEIGHT, PLAYER_WIDTH*5, 5, 50, 10, False, None, None),
                            ],
                        }
                    ]
                }
}
