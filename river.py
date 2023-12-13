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

class River1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([RIVER_WIDTH1, RIVER_HEIGHT1])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH - RIVER_WIDTH1
        self.rect.y = 0

    def update(self):
        # You can add additional logic here if needed
        pass

class River2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([RIVER_WIDTH2, RIVER_HEIGHT2])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH - RIVER_WIDTH2
        self.rect.y = 200

    def update(self):
        # You can add additional logic here if needed
        pass


class River3(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([RIVER_WIDTH3, RIVER_HEIGHT3])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = SCREEN_HEIGHT - RIVER_HEIGHT3

    def update(self):
        # You can add additional logic here if needed
        pass

