import pygame
from ping.pong.object.menu import Menu
from ping.pong.object.setting_menu import SettingMenu
from ping.pong.util.setting import Setting
from ping.pong.util import Utils
from ping.pong.screen.base_screen import BaseScreen

__all__ = ['SettingScreen']


class SettingScreen(BaseScreen):

    def __init__(self, base_game, surface):
        BaseScreen.__init__(self)
        self.base_game = base_game
        self.status = False
        self.surface = surface
        self.dt = 1.0/60.0
        self.bg = pygame.image.load(Utils.get_path('image/menu-bg.png'))

        self.menu_text = Menu(self.surface, 'Setting', 70, 565, 60)
        self.menu_text.is_selected = True
        menu_sound = SettingMenu(self.surface, 'Sound', 35, 560, 150)
        menu_sound.is_selected = True
        menu_music = SettingMenu(self.surface, 'Music', 35, 565, 190)
        menu_exit = Menu(self.surface, 'Back', 35, 570, 230)

        self.menus = [menu_sound, menu_music, menu_exit]

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
                                Setting.SOUND = not Setting.SOUND
                                menu.toggle()
                            if index == 1:
                                Setting.MUSIC = not Setting.MUSIC
                                menu.toggle()
                                self.base_game.update_music(Setting.MUSIC)
                            elif index == 2:
                                self.base_game.switch_screen(Setting.MENU_SCREEN)
                                return False
        return True