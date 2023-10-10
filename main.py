# Imports
import pygame
import time
import random

# Import our player class
from classes.player import Player, PLAYER_WIDTH, PLAYER_HEIGHT


# Set up the window
WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# Give the window a name 
pygame.display.set_caption("Shooty McShootface")


# Import the tiling of the background
BGTILE = pygame.transform.scale(pygame.image.load("./imgs/backgroundTile.png"), (100,100))


# Function to draw everthing on screen
# Thins at the top of the function are at the bottom layer of the drawing
# This means the background should be drawn first
def draw(p1):
    # Set up tiling of background.
    for x in range(0, WIDTH, 100):
        for y in range(0, HEIGHT, 100):
            WIN.blit(BGTILE, (x,y))

    # Draw player
    pygame.draw.rect(WIN, "red", p1)

    # Update the display to apply the drawing
    pygame.display.update()


# Main game function
def main():
    # Variable for when the game is running
    run = True

    # Create the player (p1) in the center of the screen
    p1 = Player(WIDTH / 2, HEIGHT / 2, 100, 100)

    while run:
        mainMenu = True
        while mainMenu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainMenu = False
                    run = False
                    break
            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                mainMenu = False
        gamePlay = True
        while gamePlay:
            # Check all events that have happened since the last check
            for event in pygame.event.get():
                # User closed window with x
                if event.type == pygame.QUIT:
                    # Stop running the game and stop checking events
                    run = False
                    gamePlay = False
                    break
                
            # Call the draw function
            draw(p1)

    # Close the window when the run loop has ended
    pygame.quit()

# Only run the main function if the file is actually being run,
# prevents this file from running if it is imported to another file
if __name__ == "__main__":
    main()