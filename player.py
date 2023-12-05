import pygame


# Define some colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Define screen dimensions
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 850

# Define player dimensions
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([PLAYER_WIDTH, PLAYER_HEIGHT])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.health = 100
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:# and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:# and self.rect.x < SCREEN_WIDTH - PLAYER_WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:# and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:# and self.rect.y < SCREEN_HEIGHT - PLAYER_HEIGHT:
            self.rect.y += self.speed
