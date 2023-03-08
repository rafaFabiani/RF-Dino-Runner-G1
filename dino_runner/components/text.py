import pygame
from dino_runner.utils.constants import FONT_STYLE

class MenuText:
    def __init__(self, text, size):
        self.font = pygame.font.Font(FONT_STYLE, size)
        self.text = text

    def draw(self, screen, x, y):
        text = self.font.render(self.text, False, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (x, y)
        screen.blit(text, text_rect)

