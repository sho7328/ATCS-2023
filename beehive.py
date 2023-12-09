import pygame


# Define screen dimensions
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 850

# Define beehive dimensions
BEEHIVE_WIDTH = 60
BEEHIVE_HEIGHT = 60

BEEHIVE_X = 10

class Beehive(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Load beehive image
        self.image = pygame.image.load("beehive_image.png")
        self.image = pygame.transform.scale(self.image, (BEEHIVE_WIDTH, BEEHIVE_HEIGHT))

        self.rect = self.image.get_rect()
        self.rect.x = BEEHIVE_X
        self.rect.y = SCREEN_HEIGHT / 2

    def get_hive_x(self):
        return self.rect.x
    
    def get_hive_y(self):
        return self.rect.y