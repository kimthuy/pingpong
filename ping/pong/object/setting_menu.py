from ping.pong.object.menu import Menu

__all__ = ['SettingMenu']


class SettingMenu(Menu):
    is_selected = False
    is_check = False
    SELECTED_COLOR = (255,255,255)
    UNSELECT_COLOR = (128,255,0)
    CHECKED_COLOR = (128,128,128)

    def selected(self):
        self.is_selected = True
        color = self.SELECTED_COLOR
        self.update(color)

    def unselect(self):
        self.is_selected = False
        color = self.CHECKED_COLOR if self.is_check else self.UNSELECT_COLOR
        self.update(color)

    def check(self):
        self.is_check = True
        color = self.CHECKED_COLOR

    def uncheck(self):
        self.is_check = False
        color = self.SELECTED_COLOR

    def init_view(self):
        if self.is_selected:
            color = self.SELECTED_COLOR
        elif self.is_check:
            color = self.CHECKED_COLOR
        else:
            color = self.UNSELECT_COLOR
        self.update(color)

    def toggle(self):
        self.is_check = not self.is_check
        color = self.CHECKED_COLOR if self.is_check else self.SELECTED_COLOR
        self.update(color)
