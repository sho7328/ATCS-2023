import pygame

# Define some colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Define screen dimensions
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 850

# Define player dimensions
PLAYER_WIDTH = 100
PLAYER_HEIGHT = 130

PLAYER_START_HEALTH = 50

PLAYER_SPEED = 5

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Load player image
        self.image = pygame.image.load("player_right.png")
        self.image = pygame.transform.scale(self.image, (PLAYER_WIDTH, PLAYER_HEIGHT))

        self.rect = self.image.get_rect()
        self.health = PLAYER_START_HEALTH
        self.speed = PLAYER_SPEED
        self.rect.x = 0
        self.rect.y = 0

    def get_player_speed(self):
        return self.speed
    
    def get_player_x(self):
        return self.rect.x
    
    def get_player_y(self):
        return self.rect.y
    
    def get_player_health(self):
        return self.health

    def change_image_direction(self, direction):
        self.image = pygame.image.load("player_" + direction + ".png")
        self.image = pygame.transform.scale(self.image, (PLAYER_WIDTH, PLAYER_HEIGHT))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
            self.change_image_direction("left")
        if keys[pygame.K_RIGHT] and self.rect.x < SCREEN_WIDTH - PLAYER_WIDTH:
            self.rect.x += self.speed
            self.change_image_direction("right")
        if keys[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y < SCREEN_HEIGHT - PLAYER_HEIGHT:
            self.rect.y += self.speed
