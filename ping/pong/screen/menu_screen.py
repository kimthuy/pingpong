import pygame
from ping.pong.screen.base_screen import BaseScreen
from ping.pong.util.setting import Setting
from ping.pong.object.menu import Menu

from ping.pong.util import Utils

__all__ = ['MenuScreen']


class MenuScreen(BaseScreen):

    def __init__(self, base_game, surface):
        BaseScreen.__init__(self)
        self.base_game = base_game
        self.status = False
        self.surface = surface
        self.bg = pygame.image.load(Utils.get_path('image/menu-bg.png'))

        self.menu_text = Menu(self.surface, 'Menu', 70, 565, 30)

        menu_single = Menu(self.surface, 'Single Player', 35, 560, 120)
        menu_single.is_selected = True
        menu_multi = Menu(self.surface, 'Multi Player', 35, 565, 160)
        menu_setting = Menu(self.surface, 'Settings', 35, 570, 200)
        menu_high_score = Menu(self.surface, 'High Score', 35, 575, 240)
        menu_exit = Menu(self.surface, 'Exit Game', 35, 577, 280)

        self.menus = [menu_single, menu_multi, menu_setting, menu_high_score, menu_exit]

    def start_screen(self):
        self.init_screen()
        while True:
            if not self.get_input():
                break
            pygame.display.update()

    def init_screen(self):
        self.surface.blit(self.bg, (0, 0))
        for menu in self.menus:
            menu.init_view()
        self.menu_text.init_view()
        pygame.display.flip()

    def get_input(self):
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
                    self.play_sound(self.check_sound)
                    for index, menu in enumerate(self.menus):
                        if menu.is_selected:
                            if index == 0:
                                Setting.PLAY_MODE = Setting.SINGLE_MODE
                                self.base_game.switch_screen(Setting.GAME_SCREEN)
                            elif index == 1:
                                Setting.PLAY_MODE = Setting.MULTI_MODE
                                self.base_game.switch_screen(Setting.GAME_SCREEN)
                            elif index == 2:
                                self.base_game.switch_screen(Setting.SETTING_SCREEN)
                            elif index == 3:
                                self.base_game.switch_screen(Setting.HIGH_SCORE_SCREEN)
                            elif index == 4:
                                self.quit_game()
                            break
                    return False
        return True


