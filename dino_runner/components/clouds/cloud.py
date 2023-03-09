import random
from pygame.sprite import Sprite
from dino_runner.utils.constants import CLOUD, SCREEN_WIDTH

class Cloud(Sprite):
    def __init__(self):
        self.image = CLOUD
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH + 100
        self.rect.y = random.randint(50, 150)

    def update(self, game_speed, clouds):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            clouds.remove(self)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y)) 

