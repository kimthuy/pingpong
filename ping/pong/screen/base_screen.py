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