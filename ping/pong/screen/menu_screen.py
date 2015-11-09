import pygame
import sys
from pygame.locals import *
from ping.pong.util.setting import Setting
from ping.pong.object.menu import Menu

from ping.pong.util import Utils

__all__ = ['MenuScreen']


class MenuScreen:

    def __init__(self, base_game, surface):
        self.base_game = base_game
        self.status = False
        self.surface = surface
        self.bg = pygame.image.load(Utils.get_path('image/menu-bg.png'))

        menu_text = Menu(self.surface, 'Menu', 70, 565, 60)
        menu_text.is_selected = Menu.SELECT
        menu_signle = Menu(self.surface, 'Single Player', 35, 560, 150)
        menu_signle.is_selected = Menu.SELECT
        menu_multi = Menu(self.surface, 'Multi Player', 35, 565, 190)
        menu_highscore = Menu(self.surface, 'High Score', 35, 570, 230)
        menu_exit = Menu(self.surface, 'Exit Game', 35, 572, 270)

        self.menus = [menu_text, menu_signle, menu_multi, menu_highscore, menu_exit]
        self.sounds = {
            'theme': pygame.mixer.Sound(Utils.get_path('sound/menu-screen-theme.wav')),
            'select-menu': pygame.mixer.Sound(Utils.get_path('sound/select-menu.wav')),
            'click-menu': pygame.mixer.Sound(Utils.get_path('sound/select-menu.wav'))
        }
        self.sounds['theme'].set_volume(0.25)
        self.sounds['select-menu'].set_volume(2)

    def start_screen(self):
        self.sounds['theme'].play(-1)
        self.init_screen()
        while True:
            if not self.get_input():
                break
            pygame.display.update()
        pygame.quit()
        sys.exit()

    def init_screen(self):
        self.surface.blit(self.bg, (0, 0))
        self.init_menu()
        pygame.display.flip()

    def update_screen(self):
        self.init_menu()
        pygame.display.flip()

    def init_menu(self):
        i = 0
        for menu in self.menus:
            if i == 0: menu.draw_menu()
            else:
                if menu.is_selected == Menu.SELECT:
                    menu.draw_menu()
                else:
                    menu.draw_menu()
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
                        if i > 0 and menu.is_selected == Menu.SELECT:
                            if i < len(self.menus) - 1:
                                self.menus[i + 1].is_selected = Menu.SELECT
                            elif i == len(self.menus) - 1:
                                self.menus[1].is_selected = Menu.SELECT
                            is_first_time = False
                            menu.is_selected = Menu.NON_SELECT
                            break
                        i += 1
                    if is_first_time:
                        self.menus[1].is_selected = Menu.SELECT
                    self.sounds['select-menu'].play()
                    # pygame.display.flip()
                    self.update_screen()

                elif event.key == K_UP:
                    i = 0
                    is_first_time = True
                    for menu in self.menus:
                        if i > 0 and menu.is_selected == Menu.SELECT:
                            if i == 1:
                                self.menus[len(self.menus) - 1].is_selected = Menu.SELECT
                            elif i >= 2 and i <= len(self.menus) - 1:
                                self.menus[i - 1].is_selected = Menu.SELECT
                            is_first_time = False
                            menu.is_selected = Menu.NON_SELECT
                            break
                        i += 1
                    if is_first_time:
                        self.menus[3].is_selected = Menu.SELECT
                    self.sounds['select-menu'].play()
                    # pygame.display.flip()
                    self.update_screen()

                elif event.key == K_RETURN:
                    i = 0
                    for menu in self.menus:
                        if menu.is_selected == Menu.SELECT:
                            if i == 1:
                                self.sounds['theme'].stop()
                                Setting.PLAY_MODE = Setting.SINGLE_MODE
                                self.base_game.switch_screen(Setting.GAME_SCREEN)
                            elif i == 2:
                                self.sounds['theme'].stop()
                                Setting.PLAY_MODE = Setting.MULTI_MODE
                                self.base_game.switch_screen(Setting.GAME_SCREEN)
                            elif i == 3:
                                self.sounds['theme'].stop()
                                self.base_game.switch_screen(Setting.HIGH_SCORE_SCREEN)
                                continue
                            elif i == 4:
                                return False
                        i += 1
        return True