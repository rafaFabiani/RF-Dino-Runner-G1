from pygame.sprite import Sprite
import random
from dino_runner.utils.constants import SCREEN_WIDTH 


class PowerUp(Sprite):
    def __init__(self, image, type):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.rect.y = random.randint(100, 150)
        self.type = type 
        # Duration of the power up in seconds
        self.duration = random.randint(5, 8)
        # Moment where it has been taken
        self.start_time = 0
        

    def update(self, game_speed, power_ups):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            power_ups.remove(self)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))



    
