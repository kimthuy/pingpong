import pygame
from pygame.locals import *
from math import *
from ping.pong.object.player import Player
from ping.pong.object.paddle import Paddle
from ping.pong.object.ball import Ball
from ping.pong.util import Utils
from ping.pong.screen.base_screen import *
from ping.pong.screen.game_screen import *
from ping.pong.screen.menu_screen import *

class Pong:
    def __init__(self):
        pygame.display.init()
        pygame.font.init()
        pygame.mixer.init(buffer=0)
        self.screen_size = [800,500]
        self.surface = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption("Ping Pang Pong - v.3.0.0 - Ian Mallett - 2012")
        game_screen = ScreenGame(self.screen_size, self.surface)
        game_screen.init_screen()
        game_screen.play()
