import pygame

__all__ = ['Menu']


class Menu:
    _IS_SELECTED = 0

    def __init__(self, surface, text, font_size, x, y):
        self.font_size = font_size
        self.font = {
            self.font_size: pygame.font.Font("../font/FEASFBI.TTF", self.font_size),
        }

        self.text = text
        self.surface = surface
        self.x = x
        self.y = y

    def draw_menu(self, color):
        menu_text = self.font[self.font_size].render(self.text, True, color)
        self.surface.blit(menu_text, (self.x, self.y))
