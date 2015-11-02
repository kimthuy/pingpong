import pygame
import sys, os, traceback
from math import *
from ping.pong import Pong

if sys.platform == 'win32' or sys.platform == 'win64':
    os.environ['SDL_VIDEO_CENTERED'] = '1'

if __name__ == '__main__':
    try:
        if len(sys.argv) > 1:
            os.chdir(sys.argv[1])
        Pong()
    except Exception as e:
        tb = sys.exc_info()[2]
        traceback.print_exception(e.__class__, e, tb)
        pygame.quit()
        input()
        sys.exit()

