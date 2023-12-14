import pygame

# Define some colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Define river dimensions
RIVER_WIDTH1 = 200
RIVER_HEIGHT1 = 850 - 130

RIVER_WIDTH2 = 400
RIVER_HEIGHT2 = 200

RIVER_WIDTH3 = 200
RIVER_HEIGHT3 = 300

# Define screen dimensions
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 850

class River(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x #SCREEN_WIDTH - RIVER_WIDTH1
        self.rect.y = y #0

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x , self.rect.y ))