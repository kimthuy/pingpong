import pygame
from ping.pong.object.player import Player
from ping.pong.object.paddle import Paddle
from ping.pong.object.ball import Ball
from ping.pong.util import Utils
from ping.pong.screen.base_screen import *
from ping.pong.util.setting import *

__all__ = ['GameScreen']


class GameScreen(BaseScreen):

    def __init__(self, base_game, screen_size, surface):
        BaseScreen.__init__(self)
        # BaseScreen.__init__(self)
        self.base_game = base_game
        self.surface = surface
        self.dt = 1.0/60.0
        self.balls = []
        self.screen_size = screen_size
        self.stop = False

    def init_screen(self):

        self.sounds = {
            'ping': pygame.mixer.Sound(Utils.get_path('sound/click.wav')),
            'click': pygame.mixer.Sound(Utils.get_path('sound/paddle-hit.wav')),
            'da-ding': pygame.mixer.Sound(Utils.get_path('sound/da-ding.wav'))
        }
        self.sounds['ping'].set_volume(0.05)
        self.sounds['click'].set_volume(0.5)
        self.sounds['da-ding'].set_volume(0.5)
        self.bg = pygame.image.load(Utils.get_path('image/pingpong-table.png'))
        self.font = {
            18: pygame.font.SysFont('Times New Roman', 18),
            72: pygame.font.SysFont('Times New Roman', 72)
        }

        up_key = pygame.K_w
        down_key = pygame.K_s
        if Setting.PLAY_MODE == Setting.SINGLE_MODE:
            up_key = None
            down_key = None

        paddle_1 = Paddle(5, self.screen_size[1]/2-30, 10, 60, None, None, down_key, up_key, self.surface, self.dt, self.screen_size)
        paddle_2 = Paddle(self.screen_size[0]-5-10, self.screen_size[1]/2-30, 10, 60, None, None, pygame.K_DOWN, pygame.K_UP, self.surface, self.dt, self.screen_size)

        self.paddles = [paddle_1, paddle_2]

        player_1 = Player((0, 255, 0), self.paddles[:1], self.sounds['click'], self.sounds['da-ding'])
        player_2 = Player((247, 52, 12), self.paddles[1:], self.sounds['click'], self.sounds['da-ding'])

        self.players = [player_1, player_2]

        self.ball = Ball(self.screen_size[0]/2, self.screen_size[1]/2,200.0, self.surface)

    def play(self):
        clock = pygame.time.Clock()
        while True:
            if not self.get_input() or  self.stop:
                break
            self.update()
            self.move()
            if Setting.PLAY_MODE == Setting.SINGLE_MODE:
                self.ai_move()
            self.draw()
            clock.tick(60)
            self.dt = 1.0/Utils.clamp(clock.get_fps(), 30, 90)

    def get_input(self):
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_BACKSPACE:
                    Setting.between_rounds_timer = 3.0
                    self.balls = []
                    self.base_game.switch_screen(Setting.MENU_SCREEN)
                    return False
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
            for subs_tep in range(10):
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
                    self.play_sound(self.sounds['ping'])
                elif ball.pos[1] > self.screen_size[1]:
                    ball.pos[1] = self.screen_size[1]
                    ball.speed[1] *= -1
                    self.play_sound(self.sounds['ping'])
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
                            self.sounds['click'].play()
                            ball.speed_up()

            if not removed:
                balls2.append(ball)

        if len(balls2) == 0 and len(self.balls) > 0:
            Setting.between_rounds_timer = 3.0

        self.balls = balls2
        if len(self.balls) == 0:
            Setting.between_rounds_timer -= self.dt
            if Setting.between_rounds_timer < 0:
                self.balls.append(Ball(self.screen_size[0]/2, self.screen_size[1]/2,200.0, self.surface))

    def draw(self):
        self.surface.blit(self.bg, (0, 0))

        for ball in self.balls:
            ball.draw()
        for player in self.players:
            for paddle in player.paddles:
                paddle.draw(player.color)

        p1_score_text = self.font[18].render('Score '+str(self.players[0].score), True, (255, 255, 255))
        p2_score_text = self.font[18].render('Score '+str(self.players[1].score), True, (255, 255, 255))
        self.surface.blit(p1_score_text, (20, 20))
        self.surface.blit(p2_score_text, (self.screen_size[0]-p2_score_text.get_width()-20, 20))

        if Setting.between_rounds_timer > 0:
            alpha = Setting.between_rounds_timer - int(Setting.between_rounds_timer)
            alpha = Utils.round_int(255*alpha)

            count = self.font[72].render(str(int(Setting.between_rounds_timer)+1),True,(alpha,alpha,alpha))

            sc = 0.5*(1.0 + Setting.between_rounds_timer-int(Setting.between_rounds_timer))
            count = pygame.transform.smoothscale(count,list(map(Utils.round_int,[count.get_width()*sc,count.get_height()*sc])))

            self.surface.blit(count,(self.screen_size[0]/2-count.get_width()/2,self.screen_size[1]/2-count.get_height()/2))

        pygame.display.flip()