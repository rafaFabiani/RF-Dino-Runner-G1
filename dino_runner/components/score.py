import pygame
from dino_runner.components.text import MenuText
from dino_runner.utils.constants import FONT_STYLE

class Score:
    def __init__(self):
        self.score = 0
        self.font = pygame.font.Font(FONT_STYLE, 24)

    def update(self, game):
        self.score += 1
        if self.score % 100 == 0:
            game.game_speed += 2

    def draw(self, screen):        
        text = MenuText(f"Score: {self.score}", 24)
        text.draw(screen, 950, 30)

    def reset(self):
        self.score = 0
