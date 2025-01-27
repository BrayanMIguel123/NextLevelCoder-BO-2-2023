from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, BIRD, LARGE_CACTUS
import pygame
import random

class obstacleManager:

    def __init__(self):
        self.Obstacles = []

    def update(self, game):
        if len(self.Obstacles) == 0:
            self.obstacles_options = random.choice([Cactus(SMALL_CACTUS), Bird(BIRD)])
            self.obstacles.append(self.obstacle_options)



        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.Obstacles)
            if game.player.rect.colliderect(obstacle.rect):
                if not game.player.shield:
                    pygame.time.delay(500)
                    game,playing = False
                    game.death_count +=1
                    break


    def draw(self, screen):
        for obstacle in self.Obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []