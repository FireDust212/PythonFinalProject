# Imports
import pygame
import time
import random

# Import our player class
from classes.player import Player, PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_VEL
# Import our enemy class
from classes.enemy import Enemy, ENEMY_WIDTH, ENEMY_HEIGHT, ENEMY_VEL, ENEMY_DAMAGE

# Setup font
pygame.font.init()
FONT = pygame.font.SysFont("consolas", 30)


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
# Parameters: p1 (the player), elapsed_time (time elapsed), enemies (the enemies)
def draw(p1, elapsed_time, enemies):
    # Set up tiling of background.
    for x in range(0, WIDTH, 100):
        for y in range(0, HEIGHT, 100):
            WIN.blit(BGTILE, (x,y))
    
    # Format elapsed time to min:sec
    mins = str(int(elapsed_time / 60))
    secs = str(int(elapsed_time % 60))
    mils = str(int(elapsed_time*100))[-2:]
    # Add leading 0s
    if len(mins) == 1:
        mins = '0' + mins
    if len(secs) == 1:
        secs = '0' + secs

    # Draw player
    pygame.draw.rect(WIN, "blue", p1)

    # Draw enemies
    for en in enemies:
        pygame.draw.rect(WIN, "red", en)

    # Draw elapsed time
    time_text = FONT.render(f"{mins}:{secs}:{mils}", 1, "white")
    WIN.blit(time_text, ((WIDTH - time_text.get_width()) / 2, 10))

    # Update the display to apply the drawing
    pygame.display.update()


# Main game function
def main():
    # Variable for when the application is running
    run = True

    # Create the player (p1) in the center of the screen
    p1 = Player((WIDTH / 2) - (PLAYER_WIDTH / 2), (HEIGHT / 2) - (PLAYER_HEIGHT / 2), 100, 100)

    # Set up the enemies
    enemy_add_increment = 4000  # When an enemy is added
    enemy_count = 0             # How long it has been since the last enemy was spawned
    enemies = []                # List of enemies

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
        gamePlay = run

        # Get game start time, setup time tracking
        start_time = time.time()
        elapsed_time = 0

        while gamePlay:
            # Set the maximum number of times the while loop runs (Frames per second)
            # Set the enemy_count equal to the number of miliseconds since the last clock tick
            enemy_count += clock.tick(60)
            # Increment elapsed time
            elapsed_time = time.time() - start_time

            # Enemy spawn logic
            if enemy_count > enemy_add_increment:
                # Value in range is the number of enemies to add
                for _ in range(1):
                    # Setup baseline enemy position
                    # Pick a random x value for the enemy
                    enemy_x = random.randint(0, WIDTH - ENEMY_WIDTH)
                    # Pick a random y value for the enemy
                    enemy_y = random.randint(0, HEIGHT - ENEMY_HEIGHT)

                    # Enemies are moved  so they appear offscreen
                    # Decide if they should be 
                        # 0: Left of the player
                        # 1: Above the player
                        # 2: Right of the player
                        # 3: Below the player
                    # (A switch/case block would be super useful here)
                    enemy_pos = random.randint(0, 3)
                    if enemy_pos == 0:
                        enemy_x = -ENEMY_WIDTH
                    elif enemy_pos == 1:
                        enemy_y = -ENEMY_HEIGHT
                    elif enemy_pos == 2:
                        enemy_x = WIDTH + ENEMY_WIDTH
                    else:
                        enemy_y = HEIGHT + ENEMY_HEIGHT

                    # Create the enemy
                    en = Enemy(enemy_x, enemy_y, 10, 10)
                    enemies.append(en)

                # Reset enemy_count and subtract 10 from enemy_add_increment (minimum of 200)
                enemy_count = 0
                enemy_add_increment = max(200, enemy_add_increment - 10)
            # End enemy spawn


            # Check all events that have happened since the last check
            for event in pygame.event.get():
                # User closed window with x
                if event.type == pygame.QUIT:
                    # Stop running the game and stop checking events
                    run = False
                    gamePlay = False
                    break
            # End event check
            

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
            # End key check

            # Move the enemies towards the player, handle collision
            # Loop though a copy of the enemy list (Modifying list while looping causes errors)
            for en in enemies[:]:
                # Tell the enemy to move towads the player, give a list of all enemies (excluding this one)
                otherEnemies = enemies[:]
                otherEnemies.remove(en)
                en.moveTowards(p1, otherEnemies)
                # Remove enemies with health below 0
                if en.currentHealth <= 0:
                    enemies.remove(en)
                elif en.colliderect(p1):
                    p1.currentHealth -= ENEMY_DAMAGE
            # End enemy loop
            
                
            # Call the draw function
            draw(p1, elapsed_time, enemies)
        # End Gameplay

    # Close the window when the run loop has ended
    pygame.quit()

# Only run the main function if the file is actually being run,
# prevents this file from running if it is imported to another file
if __name__ == "__main__":
    main()