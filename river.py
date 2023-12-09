import pygame

# Define some colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Define river dimensions
RIVER_WIDTH = 200
RIVER_HEIGHT = 750

# Define screen dimensions
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 850

class River(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([RIVER_WIDTH, RIVER_HEIGHT])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH - RIVER_WIDTH
        self.rect.y = 0

    def update(self):
        # You can add additional logic here if needed
        pass
