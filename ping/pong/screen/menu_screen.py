import pygame
import os
import sys
from pygame.locals import *
from ping.pong.util.setting import Setting
from ping.pong.object.menu import Menu
from ping.pong.screen.game_screen import GameScreen

from ping.pong.util import Utils

__all__ = ['MenuScreen']


class MenuScreen:

    def __init__(self, base_game, surface):
        self.base_game = base_game
        self.status =False
        self.surface = surface
        self.font = {
            35: pygame.font.Font("../font/FEASFBI.TTF", 35),
            70: pygame.font.Font("../font/FEASFBI.TTF", 70)
        }
        self.bg = pygame.image.load("../media/image/menu-bg.png")

        menu_text = Menu(self.surface, "Menu", 70, 550, 60)
        menu_start = Menu(self.surface, "Play", 35, 585, 150)
        menu_setting = Menu(self.surface, "Setting", 35, 575, 190)
        menu_exit = Menu(self.surface, "Exit Game", 35, 560, 230)

        self.menus = [menu_text, menu_start, menu_setting, menu_exit]
        self.sounds = {
            "theme": pygame.mixer.Sound("../media/sound/menu-screen-theme.wav"),
            "select-menu": pygame.mixer.Sound("../media/sound/select-menu.wav"),
            "click-menu": pygame.mixer.Sound("../media/sound/select-menu.wav")
        }
        self.sounds["theme"].set_volume(0.25)
        self.sounds["select-menu"].set_volume(2)

    def start_screen(self):
        clock = pygame.time.Clock()
        self.sounds["theme"].play(-1)
        while True:
            if not self.get_input():
                break
            self.init_screen()
            pygame.display.update()
        pygame.quit()
        sys.exit()

    def end_screen(self):
        self.status = True

    def init_screen(self):
        self.surface.blit(self.bg, (0, 0))
        self.init_menu()
        pygame.display.flip()

    def init_menu(self):
        i = 0
        for menu in self.menus:
            if i == 0: menu.draw_menu((255,255,255))
            else:
                if menu.is_selected == 1:
                    menu.draw_menu((255,255,255))
                else:
                    menu.draw_menu((128,255,0))
            i += 1

    def get_input(self):
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT: return False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE: return False
                elif event.key == K_DOWN:
                    i = 0
                    is_first_time = True
                    for menu in self.menus:
                        if menu.is_selected == 1:
                            if i == 1:
                                self.menus[2].is_selected = 1
                            elif i == 2:
                                self.menus[3].is_selected = 1
                            elif i == 3:
                                self.menus[1].is_selected = 1
                            is_first_time = False
                            menu.is_selected = 0
                            break
                        i += 1
                    if is_first_time:
                        self.menus[1].is_selected = 1
                    self.sounds["select-menu"].play()
                    self.init_screen()

                elif event.key == K_UP:
                    i = 0
                    is_first_time = True
                    for menu in self.menus:
                        if menu.is_selected == 1:
                            if i == 1:
                                self.menus[3].is_selected = 1
                            elif i == 2:
                                self.menus[1].is_selected = 1
                            elif i == 3:
                                self.menus[2].is_selected = 1
                            is_first_time = False
                            menu.is_selected = 0
                            break
                        i += 1
                    if is_first_time:
                        self.menus[3].is_selected = 1
                    self.sounds["select-menu"].play()
                    self.init_screen()

                elif event.key == K_RETURN:
                    i = 0;
                    for menu in self.menus:
                        if menu.is_selected == 1 and i == 1:
                            self.sounds["theme"].stop()
                            game_screen = GameScreen([800, 500], self.surface)
                            game_screen.init_screen()
                            game_screen.play()
                        if menu.is_selected == 1 and i == 2:
                            self.sounds["theme"].stop()
                            # setting_screen = SettingScreen(self.surface)
                            # setting_screen.start_screen()
                            self.base_game.switch_screen(Setting.SETTING_SCREEN)
                        elif menu.is_selected == 1 and i == 3: return False
                        i += 1;
        return True