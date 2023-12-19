# Class base was coded by chatgpt. It didn't change much from the base, though I deleted unecessary lines of code, added a beehive image, and 
# changed the beehive location and its dimensions. 

import pygame

# Screen height
SCREEN_HEIGHT = 850

# Define beehive dimensions
BEEHIVE_WIDTH = 60
BEEHIVE_HEIGHT = 60

class Beehive(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Load beehive image
        self.image = pygame.image.load("beehive_image.png")
        self.image = pygame.transform.scale(self.image, (BEEHIVE_WIDTH, BEEHIVE_HEIGHT))

        # Set beehive location
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = SCREEN_HEIGHT / 2

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x , self.rect.y ))