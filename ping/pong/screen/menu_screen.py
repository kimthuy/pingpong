__all__ = ['MenuScreen']
import pygame
import sys, os, traceback
from pygame.locals import *
from math import *
from ping.pong.object.player import Player
from ping.pong.object.paddle import Paddle
from ping.pong.object.ball import Ball
from ping.pong.object.menu_item import MenuItem
from ping.pong.util import Utils
from ping.pong.screen.base_screen import *
from ping.pong.util.setting import *
class MenuScreen:

    def __init__(self, screen_size, surface):
        self.stop =False
        self.surface = surface
        self.screen_size = screen_size
        self.list_item = []
        self.selected_item = 0

    def start_screen(self):
        self.init_screen()
        self.status = True
        self.play()

    def end_screen(self):
        self.stop = True

    def init_screen(self):
        white = (255,255,255)
        rect = self.surface.get_rect()
        game_start = MenuItem('Game Start', self.surface)
        game_start.draw(rect, white)
        game_start.set_selected(True)
        self.list_item.append(game_start)
        config_menu = MenuItem('Game Setting', self.surface)
        rect.y += 30
        config_menu.draw(rect, white)
        self.list_item.append(config_menu)

    def play(self):
        while True:
            if not self.get_input():
                break
            pygame.display.flip()

    def get_input(self):
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT:
                return False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return False
                if event.key == K_UP:
                    self._set_selected_item(self._get_item_next())
                if event.key == K_DOWN:
                    self._set_selected_item(self._get_item_prev())
        return True

    def _get_item_next(self):
        return (self.selected_item + 1) % len(self.list_item)

    def _get_item_prev(self):
        return (self.selected_item - 1 + len(self.list_item)) % len(self.list_item)

    def _set_selected_item(self, index):
        self.list_item[self.selected_item].set_selected(False)
        self.list_item[index].set_selected(True)
        self.selected_item = index