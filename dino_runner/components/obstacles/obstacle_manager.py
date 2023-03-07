import pygame
from dino_runner.components.obstacles.cactus import Cactus


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game_speed, player, game):
        if not self.obstacles:
            self.obstacles.append(Cactus())

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if player.rect.colliderect(obstacle.rect):
                game.playing = False
                pygame.time.delay(1000)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
