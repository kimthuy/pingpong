import pygame
import sys
from ping.pong.object.menu import Menu

__all__ = ['BaseScreen']


class BaseScreen:

    def __init__(self):
        self.status =False

    def start_screen(self):
        self.init_screen()
        self.status = True
        self.play()

    def end_screen(self):
        self.status = True

    def init_screen(self):
        pass

    def play(self):
        pass

    def menu_move(self, step):
        self.sounds['select-menu'].play()
        for index, menu in enumerate(self.menus):
            if menu.is_selected == Menu.SELECT:
                menu.is_selected = Menu.NON_SELECT
                menu.draw_menu()
                selected_index = (index + step) % len(self.menus)
                self.menus[selected_index].is_selected = Menu.SELECT
                self.menus[selected_index].draw_menu()
                break

    def quit_game(self):
        pygame.quit()
        sys.exit()