#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from ping.pong.screen.base_screen import BaseScreen
from ping.pong.util.setting import Setting
from ping.pong.util import Utils

__all__ = ['HighScoreScreen']


class HighScoreScreen(BaseScreen):

    def __init__(self, base_game, surface):
        BaseScreen.__init__(self)
        self.base_game = base_game
        self.status = False
        self.surface = surface
        self.dt = 1.0/60.0
        self.bg = pygame.image.load(Utils.get_path('image/menu-bg.png'))
        self.font = {
            20: pygame.font.Font(Utils.get_path('font/ActualBook.otf'), 20),
            55: pygame.font.Font(Utils.get_path('font/ActualBook.otf'), 55)
        }

        self.high_score_list = []
        self.get_high_score()

    def start_screen(self):
        self.init_screen()
        while True:
            if not self.get_input():
                break
            pygame.display.update()

    def end_screen(self):
        self.status = True

    def init_screen(self):
        self.surface.blit(self.bg, (0, 0))

        menu_text = self.font[55].render('High Score', True, (225,255,225))
        self.surface.blit(menu_text, (370, 60))

        self.draw_high_score()
        pygame.display.flip()

    def get_high_score(self):
        high_score_file = open(Utils.get_path('doc/high-score.txt'), 'r')
        stuff = high_score_file.readlines()
        for line in stuff:
            self.high_score_list.append(line)
        high_score_file.close()

    def draw_high_score(self):
        for index, line in enumerate(self.high_score_list):
            y = 150 + index*40
            x = 560 + index*3
            u = unicode(line, 'utf8')
            menu_text = self.font[20].render(u, True, (128,255,0))
            self.surface.blit(menu_text, (x, y))

    def get_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit_game()
                elif event.key == pygame.K_BACKSPACE:
                    self.base_game.switch_screen(Setting.MENU_SCREEN)
                    return False
        return True
