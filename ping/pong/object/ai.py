from ping.pong.util.setting import Setting

__all__ = ['AI']


class AI:
    def __init__(self, color, paddles, sound):
        self.score = 0
        self.sound = sound
        self.color = color
        self.paddles = list(paddles)

    def hit(self):
        if Setting.SOUND:
            self.sound.play()

    def add_score(self):
        self.score += 1
        if Setting.SOUND:
            self.sound.play()