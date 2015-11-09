__author__ = 'Luong'
__all__ = ['Setting']


class Setting:
    SINGLE_MODE = 1
    MULTI_MODE = 2
    PLAY_MODE = MULTI_MODE

    MENU_SCREEN = 0
    SETTING_SCREEN = 1
    GAME_SCREEN = 2
    HIGH_SCORE_SCREEN = 3

    between_rounds_timer = 3.0

    def __init__(self):
        global PLAY_MODE
