from pygame import font
from ping.pong.util import Utils

__all__ = ['Menu']


class Menu:

    SELECTED_COLOR = (255,255,255)
    UNSELECT_COLOR = (128,255,0)

    is_selected = False

    def __init__(self, surface, text, font_size, x, y):
        self.font_size = font_size
        self.font = {
            self.font_size: font.Font(Utils.get_path('font/FEASFBI.TTF'), self.font_size),
        }

        self.text = text
        self.surface = surface
        self.x = x
        self.y = y

    def selected(self):
        self.is_selected = True
        color = self.SELECTED_COLOR
        self.update(color)

    def unselect(self):
        self.is_selected = False
        color = self.UNSELECT_COLOR
        self.update(color)

    def init_view(self):
        color = self.SELECTED_COLOR if self.is_selected else self.UNSELECT_COLOR
        self.update(color)

    def update(self, color):
        menu_text = self.font[self.font_size].render(self.text, True, color)
        self.surface.blit(menu_text, (self.x, self.y))


