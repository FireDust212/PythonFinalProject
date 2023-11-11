import pygame
from classes.vector import Vector

# Setup font
pygame.font.init()
BIGFONT = pygame.font.SysFont("consolas", 30)
SMALLFONT = pygame.font.SysFont("consolas", 15)


# Set up the window
WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))


# Enemy tracking - having these be global makes the tracking easier
close_enemy = 'close'
far_enemy = 'far'
rand_enemy = 'rand'