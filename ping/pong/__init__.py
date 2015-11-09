import os
import pygame
from pygame.locals import *
from math import *
from ping.pong.object.player import Player
from ping.pong.object.paddle import Paddle
from ping.pong.object.ball import Ball
from ping.pong.util import Utils
from ping.pong.util.setting import Setting
from ping.pong.screen.base_screen import BaseScreen
from ping.pong.screen.game_screen import GameScreen
from ping.pong.screen.menu_screen import MenuScreen
from ping.pong.screen.highscore_screen import HighScoreScreen
from ping.pong.screen.setting_screen import SettingScreen

class Pong:

    menu_screen = None
    setting_screen = None
    game_screen = None
    high_score_screen = None

    def __init__(self):
        pygame.display.init()
        pygame.font.init()
        pygame.mixer.init(buffer=0)
        self.screen_size = [800,500]
        self.surface = pygame.display.set_mode(self.screen_size)

        life_image = pygame.image.load(Utils.get_path('image/icon.png')).convert_alpha()
        pygame.display.set_icon(life_image)
        pygame.display.set_caption("Ping Pong")
        pygame.display.set_icon(life_image)

        self.switch_screen(Setting.MENU_SCREEN)

    def switch_screen(self, screen_index):
        if screen_index == Setting.MENU_SCREEN:
            if not self.menu_screen:
                self.menu_screen = MenuScreen(self, self.surface)
            self.menu_screen.start_screen()
        elif screen_index == Setting.SETTING_SCREEN:
            if not self.setting_screen:
                self.setting_screen = SettingScreen(self, self.surface)
            self.setting_screen.start_screen()
        elif screen_index == Setting.GAME_SCREEN:
            if not self.game_screen:
                self.game_screen = GameScreen(self, self.screen_size, self.surface)
            self.game_screen.init_screen()
            self.game_screen.play()
        elif screen_index == Setting.HIGH_SCORE_SCREEN:
            if not self.high_score_screen:
                self.high_score_screen = HighScoreScreen(self, self.surface)
            self.high_score_screen.start_screen()