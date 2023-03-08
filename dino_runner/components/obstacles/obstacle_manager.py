import pygame
import random
from dino_runner.components.obstacles.cactus import SmallCactus, LargeCactus
from dino_runner.components.obstacles.bird import Bird

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game_speed, player, on_death):
        if not self.obstacles:
            obstacle_type = random.randint(0, 2)
            if obstacle_type == 0:
                self.obstacles.append(SmallCactus())
            elif obstacle_type == 1:
                self.obstacles.append(LargeCactus())
            else:
                self.obstacles.append(Bird())

        for obstacle in self.obstacles:
            obstacle.update(game_speed, self.obstacles)
            if player.rect.colliderect(obstacle.rect):
                on_death()
                pygame.time.delay(1000)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset(self):
        self.obstacles.clear()
