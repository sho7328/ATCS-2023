# Class outlined with Chatgpt. 
# Chatgpt also helped with some other additions and debugging. 
# The rest is coded and tweaked by me (Sophie), and help from Ms. Namasivayam with implementing the bees FSM.

import pygame
from player import Player
from bee import Bee
from river import River
from beehive import Beehive
from house import House

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Define screen dimensions
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 850

# Game class:
class Game:
    # Constructor:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("River Trek")

        # Load background image
        self.background = pygame.image.load("background_image.jpg")
        self.background = pygame.transform.scale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))

        # Create sprite group for the bees.
        self.bees = pygame.sprite.Group()

        # Initialize game elements
        # Different rivers have different shape and locations
        self.river1 = River(200, SCREEN_HEIGHT - 130, SCREEN_WIDTH - 200, 0)
        self.river2 = River(400, 200, SCREEN_WIDTH - 400, 200)
        self.river3 = River(200, 300, 0, SCREEN_HEIGHT - 300)
        self.house = House()
        self.player = Player()
        self.beehive = Beehive()
        # Create bees and add them to the bees sprite group
        for i in range(5):
            bee = Bee(self, self.beehive)
            self.bees.add(bee)

        # Initialize collision variables
        self.beehive_collide = False
        self.first_collide = True

        # Initialize font
        self.font = pygame.font.Font(None, 36)

        # Initialize timers
        self.game_over_timer = 0
        self.wait_timer = 0

        # Flags for game state
        self.player_win = False
        self.game_over = False

        # Set the frame rate
        self.clock = pygame.time.Clock()

    # Checks for collision between player and river
    def check_river_collision(self):
        # If the player touched the river, decrease health by 1
        if pygame.sprite.collide_rect(self.player, self.river1) or pygame.sprite.collide_rect(self.player, self.river2) or pygame.sprite.collide_rect(self.player, self.river3):
            self.player.health -= 1

    # Checks for collision between player and bees
    def check_bee_collision(self):
        # If player touches bees
        if pygame.sprite.spritecollide(self.player, self.bees, False):
            # For each bee
            for bee in self.bees:
                # If the bee is in the chasing state, player loses 1 health.
                if bee.get_state() == "chasing":
                    self.player.health -= 1

    # Checks for collision between player and beehive
    def check_beehive_collision(self):
        # If the player touches beehive
        if pygame.sprite.collide_rect(self.player, self.beehive):
            self.beehive_collide = True
            # If it's the first time colliding with the beehive, double player speed
            if self.first_collide == True:
                self.player.speed *= 2
                # Make sure that it's set as not the first collide anymore, so that the player speed doesn't keep doubling
                self.first_collide = False
                # Set wait timer to 0 so that the game knows the player just collided with the beehive.
                self.wait_timer = 0

    # Checks for collision between player and house
    def check_house_collision(self):
        # If player touches house and the player is not dead yet, the player has won
        if pygame.sprite.collide_rect(self.player, self.house) and self.player.health > 0:
            self.player_win = True

    # Code for the game
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Check collisions/run the collision methods
            self.check_river_collision()
            self.check_bee_collision()
            self.check_beehive_collision()
            self.check_house_collision()

            # Set input based on collision with beehive (Help from Ms. Namasivayam)
            # Default input is None (bee stays calm, waiting, or chasing)
            input = None
            # If the player has touched the beehive
            if self.beehive_collide:
                # If it is the first time (right after) the player touched the hive, the bee's input becomes "touched_hive" (bee is now waiting)
                if self.wait_timer < 1:
                    input = "touched_hive"
                # Increase wait timer
                self.wait_timer += 1
                # If the bee is done waiting (time has passed) the bee's input is time up (bee will now start chasing)
                if self.wait_timer > 30 and self.wait_timer < 100:
                    input = "time_up"
                    # Make sure wait timer can't change the input now (input will default to None)
                    self.wait_timer = 1000

            # Update bee imput for FSM
            for bee in self.bees:
                bee.update(input)

            # Update game elements
            self.beehive.update()
            self.river1.update()
            self.river2.update()
            self.river3.update()
            self.house.update()
            self.player.update()

            # Draw background
            self.screen.blit(self.background, (0, 0))

            # Draw all game elements
            self.river1.draw(self.screen)
            self.river2.draw(self.screen)
            self.river3.draw(self.screen)
            self.house.draw(self.screen)
            for bee in self.bees:
                self.bees.draw(self.screen)
            self.beehive.draw(self.screen)
            self.player.draw(self.screen)

            # Display player health
            # If the player health is less than 30, switch font color to red
            if self.player.health < 30:
                self.health_color = (255, 0, 0)
            else:
                # Otherwise font color is green
                self.health_color = (0, 255, 0)
            # Set font size
            self.font = pygame.font.Font(None, 36)
            # Draw the text
            health_text = self.font.render(f"Health: {self.player.health}", True, self.health_color)
            self.screen.blit(health_text, (325, 10))

            # Check for win or game over conditions
            # If the player won (touched the house) and the game is not over yet (the player is still alive):
            if self.player_win == True and self.game_over == False:
                # Set font size and draw the text
                self.font = pygame.font.Font(None, 80)
                game_over = self.font.render(f"YOU WIN!", True, (0, 255, 0))
                self.screen.blit(game_over, ((SCREEN_WIDTH/6), SCREEN_HEIGHT/2))
                # Show for a certain amount of time, then close the game once timer is reached.
                self.game_over_timer += 1
                if self.game_over_timer >= 100:
                    running = False
            # If the player health is less than or equal to zero (player is dead) and the player hasn't won yet
            if self.player.health <= 0 and self.player_win == False:
                # The game is over
                self.game_over = True
                # Set font size and draw the text
                self.font = pygame.font.Font(None, 80)
                game_over = self.font.render(f"GAME OVER", True, (255, 0, 0))
                self.screen.blit(game_over, ((SCREEN_WIDTH/6), SCREEN_HEIGHT/2))
                # Show for a certain amount of time, then close the game once timer is reached.
                self.game_over_timer += 1
                if self.game_over_timer >= 100:
                    running = False

            pygame.display.flip()
            self.clock.tick(30)
        # End game once it's over
        pygame.quit()

# Run the game.
if __name__ == "__main__":
    game = Game()
    game.run()
