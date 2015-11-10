from pygame import draw
from ping.pong.util import Utils

__all__ = ['Paddle']


class Paddle:
    _COLOR = (255,255,255)
    _SPEED = 300

    def __init__(self, x, y, w, h, key_l, key_r, key_d, key_u, surface, dt, screen_size):
        self.pos = [x,y]
        self.dim = [w,h]

        self.key_l = key_l
        self.key_r = key_r
        self.key_d = key_d
        self.key_u = key_u

        self.screen_size = screen_size
        self.surface = surface
        self.dt = dt

    def move(self, rel_x, rel_y):
        self.pos[0] += self.dt*rel_x
        self.pos[1] -= self.dt*rel_y
        self.pos[0] = Utils.clamp(self.pos[0],0,self.screen_size[0]-self.dim[0])
        self.pos[1] = Utils.clamp(self.pos[1],0,self.screen_size[1]-self.dim[1])

    def update(self, key):
        speed = self._SPEED
        if self.key_l and key[self.key_l]: self.move(-speed, 0)
        if self.key_r and key[self.key_r]: self.move(speed, 0)
        if self.key_d and key[self.key_d]: self.move(0, -speed)
        if self.key_u and key[self.key_u]: self.move(0, speed)

    def draw(self, color):
        draw.rect(self.surface,
                         color,
                         (self.pos[0],self.pos[1],self.dim[0],self.dim[1]),
                         0)
        draw.rect(self.surface,
                         self._COLOR,
                         (self.pos[0],self.pos[1],self.dim[0],self.dim[1]),
                         1)
