__author__ = 'Luong'
__all__ = ['Setting']


class Setting:

    _SINGLE_MODE = 1
    _MULTI_MODE = 2
    _PLAY_MODE = _MULTI_MODE

    MENU_SCREEN = 0
    SETTING_SCREEN = 1
    GAME_SCREEN = 2

    between_rounds_timer = 3.0