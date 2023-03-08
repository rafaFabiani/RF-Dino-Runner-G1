import random
from dino_runner.components.obstacles.osbtacle import Obstacle
from dino_runner.utils.constants import BIRD, SCREEN_HEIGHT, SCREEN_WIDTH   

class Bird(Obstacle):
    def __init__(self):
        super().__init__(BIRD[0])
        self.step = 0
        self.rect.y = random.randint(200, (SCREEN_HEIGHT - 325))

    def update(self, game_speed, obstacles):
        self.image = BIRD[self.step // 5]
        self.step += 1
        if self.step >= 10:
            self.step = 0
        super().update(game_speed, obstacles)
