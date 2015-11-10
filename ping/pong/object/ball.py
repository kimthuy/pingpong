from pygame import draw
import random
from math import *
from ping.pong.util import Utils
__all__ = ['Ball']


class Ball:
    _COLOR = (255, 255, 255)
    _SIZE = 8
    _LIGHT = 255/10
    # speed_increase = [0, 0]

    def __init__(self, x, y, speed, surface):
        self.pos = [x,y]
        self.trail = []
        self.surface = surface

        angle = pi / 2
        while abs(cos(angle)) < 0.1 or abs(cos(angle)) > 0.9:
            angle = radians(random.randint(0, 360))
        self.speed = [speed*cos(angle), speed*sin(angle)]
        # self.speed_increase = [self.speed[0]*0.2, self.speed[1]*0.2]

        self.radius = self._SIZE

    def update(self):
        self.trail = [self.pos + [self.radius]] + self.trail
        while len(self.trail) > 10: self.trail = self.trail[:-1]

    def move(self, dt):
        self.pos[0] += dt*self.speed[0]
        self.pos[1] += dt*self.speed[1]

    def speed_up(self):
        factor = 1.1
        self.speed[0] *= factor
        self.speed[1] *= factor
        # self.speed[0] += self.speed_increase[0]
        # self.speed[1] += self.speed_increase[1]

    def draw(self):
        # light = self._LIGHT
        # for px, py, r in self.trail[::-1]:
        #     pygame.draw.circle(self.surface,
        #                        (light,0,0),
        #                        list(map(Utils.round_int,[px,py])),
        #                        r)
        #     light += self._LIGHT
        draw.circle(self.surface,
                           self._COLOR,
                           list(map(Utils.round_int, self.pos)),
                           self.radius)
