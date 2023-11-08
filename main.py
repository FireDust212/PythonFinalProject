# Imports
import pygame
import time
import random

# Import our classes
from classes.player import Player, PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_VEL
from classes.enemy import Enemy, ENEMY_WIDTH, ENEMY_HEIGHT, ENEMY_VEL, ENEMY_DAMAGE
from classes.weapon import Weapon
from classes.weaponHitboxFrame import WeaponHitBoxFrame
from classes.vector import Vector

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
# Import the skull for the kill tracker
SKULL = pygame.transform.scale(pygame.image.load("./imgs/Skull.png"), (30,30))


# Function to draw everthing on screen
# Thins at the top of the function are at the bottom layer of the drawing
# This means the background should be drawn first
# Parameters: hitboxes (an array of hitboxes to draw), elapsed_time (time elapsed), kills(the number of enemies killed)
def draw(hitboxes, elapsed_time, kills):
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

    # Draw player/enemies/weapons
    for hb in hitboxes:
        hb.draw()

    # Draw elapsed time
    time_text = FONT.render(f"{mins}:{secs}:{mils}", 1, "white")
    WIN.blit(time_text, ((WIDTH - time_text.get_width()) / 2, 10))

    # Draw kills text
    kill_text = FONT.render(f"{kills}", 1, "white")
    WIN.blit(kill_text, (WIDTH - kill_text.get_width(), 10))
    WIN.blit(SKULL, (WIDTH - kill_text.get_width() - SKULL.get_width(), 10))

    # Update the display to apply the drawing
    pygame.display.update()


# Main game function
def main():
    # Variable for when the application is running
    run = True

    # Setup Clock
    clock = pygame.time.Clock()

    # Application loop
    while run:
        # Create the player (p1) in the center of the screen
        p1 = Player(WIN, (WIDTH / 2) - (PLAYER_WIDTH / 2), (HEIGHT / 2) - (PLAYER_HEIGHT / 2), 100, 100, [])

        # Create the initial weapon
        # Set up the weapon hitboxes
        target = Vector(0,0) # Set up the target for the projectile. Changing this will change the projectile target
        weaponHBS = [
            WeaponHitBoxFrame(45, -50, 10, 100, 60, 30, False, None, None),
            WeaponHitBoxFrame(PLAYER_WIDTH/2, PLAYER_HEIGHT/2, 10, 20, 120, 1, True, target, 2),
        ]
        w1 = Weapon(WIN, "white", weaponHBS, 5, p1)

        # Give weapon to player
        p1.addWeapon(w1)

        # Set up the enemies
        enemy_add_increment = 4000  # When an enemy is added
        enemy_count = 0             # How long it has been since the last enemy was spawned
        enemies = []                # List of enemies

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
                keys = []
        # End main menu


        # Gameplay
        gamePlay = run

        # Get game start time, setup time tracking
        start_time = time.time()
        elapsed_time = 0
        # Ticks - the number of times the game loop has run
        ticks = 0

        # Other variables to track that need to be set up outside the while loop
        kills = 0
        win = True

        while gamePlay:
            # Set the maximum number of times the while loop runs (Frames per second)
            # Set the enemy_count equal to the number of miliseconds since the last clock tick
            enemy_count += clock.tick(60)
            # Increment elapsed time
            elapsed_time = time.time() - start_time
            # Increment ticks
            ticks+=1

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
                    en = Enemy(WIN, enemy_x, enemy_y, 10, 10)
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

            # Weapon logic here
            # target.x += 1
            # target.y += 1
            for weapon in p1.weapons:
                # Update weapons
                weapon.update(ticks)
                # Deal damage to enemies
                for weaponHB in weapon.hitboxes:
                    for en in enemies:
                        if en.colliderect(weaponHB):
                            en.currentHealth -= weapon.damage


            # Move the enemies towards the player, handle collision
            # Loop though a copy of the enemy list (Modifying list while looping causes errors)
            for en in enemies[:]:
                # Tell the enemy to move towads the player, give a list of all enemies (excluding this one)
                otherEnemies = enemies[:]
                otherEnemies.remove(en)
                en.moveTowards(p1, ENEMY_VEL, otherEnemies)
                # Remove enemies with health below 0
                if en.currentHealth <= 0:
                    enemies.remove(en)
                    kills += 1
                elif en.colliderect(p1):
                    p1.currentHealth -= ENEMY_DAMAGE
            # End enemy loop
            
            # Check player health
            if p1.currentHealth <= 0:
                win = False
                gamePlay = False
                
            # Call the draw function
            # list of hitboxes to draw
            drawHB = [p1]
            for en in enemies:
                drawHB.append(en)
            for weapon in p1.weapons:
                for weaponHB in weapon.hitboxes:
                    drawHB.append(weaponHB)
            draw(drawHB, elapsed_time, kills)

            # end game after 3 mins
            if int(elapsed_time / 60) >= 3:
                run = False
        # End Gameplay

        # End Screen
        endScreen = run
        while endScreen:
            # Set the maximum number of times the while loop runs (Frames per second)
            clock.tick(60)

            # Check all events that have happened since the last check
            for event in pygame.event.get():
                # User closed window with x
                if event.type == pygame.QUIT:
                    # Stop running the game and stop checking events
                    endScreen = False
                    run = False
                    break
            
            # Check the keys pressed
            keys = pygame.key.get_pressed()
            # If the key is space, return to the main menu
            if keys[pygame.K_SPACE]:
                endScreen = False
                keys = []

            # Temp end screen
            winMessage = ""
            if win:
                winMessage = 'You Win'
            else:
                winMessage = "You loser"
            message_text = FONT.render(winMessage, 1, "white")
            WIN.blit(message_text, ((WIDTH - message_text.get_width())/2, (HEIGHT - message_text.get_height())/2))
            pygame.display.update()
        # End end screen

        # Delay to prevent instantly skipping the main menu
        if run:
            start_time = time.time()
            elapsed_time = 0
            while elapsed_time < 1:
                # Increment elapsed time
                elapsed_time = time.time() - start_time

    # End run loop
    # Close the window when the run loop has ended
    pygame.quit()

# Only run the main function if the file is actually being run,
# prevents this file from running if it is imported to another file
if __name__ == "__main__":
    main()