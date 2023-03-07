import random
from dino_runner.components.obstacles.osbtacle import Obstacle
from dino_runner.utils.constants import BIRD, SCREEN_HEIGHT, SCREEN_WIDTH   

class Bird(Obstacle):
    def __init__(self):
        self.image = BIRD[0]
        self.step = 0
        self.BIRD_Y = random.randint(200, (SCREEN_HEIGHT - 325))
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        

    def update(self, game_speed, obstacles):
        image = BIRD[self.step // 5]
        self.image = image
        self.rect.y = self.BIRD_Y
        self.step += 1
        if self.step >= 10:
            self.step = 0
        super().update(game_speed, obstacles)
