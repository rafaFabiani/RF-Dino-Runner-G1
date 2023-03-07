import sys
from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH
print(sys.path)

class Obstacle(Sprite):
    def __init__(self, image):
        self.image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.remove(self)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))





