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
        self.font = {
            18: pygame.font.SysFont("Times New Roman",18),
            72: pygame.font.SysFont("Times New Roman",72)
        }


    def play(self):
        pass