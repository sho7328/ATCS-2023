import pygame
from player import Player
from bee import Bee
from river import River
from beehive import Beehive
from house import House

# Define some colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Define screen dimensions
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 850

# Define bee dimensions
BEE_WIDTH = 30
BEE_HEIGHT = 30

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("River Trek")

        # Load background image
        self.background = pygame.image.load("background_image.jpg")  # Replace with your image file
        self.background = pygame.transform.scale(self.background, (SCREEN_WIDTH, SCREEN_HEIGHT))

        self.bees = pygame.sprite.Group()
        
        self.beehives = pygame.sprite.Group()

        self.river1 = River(200, SCREEN_HEIGHT - 130, SCREEN_WIDTH - 200, 0)

        self.river2 = River(400, 200, SCREEN_WIDTH - 400, 200)

        self.river3 = River(200, 300, 0, SCREEN_HEIGHT - 300)

        self.house = House()
        
        self.player = Player()

        self.beehive = Beehive()

        self.beehive_collide = False
        self.first_collide = True

        for i in range(5):
            bee = Bee(self)
            self.bees.add(bee)

        self.font = pygame.font.Font(None, 36)

        # Add a timer variable
        self.game_over_timer = 0  
        self.wait_timer = 0

        self.player_win = False

        self.clock = pygame.time.Clock()


    def get_game_over(self):
        return self.game_over

    def check_river_collision(self):
        # Check for collision between player and river
        if pygame.sprite.collide_rect(self.player, self.river1) or pygame.sprite.collide_rect(self.player, self.river2) or pygame.sprite.collide_rect(self.player, self.river3):
            # Player touched the river, decrease health
            self.player.health -= 1
    
    def check_bee_collision(self):
        # Check for collisions
        if pygame.sprite.spritecollide(self.player, self.bees, False):
            for bee in self.bees:
                if bee.get_state() == "chasing":
                    self.player.health -= 1
    
    def check_beehive_collision(self):
        if pygame.sprite.collide_rect(self.player, self.beehive):

            self.beehive_collide = True
            if self.first_collide == True:
                self.player.speed *= 2  # Double player speed
                self.first_collide = False
                self.wait_timer = 0

    def check_house_collision(self):
        if pygame.sprite.collide_rect(self.player, self.house):
            self.player_win = True

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.check_river_collision()
            self.check_bee_collision()
            self.check_beehive_collision()
            self.check_house_collision()


            input = None
            if self.beehive_collide:
                if self.wait_timer < 1:
                    input = "touched_hive"
                self.wait_timer += 1
                if self.wait_timer > 30 and self.wait_timer < 100:
                    input = "time_up"
                    self.wait_timer = 1000
            
            for bee in self.bees:
                bee.update(input)


            self.beehive.update()
            self.river1.update()
            self.river2.update()
            self.river3.update()
            self.house.update()
            self.player.update()

            # Draw background
            self.screen.blit(self.background, (0, 0))

            # Draw everything
            for bee in self.bees:
                self.bees.draw(self.screen)
            self.beehive.draw(self.screen)
            self.river1.draw(self.screen)
            self.river2.draw(self.screen)
            self.river3.draw(self.screen)
            self.house.draw(self.screen)
            self.player.draw(self.screen)

            # Display player health
            if self.player.health < 30:
                self.health_color = (255, 0, 0)
            else:
                self.health_color = (0, 255, 0)
            self.font = pygame.font.Font(None, 36)
            health_text = self.font.render(f"Health: {self.player.health}", True, self.health_color)
            self.screen.blit(health_text, (325, 10))

            if self.player_win == True:
                self.font = pygame.font.Font(None, 80)
                game_over = self.font.render(f"YOU WIN!", True, (0, 255, 0))
                self.screen.blit(game_over, ((SCREEN_WIDTH/6), SCREEN_HEIGHT/2))
                self.game_over_timer += 1

                if self.game_over_timer >= 200:
                    running = False

            if self.player.health <= 0:
                self.font = pygame.font.Font(None, 80)
                game_over = self.font.render(f"GAME OVER", True, (255, 0, 0))
                self.screen.blit(game_over, ((SCREEN_WIDTH/6), SCREEN_HEIGHT/2))
                self.game_over_timer += 1

                if self.game_over_timer >= 200:
                    running = False
            
            pygame.display.flip()
            self.clock.tick(30)

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
