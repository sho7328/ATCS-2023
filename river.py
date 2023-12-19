# The very base of this class was coded by chatgpt and which I expanded on to have 3 river classes for each different river shape,
# and Ms. Namasivayam then told me how I could just have 1 class with different river shapes/dimensions, so I tweaked the code again to make it more efficient.

import pygame 

# Blue color
BLUE = (0, 0, 255)

class River(pygame.sprite.Sprite):
    # Game passes in the rivers' dimensions and location
    def __init__(self, width, height, x, y):
        super().__init__()

        # Set the river visuals, color, and location
        self.image = pygame.Surface([width, height])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x , self.rect.y ))