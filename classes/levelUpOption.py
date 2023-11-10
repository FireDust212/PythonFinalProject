import pygame
from setupVars import BIGFONT, SMALLFONT, WIDTH, HEIGHT

# Declare the class - extends the pygame.Rect class, giving us some pre-declared functions
class LevelUpOption(pygame.Rect):
    # Define the initialization function
    def __init__(self, window, title, level, description, origin):
        # Call the parent class's initialization function
        super().__init__(WIDTH/4, 50, WIDTH/2, HEIGHT/5)

        # Set up other attributes
        self.window = window
        self.level = level
        self.title = title
        self.description = description
        self.origin = origin # The thing that will level up

    # Draw Function
    def draw(self):
        # Draw a box around the text
        pygame.draw.rect(self.window, (255,255,0), (self.x-5, self.y-5, self.width+10, self.height+10))
        pygame.draw.rect(self.window, (255,215,0), (self.x, self.y, self.width, self.height))

        # Draw the title
        title_text = BIGFONT.render(f"{self.title}", 1, "black")
        self.window.blit(title_text, (self.x+10, self.y+10))
        # Draw the level
        level_text = BIGFONT.render(f"Level: {self.level}", 1, "black")
        self.window.blit(level_text, (self.x+10, self.y+10+BIGFONT.get_height()))
        # Draw the description
        for y in range(len(self.description)):
            desc_text = SMALLFONT.render(f"{self.description[y]}", 1, "black")
            self.window.blit(desc_text, (self.x+10, self.y+20+2*BIGFONT.get_height()+SMALLFONT.get_height()*y))