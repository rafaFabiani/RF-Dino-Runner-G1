import pygame
from dino_runner.components.power_ups.hammer import Hammer
from pygame.sprite import Sprite
from dino_runner.components.text import MenuText

from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING, DEFAULT_TYPE, DUCKING_SHIELD, JUMPING_SHIELD, RUNNING_SHIELD, SHIELD_TYPE, SCREEN_WIDTH, HAMMER_TYPE, RUNNING_HAMMER, DUCKING_HAMMER, JUMPING_HAMMER 

RUNNING_HEIGHT = RUNNING[0].get_height()
DUCKING_HEIGHT = DUCKING[0].get_height()

DINO_RUNNING = "running"
DINO_JUMPING = "jumping"
DINO_DUCKING = "ducking"

DUCK_IMG = { DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER}
JUMP_IMG = { DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER}
RUN_IMG = { DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER}


class Dinosaur(Sprite):
    POSITION_X = 80
    POSITION_Y = 310
    JUMP_VELOCITY = 8.5

    def __init__(self):
        self.type = DEFAULT_TYPE
        self.power_up_time_up = 0
        self.image = RUN_IMG[self.type][0]
        self.rect = self.image.get_rect(midbottom = (self.POSITION_X, self.POSITION_Y))
        self.rect.x = self.POSITION_X
        self.rect.y = self.POSITION_Y
        self.step = 0
        self.action = DINO_RUNNING
        self.hammer_qtty = 0
        self.jump_velocity = self.JUMP_VELOCITY
        
    def update(self, user_input, game):
        if self.action == DINO_RUNNING:
            self.run()

        elif self.action == DINO_JUMPING:
            self.jump()

        elif self.action == DINO_DUCKING:
            self.ducking()

        if self.action != DINO_JUMPING:
            if user_input[pygame.K_DOWN]:
                self.action = DINO_DUCKING

            elif user_input[pygame.K_SPACE]:
                self.action = DINO_JUMPING

            else:
                self.action = DINO_RUNNING
        
        if self.type == HAMMER_TYPE: 
            if user_input[pygame.K_LEFT] and self.hammer_qtty > 0:
                self.hammer_qtty -= 1
                self.hammer.throw = True

            if self.hammer.throw:
                self.hammer.update_throw(self, game)

    def run(self):
        self.image = RUN_IMG[self.type][self.step // 5] 
        self.rect.y = self.POSITION_Y
        self.step += 1
        if self.step >= 10:
            self.step = 0

    def jump(self):
        self.image = JUMP_IMG[self.type]
        self.jump_velocity -= 0.8
        self.rect.y -= self.jump_velocity * 4 
            
        if self.jump_velocity < -self.JUMP_VELOCITY:
            self.jump_velocity = self.JUMP_VELOCITY
            self.action = DINO_RUNNING
            self.rect.y = self.POSITION_Y

    def ducking(self):
        self.rect.y = self.POSITION_Y + RUNNING_HEIGHT - DUCKING_HEIGHT
        self.image = DUCK_IMG[self.type][self.step // 5]
        self.step += 1
        if self.step >= 10:
            self.step = 0

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def on_pick_power_up(self, power_up):
        self.type = power_up.type
        if self.type == HAMMER_TYPE:
            self.hammer = Hammer()
            self.hammer_qtty = 3

        if self.type == SHIELD_TYPE:
            self.power_up_time_up = power_up.start_time + (power_up.duration * 1000)

    def check_power_up(self, screen):
        time_to_show = 0
        if self.type == SHIELD_TYPE:
            time_to_show = round((self.power_up_time_up - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show > 0:
                text = MenuText(f"{self.type.capitalize()} enabled for {time_to_show} seconds", 16)
                text.draw(screen, SCREEN_WIDTH // 2, 50)
            else:
                self.type = DEFAULT_TYPE
                self.power_up_time_up = 0

        elif self.type == HAMMER_TYPE:
            text = MenuText(f"{self.hammer_qtty} {self.type.capitalize()}(S), left", 16)
            text.draw(screen, SCREEN_WIDTH // 2, 50)

    def reset(self):
        self.power_up_time_up = 0
        self.type = DEFAULT_TYPE
            
        
            


        
    
