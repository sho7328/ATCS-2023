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

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x , self.rect.y ))