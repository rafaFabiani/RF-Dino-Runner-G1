import random
from dino_runner.components.clouds.cloud import Cloud

class CloudManager:
    def __init__(self):
        self.clouds: list[Cloud] = []
        self.when_appears = 0

    def update(self, game_speed, score):
        if score == self.when_appears:
            self.clouds.append(Cloud())
            self.when_appears += random.randint(0, 20)

        for cloud in self.clouds:
            cloud.update(game_speed, self.clouds)

    def draw(self, screen):
        for cloud in self.clouds:
            cloud.draw(screen)
    
    def reset(self):
        self.clouds = []
        self.when_appears = 0
