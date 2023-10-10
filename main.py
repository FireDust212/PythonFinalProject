# Imports
import pygame
import time
import random

# Import our player class
from classes.player import Player, PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_VEL


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
    # Variable for when the application is running
    run = True

    # Create the player (p1) in the center of the screen
    p1 = Player((WIDTH / 2) - (PLAYER_WIDTH / 2), (HEIGHT / 2) - (PLAYER_HEIGHT / 2), 100, 100)

    # Setup Clock
    clock = pygame.time.Clock()

    # Application loop
    while run:
        # Main menu
        mainMenu = True
        while mainMenu:
            # Set the maximum number of times the while loop runs (Frames per second)
            clock.tick(60)

            # Check all events that have happened since the last check
            for event in pygame.event.get():
                # User closed window with x
                if event.type == pygame.QUIT:
                    # Stop running the game and stop checking events
                    mainMenu = False
                    run = False
                    break
            
            # Check the keys pressed
            keys = pygame.key.get_pressed()
            # If the key is space, close the main menu - this is temporary behavior
            if keys[pygame.K_SPACE]:
                mainMenu = False
        # End main menu


        # Gameplay
        gamePlay = True
        while gamePlay:
            # Set the maximum number of times the while loop runs (Frames per second)
            clock.tick(60)

            # Check all events that have happened since the last check
            for event in pygame.event.get():
                # User closed window with x
                if event.type == pygame.QUIT:
                    # Stop running the game and stop checking events
                    run = False
                    gamePlay = False
                    break
            

            # Check the keys pressed
            keys = pygame.key.get_pressed()
            # Use the arrow keys or WASD to move
            # The "and"ed condition keeps the player onscreen
            if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and p1.x - PLAYER_VEL >= 0:
                # Move player left
                p1.x -= PLAYER_VEL
            if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and p1.x + PLAYER_VEL + p1.width <= WIDTH:
                # Move player right
                p1.x += PLAYER_VEL
            if (keys[pygame.K_UP] or keys[pygame.K_w]) and p1.y - PLAYER_VEL >= 0:
                # Move player up
                p1.y -= PLAYER_VEL
            if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and p1.y + PLAYER_VEL + p1.height <= HEIGHT:
                # Move player down
                p1.y += PLAYER_VEL
            
                
            # Call the draw function
            draw(p1)
        # End Gameplay

    # Close the window when the run loop has ended
    pygame.quit()

# Only run the main function if the file is actually being run,
# prevents this file from running if it is imported to another file
if __name__ == "__main__":
    main()