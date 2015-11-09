#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
import os
import sys
from pygame.locals import *
from ping.pong.object.menu import Menu
from ping.pong.util.setting import *
from ping.pong.util import Utils

__all__ = ['HighScoreScreen']


class HighScoreScreen:

    def __init__(self, base_game, surface):
        self.base_game = base_game
        self.status = False
        self.surface = surface
        self.dt = 1.0/60.0
        self.bg = pygame.image.load(Utils.get_path('image/menu-bg.png'))
        self.font = {
            20: pygame.font.Font(Utils.get_path('font/ActualBook.otf'), 20),
            55: pygame.font.Font(Utils.get_path('font/ActualBook.otf'), 55)
        }
        self.sounds = {
            "theme": pygame.mixer.Sound(Utils.get_path('sound/menu-screen-theme.wav'))
        }
        self.sounds["theme"].set_volume(0.25)

        self.high_score_list = []
        self.get_high_score()

    def start_screen(self):
        clock = pygame.time.Clock()
        self.sounds["theme"].play(-1)
        while True:
            if not self.get_input():
                break
            self.init_screen()
            clock.tick(60)
            self.dt = 1.0/Utils.clamp(clock.get_fps(), 30, 90)
            pygame.display.update()
        pygame.quit()
        sys.exit()

    def end_screen(self):
        self.status = True

    def init_screen(self):
        self.surface.blit(self.bg, (0, 0))

        menu_text = self.font[55].render("High Score", True, (225,255,225))
        self.surface.blit(menu_text, (370, 60))

        self.draw_high_score()
        pygame.display.flip()

    def get_high_score(self):
        file = open(Utils.get_path('doc/high-score.txt'), "r")
        stuff = file.readlines()
        for line in stuff:
            self.high_score_list.append(line)
        file.close()

    def draw_high_score(self):
        i = 0
        for line in self.high_score_list:
            y = 150 + i*40
            u = unicode(line, 'utf8')
            menu_text = self.font[20].render(u, True, (128,255,0))
            self.surface.blit(menu_text, (560, y))
            i += 1

    def get_input(self):
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT: return False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE: return False
                elif event.key == K_ESCAPE or event.key == K_BACKSPACE:
                    self.sounds["theme"].stop()
                    self.base_game.switch_screen(Setting.MENU_SCREEN)
        return True