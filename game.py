import pygame
import time
from player import Player
from bee import Bee
from river import River1
from river import River2
from river import River3
from beehive import Beehive

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

        self.all_sprites = pygame.sprite.Group()
        self.bees = pygame.sprite.Group()
        self.beehives = pygame.sprite.Group()

        self.river1 = River1()
        self.all_sprites.add(self.river1)  

        self.river2 = River2()
        self.all_sprites.add(self.river2)

        self.river3 = River3()
        self.all_sprites.add(self.river3)


        self.player = Player()
        self.all_sprites.add(self.player)

        self.font = pygame.font.Font(None, 36)  

        for _ in range(5):
            bee = Bee()
            self.all_sprites.add(bee)
            self.bees.add(bee)

        beehive = Beehive()
        self.all_sprites.add(beehive)
        self.beehives.add(beehive)

        self.game_over = False

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
        hits = pygame.sprite.spritecollide(self.player, self.bees, False)
        if hits:
            self.player.health -= 1
    
    def check_beehive_collision(self):
        hits = pygame.sprite.spritecollide(self.player, self.beehives, True)
        if hits:
            self.player.speed *= 2  # Double player speed
        


    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.all_sprites.update()

            self.check_river_collision()
            self.check_bee_collision()
            self.check_beehive_collision()

            # Draw everything
            self.screen.fill(WHITE)
            self.all_sprites.draw(self.screen)

            # Display player health
            health_text = self.font.render(f"Health: {self.player.health}", True, (0, 0, 0))
            self.screen.blit(health_text, (10, 10))

            if self.player.health <= 0:
                game_over = self.font.render(f"GAME OVER", True, (0, 0, 0))
                self.screen.blit(game_over, (50, 50))
                time.sleep(5)
                running = False

            pygame.display.flip()
            self.clock.tick(30)

        
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
