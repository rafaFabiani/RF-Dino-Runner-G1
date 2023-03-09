import random
import pygame
from dino_runner.utils.constants import HAMMER, HAMMER_TYPE, DEFAULT_TYPE
from dino_runner.components.power_ups.power_up import PowerUp


class Hammer(PowerUp):
    def __init__(self):
        super().__init__(HAMMER, HAMMER_TYPE)
        self.rect.midbottom = (self.rect.x, 310) 
        self.throw = False
    
    def update_throw(self, dinosaur, game):
        self.rect.x += 2
        self.rect.y = dinosaur.rect.y 
        if dinosaur.hammer_qtty < 0:
            dinosaur.type = DEFAULT_TYPE       
        else:
            dinosaur.type = HAMMER_TYPE
        
        for obstacle in game.obstacle_manager.obstacles:
            if self.rect.colliderect(obstacle):
                game.obstacle_manager.obstacles.remove(obstacle)

        self.draw(game.screen)


