from ping.pong.object.menu import Menu

__all__ = ['SettingMenu']


class SettingMenu(Menu):
    is_selected = False
    is_check = True
    CHECK_SELECT = (204,255,102)
    CHECK_UNSELECT = (128,255,0)
    UNCHECK_SELECT = (255,255,255)
    UNCHECK_UNSELECT = (50, 50, 50)

    def selected(self):
        self.is_selected = True
        color = self.CHECK_SELECT if self.is_check else self.UNCHECK_SELECT
        self.update(color)

    def unselect(self):
        self.is_selected = False
        color = self.CHECK_UNSELECT if self.is_check else self.UNCHECK_UNSELECT
        self.update(color)

    def init_view(self):
        if self.is_selected and self.is_check:
            color = self.CHECK_SELECT
        elif self.is_selected and not self.is_check:
            color = self.UNCHECK_SELECT
        elif self.is_check:
            color = self.CHECK_UNSELECT
        else:
            color = self.UNCHECK_UNSELECT
        self.update(color)

    def toggle(self):
        self.is_check = not self.is_check
        color = self.CHECK_SELECT if self.is_check else self.UNCHECK_SELECT
        self.update(color)
