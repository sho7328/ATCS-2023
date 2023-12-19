# This is all Chatgpt except for the house dimensions, image, location, and draw function.

import pygame

# House dimensions
HOUSE_WIDTH = 130
HOUSE_HEIGHT = 130

# Screen dimensions
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 850

class House(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Load house image
        self.image = pygame.image.load("house_image.png") 
        self.image = pygame.transform.scale(self.image, (HOUSE_WIDTH, HOUSE_HEIGHT))

        # Set house location
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH - HOUSE_WIDTH
        self.rect.y = SCREEN_HEIGHT - HOUSE_HEIGHT

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x , self.rect.y ))