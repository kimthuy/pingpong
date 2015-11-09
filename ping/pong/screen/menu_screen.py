import pygame
from pygame.locals import *
from ping.pong.screen.base_screen import BaseScreen
from ping.pong.util.setting import Setting
from ping.pong.object.menu import Menu

from ping.pong.util import Utils

__all__ = ['MenuScreen']


class MenuScreen(BaseScreen):

    def __init__(self, base_game, surface):
        self.base_game = base_game
        self.status = False
        self.surface = surface
        self.bg = pygame.image.load(Utils.get_path('image/menu-bg.png'))

        self.menu_text = Menu(self.surface, 'Menu', 70, 565, 60)

        menu_single = Menu(self.surface, 'Single Player', 35, 560, 150)
        menu_single.is_selected = Menu.SELECT
        menu_multi = Menu(self.surface, 'Multi Player', 35, 565, 190)
        menu_high_score = Menu(self.surface, 'High Score', 35, 570, 230)
        menu_exit = Menu(self.surface, 'Exit Game', 35, 572, 270)

        self.menus = [menu_single, menu_multi, menu_high_score, menu_exit]
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

    def init_screen(self):
        self.surface.blit(self.bg, (0, 0))
        for menu in self.menus:
            menu.draw_menu()
        self.menu_text.draw_menu()
        pygame.display.flip()

    def get_input(self):
        # keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit_game()
                elif event.key == pygame.K_DOWN:
                    self.menu_move(1)
                elif event.key == pygame.K_UP:
                    self.menu_move(-1)
                elif event.key == pygame.K_RETURN:
                    self.sounds['theme'].stop()
                    for index, menu in enumerate(self.menus):
                        if menu.is_selected == Menu.SELECT:
                            if index == 0:
                                Setting.PLAY_MODE = Setting.SINGLE_MODE
                                self.base_game.switch_screen(Setting.GAME_SCREEN)
                            elif index == 1:
                                Setting.PLAY_MODE = Setting.MULTI_MODE
                                self.base_game.switch_screen(Setting.GAME_SCREEN)
                            elif index == 2:
                                self.base_game.switch_screen(Setting.HIGH_SCORE_SCREEN)
                            elif index == 3:
                                self.quit_game()
                            break
                    return False
        return True


