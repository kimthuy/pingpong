from pygame import (
    quit,
    mixer
)
from sys import exit
from ping.pong.util.setting import Setting
from ping.pong.util import Utils

__all__ = ['BaseScreen']


class BaseScreen:

    def __init__(self):
        self.status = False
        self.select_sound = mixer.Sound(Utils.get_path('sound/select-menu.wav'))
        self.select_sound.set_volume(2)
        self.check_sound = mixer.Sound(Utils.get_path('sound/select-menu.wav'))
        self.check_sound.set_volume(5)

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
        self.play_sound(self.select_sound)
        for index, menu in enumerate(self.menus):
            if menu.is_selected:
                menu.unselect()
                selected_index = (index + step) % len(self.menus)
                self.menus[selected_index].selected()
                break

    def play_sound(self, sound):
        if Setting.SOUND:
            sound.play()

    def quit_game(self):
        quit()
        exit()