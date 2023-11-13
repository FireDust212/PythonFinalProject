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

# Import weapons
from weapons import WEAPONSETUP

# Import window things - this prevents some cicuitous imports
from setupVars import BIGFONT, WIDTH, HEIGHT, WIN

# Give the window a name 
pygame.display.set_caption("Square Survivor")

# Import the tiling of the background
BGTILE = pygame.transform.scale(pygame.image.load("./imgs/backgroundTile.png"), (100,100))
# Import the skull for the kill tracker
SKULL = pygame.transform.scale(pygame.image.load("./imgs/Skull.png"), (30,30))


# Function to draw everthing on screen
# Thins at the top of the function are at the bottom layer of the drawing
# This means the background should be drawn first
# Parameters: hitboxes (an array of hitboxes to draw), elapsed_time (time elapsed), kills(the number of enemies killed)
def draw(hitboxes, elapsed_time, kills, update = True):
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
    time_text = BIGFONT.render(f"{mins}:{secs}:{mils}", 1, "white")
    WIN.blit(time_text, ((WIDTH - time_text.get_width()) / 2, 10))

    # Draw kills text
    kill_text = BIGFONT.render(kills, 1, "white")
    WIN.blit(kill_text, (WIDTH - kill_text.get_width(), 10))
    WIN.blit(SKULL, (WIDTH - kill_text.get_width() - SKULL.get_width(), 10))

    # Update the display to apply the drawing
    if update: pygame.display.update()
# End Draw

# Drawing the level up screen
def drawLevelUp(elapsed_time, kills, levelUpOptions):
    # Draw regular screen
    draw([], elapsed_time, kills, False)

    # Draw a mask over the regular gameplay
    mask = pygame.Surface((WIDTH,HEIGHT))   # Create a surface
    mask.set_alpha(128)                     # Set it's alpha level
    mask.fill((0,0,0))                # this fills the entire surface
    WIN.blit(mask, (0,0))                   # Add the mask to the window

    # Draw Level Up Title
    level_up_title = BIGFONT.render(f"Level Up!", 1, "white")
    WIN.blit(level_up_title, ((WIDTH - level_up_title.get_width()) / 2, 40))
    
    # Draw the levelUp options
    for y in range(len(levelUpOptions)):
        levelUpOptions[y].y = 50 + BIGFONT.get_height() + (20 + levelUpOptions[y].height) * y
        levelUpOptions[y].draw()

    # Update the display to apply the drawing
    pygame.display.update()
# End Draw Level Up



# Main game function
def main():
    # Variable for when the application is running
    run = True

    # Setup Clock
    clock = pygame.time.Clock()

    # Hit space reminder
    hit_space = BIGFONT.render("Hit Space", 1, "white")


    # Application loop
    while run:
        # Create the player (p1) in the center of the screen
        p1 = Player(WIN, (WIDTH / 2) - (PLAYER_WIDTH / 2), (HEIGHT / 2) - (PLAYER_HEIGHT / 2), 100, 100, [])


        # Create weapons, give to player
        for weaponName in WEAPONSETUP.copy():
            wep = Weapon(WIN, WEAPONSETUP[weaponName]['color'], weaponName,  WEAPONSETUP[weaponName]['hbs'][:], WEAPONSETUP[weaponName]['damage'], p1, WEAPONSETUP[weaponName]['levelUp'][:])
            p1.addWeapon(wep)

        # Set up the enemies
        enemy_add_increment = 4000  # When an enemy is added
        enemy_count = 0             # How long it has been since the last enemy was spawned
        enemies = []                # List of enemies

        # Main menu
        mainMenu = True
        while mainMenu:
            # Set the maximum number of times the while loop runs (Frames per second)
            clock.tick(60)

            #set display image for the main menu
            WIN.fill((255,0,0))
            title_text = BIGFONT.render(f"Square Survivor", 1, "white")
            title_shadow = BIGFONT.render(f"Square Survivor", 1, "black")
            WIN.blit(title_shadow, ((WIDTH - title_text.get_width()) / 2 + 2, 40 + 2))
            WIN.blit(title_text, ((WIDTH - title_text.get_width()) / 2, 40))
            start_text = BIGFONT.render(f"Click to Start!", 1, "black")
            
            #set-up to draw the rectangle
            input_rect = pygame.Rect(((WIDTH - start_text.get_width()) / 2 -20, (HEIGHT - start_text.get_height()) / 2 -20, start_text.get_width() + 40, start_text.get_height() + 30))
            color = pygame.Color(0,0,0)
            pygame.draw.rect(WIN, color, input_rect)
            inner_rect = pygame.Rect(((WIDTH - start_text.get_width()) / 2 -10, (HEIGHT - start_text.get_height()) / 2 -10, start_text.get_width() + 20, start_text.get_height() + 10))
            pygame.draw.rect(WIN, 'white', inner_rect)

            WIN.blit(start_text, ((WIDTH - start_text.get_width()) / 2, (HEIGHT - start_text.get_height())/2))

            pygame.display.update()
            # Check all events that have happened since the last check
            for event in pygame.event.get():
                # User closed window with x
                if event.type == pygame.QUIT:
                    # Stop running the game and stop checking events
                    mainMenu = False
                    run = False
                    break
                #check for mouse click events
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    #Check if the mouse click is inside the rectangle
                    pos = pygame.mouse.get_pos()
                    if input_rect.collidepoint(pos):
                        mainMenu = False
            
            # # Check the keys pressed
            # keys = pygame.key.get_pressed()
            # # If the key is space, close the main menu - this is temporary behavior
            # if keys[pygame.K_SPACE]:
            #     mainMenu = False
            #     keys = []
            
            # # Tell the user to hit space
            # hit_space = BIGFONT.render("Hit Space", 1, "white")
            # WIN.blit(hit_space, ((WIDTH - hit_space.get_width())/2, (HEIGHT - hit_space.get_height())/2 + hit_space.get_height()))
            # pygame.display.update()

        # End main menu


        # Gameplay
        gamePlay = run
        levelUp = False

        # Get game start time, setup time tracking
        start_time = time.time()
        elapsed_time = 0
        # Ticks - the number of times the game loop has run
        ticks = 0

        # Other variables to track that need to be set up outside the while loop
        kills = 0
        killsToLevelUp = 10
        levels = 1
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
                for _ in range(5):
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
                    enhp = 15 + int(elapsed_time) # enemy health increses each minute
                    en = Enemy(WIN, enemy_x, enemy_y, enhp, enhp)
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

            # Get closest, furthest, and a random enemy
            close_enemy_pos, far_enemy_pos, rand_enemy_pos = Vector(0,0),Vector(0,0),Vector(0,0)
            if len(enemies) > 0:
                re = random.choice(enemies)
                rand_enemy_pos = Vector(re.x, re.y)

                short = WIDTH*HEIGHT
                long = 0
                for en in enemies:
                    dist = Vector(p1.x,p1.y).distTo(en)
                    if dist > long:
                        long = dist
                        far_enemy_pos = Vector(en.x,en.y)
                    if dist < short:
                        short = dist
                        close_enemy_pos = Vector(en.x,en.y)

            # Weapon logic here
            # target.x += 1
            # target.y += 1
            for weapon in p1.weapons:
                # Update weapons
                weapon.update(ticks, close_enemy_pos, far_enemy_pos, rand_enemy_pos)
                # Deal damage to enemies
                for weaponHB in weapon.hitboxes:
                    for en in enemies:
                        if en.colliderect(weaponHB):
                            if not en.invincible:
                                en.currentHealth -= weapon.damage
                                en.invincible = True


            # Update the hitboxes
            p1.update(ticks)
            for en in enemies: en.update(ticks)
            
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
                    # Check levelup condition
                    if kills >= killsToLevelUp: 
                        levelUp = run
                        killsToLevelUp += 5*levels
                        levels += 1
                elif en.colliderect(p1):
                    if not p1.invincible:
                        p1.currentHealth -= ENEMY_DAMAGE
                        p1.invincible = True
            # End enemy loop
            
            # Check player health
            if p1.currentHealth <= 0:
                win = False
                gamePlay = False
            

            # LevelUp Loop setup
            if levelUp:
                # Determine the level up options
                levelUpOptions = [p1.getNextLevel()]
                for weapon in p1.weapons:
                    if weapon.level < weapon.maxLevel:
                        levelUpOptions.append(weapon.getNextLevel())
                
                if len(levelUpOptions) > 3:
                    random.shuffle(levelUpOptions)
                    levelUpOptions = levelUpOptions[0:3]
            # LevelUp Loop
            while levelUp:
                # Check all events that have happened since the last check
                for event in pygame.event.get():
                    # User closed window with x
                    if event.type == pygame.QUIT:
                        # Stop running the game and stop checking events
                        levelUp = False
                        gamePlay = False
                        run = False
                        break
                    # User clicked a part of the screen
                    elif event.type == pygame.MOUSEBUTTONUP:
                        # Get mouse position
                        pos = pygame.mouse.get_pos()
                        # Check if mouse is in a level up option
                        for option in levelUpOptions:
                            if option.collidepoint(pos):
                                option.origin.levelUp()
                                levelUp = False
                                break

                # Draw the levelUp screen
                drawLevelUp(elapsed_time, f"{kills}/{killsToLevelUp}", levelUpOptions)
            # end levelUp

                
            # Call the draw function
            drawHB = [p1] # list of hitboxes to draw
            for en in enemies:
                drawHB.append(en)
            for weapon in p1.weapons:
                for weaponHB in weapon.hitboxes:
                    drawHB.append(weaponHB)
            draw(drawHB, elapsed_time, f"{kills}/{killsToLevelUp}")

            # end game after 3 mins
            if elapsed_time // 60 >= 3:
            # if elapsed_time >20: #- testing
                gamePlay = False
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
            message_text = BIGFONT.render(winMessage, 1, "white")
            WIN.blit(hit_space, ((WIDTH - hit_space.get_width())/2, (HEIGHT - hit_space.get_height())/2 + hit_space.get_height()))
            WIN.blit(message_text, ((WIDTH - message_text.get_width())/2, (HEIGHT - message_text.get_height())/2))
            pygame.display.update()
        # End end screen

        
        # Cleanup before restarting the game
        for x in range(len(p1.weapons)):
            for y in range(len(p1.weapons[x].hitboxes)):
                p1.weapons[x].hitboxes[y] = None
            p1.weapons[x].hitboxes = None
            for z in range(len(p1.weapons[x].hitboxSetup)):
                p1.weapons[x].hitboxSetup[z] = None
            p1.weapons[x].hitboxSetup = None
            p1.weapons[x] = None
        p1.weapons = None
        del p1.weapons
        for en in enemies:
            en = None
            del en
        enemies = None
        del enemies
        p1 = None
        del p1

    # End run loop
    # Close the window when the run loop has ended
    pygame.quit()

# Only run the main function if the file is actually being run,
# prevents this file from running if it is imported to another file
if __name__ == "__main__":
    main()