# The very base of the bee class was coded by Chatgpt, but I changed most of it by the time that I added more elements, debugged it, and implemented the FSM.
# At least 90% coded by me and help from Ms. Namasivayam

import pygame
from beehive import Beehive
from bee_fsm import FSM
import random

# Define bee dimensions
BEE_WIDTH = 30
BEE_HEIGHT = 30

class Bee(pygame.sprite.Sprite):
    def __init__(self, game, beehive):
        super().__init__()

        # Load bee image
        self.image = pygame.image.load("bee_image.png") 
        self.image = pygame.transform.scale(self.image, (BEE_WIDTH, BEE_HEIGHT))

        # Initialize/sync the game and the game beehive
        self.beehive = beehive
        self.game = game

        self.rect = self.image.get_rect()
        # The bee's location is a random range distance from the beehive, so that the bees aren't just stacked on top of each other.
        self.og_x = self.beehive.rect.x + random.randrange(-1 * BEE_WIDTH, BEE_WIDTH + 20)
        self.og_y = self.beehive.rect.y + random.randrange(-1 * BEE_HEIGHT, BEE_HEIGHT)
        self.rect.x = self.og_x
        self.rect.y = self.og_y

        # The bee starts off calm, speed = 0 because it is not moving.
        self.speed = 0

        # Intialize and define the fsm
        # Initial state is calm; bee is not moving and doesn't attack/chase player
        self.fsm = FSM("calm")
        self.init_fsm()

        # Add a timer variable
        self.wait_timer = 0  

    # Return the bee's state
    def get_state(self):
        return self.fsm.current_state

    # Add the bee's transitions to the FSM dictionary
    def init_fsm(self):
        self.fsm.add_transition(None, "calm", self.calm, "calm")
        self.fsm.add_transition("touched_hive", "calm", None, "waiting")
        self.fsm.add_transition(None, "waiting", None, "waiting")
        self.fsm.add_transition("touched_hive", "waiting", None, "waiting")
        self.fsm.add_transition("time_up", "waiting", self.chase_player, "chasing")
        self.fsm.add_transition(None, "chasing", self.chase_player, "chasing")

    # Action: if the bee is calm, it's not moving
    def calm(self):
        self.speed = 0
        self.rect.x = self.og_x
        self.rect.y = self.og_y

    # Action: the bee chases the player
    def chase_player(self):
        # It is 2 slower than the player
        self.speed = self.game.player.speed - 2
        # Follow the player's x by the bee speed
        if self.game.player.rect.x > self.rect.x:
             self.rect.x += self.speed
        elif self.game.player.rect.x < self.rect.x:
            self.rect.x -= self.speed
        # Follow the player's y by the bee speed
        if self.game.player.rect.y > self.rect.y:
             self.rect.y += self.speed
        elif self.game.player.rect.y < self.rect.y:
             self.rect.y -= self.speed

    # Take in the input from what is happening in the game, and send it to the FSM
    def update(self, input=None):
        self.fsm.process(input)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x , self.rect.y))