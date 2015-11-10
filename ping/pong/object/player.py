from ping.pong.util.setting import Setting

__all__ = ['Player']


class Player:
    def __init__(self, color, paddles, sound_hit, sound_da_ding):
        self.score = 0
        self.sound_hit = sound_hit
        self.sound_da_ding = sound_da_ding
        self.color = color
        self.paddles = list(paddles)

    def hit(self):
        if Setting.SOUND:
            self.sound_hit.play()

    def add_score(self):
        self.score += 1
        if Setting.SOUND:
            self.sound_da_ding.play()
