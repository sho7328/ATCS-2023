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
    def __init__(self, game):
        super().__init__()

        # Load bee image
        self.image = pygame.image.load("bee_image.png") 
        self.image = pygame.transform.scale(self.image, (BEE_WIDTH, BEE_HEIGHT))

        self.beehive = Beehive()
        self.game = game

        self.rect = self.image.get_rect()
        self.og_x = self.beehive.rect.x + random.randrange(-1 * BEE_WIDTH, BEE_WIDTH + 20)
        self.og_y = self.beehive.rect.y + random.randrange(-1 * BEE_HEIGHT, BEE_HEIGHT)
        self.rect.x = self.og_x
        self.rect.y = self.og_y
        
        self.speed = 0

        # intialize and define the fsm
        # initial state is south
        self.fsm = FSM("calm")
        self.init_fsm()

        # Add a timer variable
        self.wait_timer = 0  


    def get_state(self):
        return self.fsm.current_state

    def init_fsm(self):
        self.fsm.add_transition("touched_hive", "calm", None, "waiting")
        self.fsm.add_transition(None, "waiting", None, "waiting")
        self.fsm.add_transition("touched_hive", "waiting", None, "waiting")
        self.fsm.add_transition("time_up", "waiting", self.chase_player, "chasing")
        self.fsm.add_transition(None, "chasing", self.chase_player, "chasing")
        self.fsm.add_transition(None, "calm", self.calm, "calm")
    

    def calm(self):
        self.speed = 0
        self.rect.x = self.og_x
        self.rect.y = self.og_y

    
    def chase_player(self):
        self.speed = self.game.player.speed - 2
        if self.game.player.rect.x > self.rect.x:
             self.rect.x += self.speed
        elif self.game.player.rect.x < self.rect.x:
            self.rect.x -= self.speed
        if self.game.player.rect.y > self.rect.y:
             self.rect.y += self.speed
        elif self.game.player.rect.y < self.rect.y:
             self.rect.y -= self.speed


    def update(self, input=None):
        self.fsm.process(input)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x , self.rect.y))
