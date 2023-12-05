import pygame

# Define some colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Define bee dimensions
BEE_WIDTH = 30
BEE_HEIGHT = 30

class Bee(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        # Load bee image
        self.image = pygame.image.load("bee_image.png")  # Replace "bee_image.png" with your image file
        self.image = pygame.transform.scale(self.image, (BEE_WIDTH, BEE_HEIGHT))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 3
        self.state = "calm"  # Initial state

    def update(self):
        if self.state == "calm":
            # Implement FSM for transitioning to angry state
            pass
        elif self.state == "angry":
            # Implement chasing behavior
            pass

