__all__ = ['MenuScreen']
class MenuScreen:

    def __init__(self, screen_size, surface):
        self.status =False
        self.surface = surface
        self.screen_size = screen_size
        self.list_item = []

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