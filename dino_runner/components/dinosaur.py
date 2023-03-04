import pygame
from pygame.surface import Surface
from pygame.sprite import Sprite

from dino_runner.utils.constants import RUNNING, JUMPING

DINO_RUNNING = "running"
DINO_JUMPING = "jumping"


class Dinosaur(Sprite):
    POSITION_X = 80
    POSITION_Y = 310
    JUMP_VELOCITY = 8.5

    def __init__(self):
        self.image = RUNNING[0]
        self.rect = self.image.get_rect()
        self.rect.x = self.POSITION_X
        self.rect.y = self.POSITION_Y
        self.step = 0
        self.action = DINO_RUNNING
        self.jump_velocity = self.JUMP_VELOCITY


    def update(self, user_input):
        if self.action == DINO_RUNNING:
            self.run()

        elif self.action == DINO_JUMPING:
            self.jump()

        if self.action != DINO_JUMPING:

            if user_input[pygame.K_SPACE]:
                self.action = DINO_JUMPING

            else:
                self.action = DINO_RUNNING


    def run(self):
            self.image = RUNNING[self.step // 5] 
            self.step += 1
            if self.step >= 10:
                self.step = 0

    def jump(self):
            self.image = JUMPING
            self.jump_velocity -= 0.8
            self.rect.y -= self.jump_velocity * 4 
            
            if self.jump_velocity < -self.JUMP_VELOCITY:
                self.jump_velocity = self.JUMP_VELOCITY
                self.action = DINO_RUNNING
                self.rect.y = self.POSITION_Y




    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))


        
    
