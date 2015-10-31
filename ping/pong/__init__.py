import pygame
from pygame.locals import *
from math import *
from ping.pong.object.player import Player
from ping.pong.object.paddle import Paddle
from ping.pong.object.ball import Ball
from ping.pong.util import Utils


class Pong:
    _SINGLE_MODE = 1
    _MULTI_MODE = 2
    _PLAY_MODE = _SINGLE_MODE
    balls = []
    between_rounds_timer = 3.0

    def __init__(self):
        pygame.display.init()
        pygame.font.init()
        pygame.mixer.init(buffer=0)

        self.dt = 1.0/60.0
        self.screen_size = [800,500]
        self.icon = pygame.Surface((1, 1))
        self.icon.set_alpha(0)
        pygame.display.set_icon(self.icon)
        pygame.display.set_caption("Ping Pang Pong - v.3.0.0 - Ian Mallett - 2012")
        self.surface = pygame.display.set_mode(self.screen_size)

        self.sounds = {
            "ping" : pygame.mixer.Sound("data/ping.wav"),
            "click" : pygame.mixer.Sound("data/click.wav"),
            "da-ding" : pygame.mixer.Sound("data/da-ding.wav")
        }
        self.sounds["ping"].set_volume(0.05)
        self.sounds["click"].set_volume(0.5)
        self.sounds["da-ding"].set_volume(0.5)

        self.font = {
            18: pygame.font.SysFont("Times New Roman",18),
            72: pygame.font.SysFont("Times New Roman",72)
        }

        up_key = K_w
        down_key = K_s
        if self._PLAY_MODE == self._SINGLE_MODE:
            up_key = None
            down_key = None

        paddle_1 = Paddle(5, self.screen_size[1]/2-30, 10, 60, None, None, down_key, up_key, self.surface, self.dt, self.screen_size)
        paddle_2 = Paddle(self.screen_size[0]-5-10, self.screen_size[1]/2-30, 10, 60, None, None, K_DOWN, K_UP, self.surface, self.dt, self.screen_size)

        self.paddles = [paddle_1, paddle_2]

        player_1 = Player((0,255,0), self.paddles[:1], self.sounds["da-ding"])
        player_2 = Player((247,52,12), self.paddles[1:], self.sounds["da-ding"])

        self.players = [player_1, player_2]

        self.ball = Ball(self.screen_size[0]/2, self.screen_size[1]/2,200.0, self.surface)

        # start play
        self.play()

    def play(self):
        clock = pygame.time.Clock()
        while True:
            if not self.get_input():
                break
            self.update()
            self.move()
            if self._PLAY_MODE == self._SINGLE_MODE:
                self.ai_move()
            self.draw()
            clock.tick(60)
            self.dt = 1.0/Utils.clamp(clock.get_fps(), 30, 90)

        pygame.quit()
        # sys.exit()

    def get_input(self):
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT: return False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE: return False
        for player in self.players:
            for paddle in player.paddles:
                paddle.update(keys)
        return True

    def update(self):
        for ball in self.balls:
            ball.update()

    def ai_move(self):
        move_speed = 5
        if self.balls and self.balls[0].speed[0] < 0:
            for paddle in self.players[0].paddles:
                if abs(paddle.pos[1]-self.balls[0].pos[1]) > 50:
                    if paddle.pos[1] > self.balls[0].pos[1]:
                        paddle.pos[1] -= move_speed
                    else:
                        paddle.pos[1] += move_speed
                else:
                    paddle.pos[1] = self.balls[0].pos[1] - paddle.dim[1]/2
                # paddle.pos[1] += 5
            paddle.pos[1] = Utils.clamp(paddle.pos[1], 0, self.screen_size[1] - paddle.dim[1])


    def move(self):
        balls2 = []
        for ball in self.balls:
            removed = False
            for subs_tep in range(10): #Do substeps so that it is much harder for the ball to ghost through the paddles.
                ball.move(self.dt/10.0)

                if ball.pos[0] < 0:
                    self.players[1].add_score()
                    removed = True
                    break
                elif ball.pos[0] > self.screen_size[0]:
                    self.players[0].add_score()
                    removed = True
                    break

                if ball.pos[1] < 0:
                    ball.pos[1] = 0
                    ball.speed[1] *= -1
                    self.sounds["ping"].play()
                elif ball.pos[1] > self.screen_size[1]:
                    ball.pos[1] = self.screen_size[1]
                    ball.speed[1] *= -1
                    self.sounds["ping"].play()
                for player in self.players:
                    for paddle in player.paddles:
                        if paddle.pos[0] < ball.pos[0] < paddle.pos[0]+paddle.dim[0] and \
                                        paddle.pos[1] < ball.pos[1] < paddle.pos[1]+paddle.dim[1]:
                            dist_lrdu = [
                                ball.pos[0] - paddle.pos[0],
                                (paddle.pos[0]+paddle.dim[0]) - ball.pos[0],
                                (paddle.pos[1]+paddle.dim[1]) - ball.pos[1],
                                ball.pos[1] - paddle.pos[1],
                            ]
                            dist_min = min(dist_lrdu)
                            if dist_min == dist_lrdu[0]:
                                ball.speed[0] = -abs(ball.speed[0])
                            elif dist_min == dist_lrdu[1]:
                                ball.speed[0] = abs(ball.speed[0])
                            elif dist_min == dist_lrdu[2]:
                                ball.speed[1] = abs(ball.speed[1])
                            elif dist_min == dist_lrdu[3]:
                                ball.speed[1] = -abs(ball.speed[1])
                            self.sounds["click"].play()
                            ball.speed_up()

            if not removed:
                balls2.append(ball)

        if len(balls2) == 0 and len(self.balls) > 0: #someone scored the last of the balls
            self.between_rounds_timer = 3.0

        self.balls = balls2
        if len(self.balls) == 0:
            self.between_rounds_timer -= self.dt
            if self.between_rounds_timer < 0:
                self.balls.append(Ball(self.screen_size[0]/2, self.screen_size[1]/2,200.0, self.surface))
                # balls.append(Ball(screen_size[0]/2,screen_size[1]/2,200.0))
                # balls.append(Ball(screen_size[0]/2,screen_size[1]/2,200.0))

    def draw(self):
        self.surface.fill((12,14,101))

        for ball in self.balls:
            ball.draw()
        for player in self.players:
            for paddle in player.paddles:
                paddle.draw(player.color)

        p1_score_text = self.font[18].render("Score "+str(self.players[0].score),True,(255,255,255))
        p2_score_text = self.font[18].render("Score "+str(self.players[1].score),True,(255,255,255))
        self.surface.blit(p1_score_text,(20,20))
        self.surface.blit(p2_score_text,(self.screen_size[0]-p2_score_text.get_width()-20,20))

        if self.between_rounds_timer > 0:
            alpha = self.between_rounds_timer - int(self.between_rounds_timer)
            alpha = Utils.round_int(255*alpha)

            count = self.font[72].render(str(int(self.between_rounds_timer)+1),True,(alpha,alpha,alpha))

            sc = 0.5*(1.0 + self.between_rounds_timer-int(self.between_rounds_timer))
            count = pygame.transform.smoothscale(count,list(map(Utils.round_int,[count.get_width()*sc,count.get_height()*sc])))

            self.surface.blit(count,(self.screen_size[0]/2-count.get_width()/2,self.screen_size[1]/2-count.get_height()/2))

        pygame.display.flip()