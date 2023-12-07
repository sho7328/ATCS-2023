import pygame
from beehive import Beehive
from bee_fsm import FSM

# Define some colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Define bee dimensions
BEE_WIDTH = 30
BEE_HEIGHT = 30

class Bee(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Load bee image
        self.image = pygame.image.load("bee_image.png")  # Replace "bee_image.png" with your image file
        self.image = pygame.transform.scale(self.image, (BEE_WIDTH, BEE_HEIGHT))

        self.beehive = Beehive()

        self.rect = self.image.get_rect()
        self.rect.x = self.beehive.get_hive_x()
        self.rect.y = self.beehive.get_hive_y()
        self.speed = 0

        # intialize and define the fsm
        # initial state is south
        self.fsm = FSM("calm")
        self.init_fsm()

    def init_fsm(self):
        self.fsm.add_transition("dead", "chasing", self.calm, "calm")
        self.fsm.add_transition("touched_hive", "calm", self.chase_player, "chasing")
    

    def calm(self):
        self.speed = 0
        self.rect.x = self.beehive.get_hive_x()
        self.rect.y = self.beehive.get_hive_y()

    
    def chase_player(self):
         pass
    
    def dead(self):
         pass
    


    def update(self):
        # if self.state == "calm":
        #     # Implement FSM for transitioning to angry state
        #     pass
        # elif self.state == "angry":
        #     # Implement chasing behavior
            pass

