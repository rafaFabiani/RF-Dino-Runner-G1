import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import SMALL_CACTUS


class Cactus(Obstacle):
    def __init__(self):
        obstacle_type = random.randint(0, 2)
        if obstacle_type == 0:
            self.generate_small_cactus()
        elif obstacle_type == 1:
            self.generate_large_cactus()
        else:
            self.generate_bird()

    def generate_small_cactus(self):
        super().__init__(image)
        pass

    def generate_large_cactus(self):
        pass

    def generate_bird(self):
        pass
        



