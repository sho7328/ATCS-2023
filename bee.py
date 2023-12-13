import pygame
from beehive import Beehive
from bee_fsm import FSM
from player import Player
import random


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
        self.image = pygame.image.load("bee_image.png") 
        self.image = pygame.transform.scale(self.image, (BEE_WIDTH, BEE_HEIGHT))

        self.beehive = Beehive()
        self.player = Player()

        self.rect = self.image.get_rect()
        self.og_x = self.beehive.get_hive_x() + random.randrange(-1 * BEE_WIDTH, BEE_WIDTH)
        self.og_y = self.beehive.get_hive_y() + random.randrange(-1 * BEE_HEIGHT, BEE_HEIGHT)
        self.rect.x = self.og_x
        self.rect.y = self.og_y
        
        self.speed = 0

        # intialize and define the fsm
        # initial state is south
        self.fsm = FSM("calm")
        self.init_fsm()
        

    def get_state(self):
        return self.fsm.current_state

    def init_fsm(self):
        self.fsm.add_transition("dead", "chasing", self.calm, "calm")
        self.fsm.add_transition("touched_hive", "calm", self.chase_player, "chasing")
    

    def calm(self):
        self.speed = 0
        self.rect.x = self.og_x
        self.rect.y = self.og_y

    
    def chase_player(self):
        self.speed = self.player.get_player_speed()
        if self.player.get_player_x() > self.rect.x:
             self.rect.x += self.speed
        else: #elif self.player.get_player_x() < self.rect.x:
            self.rect.x -= self.speed
        if self.player.get_player_y() > self.rect.y:
             self.rect.y += self.speed
        else: #elif self.player.get_player_y() < self.rect.y:
             self.rect.y -= self.speed


    def update(self):
        # if self.state == "calm":
        #     # Implement FSM for transitioning to angry state
        #     pass
        # elif self.state == "angry":
        #     # Implement chasing behavior
        self.chase_player()

