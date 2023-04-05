from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS
import pygamee

class obstacleManager:

    def __init__(self):
        self.Obstacles = []

    def update(self, game):
        if len(self.Obstacles) == 0:
            self.Obstacles.append(Cactus(SMALL_CACTUS))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.Obstacles)
            if game.player.rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game,playing = False
                game.death_count +=1
                break


    def draw(self, screen):
        for obstacle in self.Obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []