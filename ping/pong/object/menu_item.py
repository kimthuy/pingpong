import pygame
import random
from math import *
from ping.pong.util import Utils
from ping.pong.util.font_manager import cFontManager
__all__ = ['MenuItem']


class MenuItem:

    def __init__(self, text, surface):
        self.text = text
        self.color = (255,0,0)
        self.selected = False
        self.surface = surface
        self.surface.set_colorkey((0, 51, 0))
         # a font of None means to use the default font
        self.fontMgr = cFontManager(((None, 24), (None, 48), ('arial', 24)))


    def set_selected(self, selected):
        self.selected = selected
        if selected:
            pygame.draw.rect(self.surface,(255,0,0),self.font_rect,2)
        else:
            pygame.draw.rect(self.surface,self.surface.get_colorkey(),self.font_rect,2)

    def draw(self, rect,color):
        self.font_rect = self.fontMgr.Draw(self.surface , 'arial', 24, self.text, rect, color,
                    'center', 'top')

    def get_rect(self):
        return self.font_rect
