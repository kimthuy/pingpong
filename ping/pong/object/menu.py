import pygame

__all__ = ['Menu']


class Menu:
    _SELECT = 1
    _NON_SELECT = 0
    _IS_SELECTED = _NON_SELECT

    def __init__(self, surface, text, font_size, x, y):
        self.font_size = font_size
        self.font = {
            self.font_size: pygame.font.Font("../font/FEASFBI.TTF", self.font_size),
        }

        self.text = text
        self.surface = surface
        self.x = x
        self.y = y

    def draw_menu(self):
        if self._IS_SELECTED == self._SELECT:
            color = (255,255,255)
        elif self._IS_SELECTED == self._NON_SELECT:
            color = (128,255,0)

        menu_text = self.font[self.font_size].render(self.text, True, color)
        self.surface.blit(menu_text, (self.x, self.y))
