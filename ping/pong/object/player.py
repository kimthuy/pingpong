
__all__ = ['Player']


class Player:
    def __init__(self, color, paddles, sound):
        self.score = 0
        self.sound = sound
        self.color = color
        self.paddles = list(paddles)

    def hit(self):
        self.sound.play()

    def add_score(self):
        self.score += 1
        self.sound.play()
