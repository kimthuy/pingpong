__all__ = ['Utils']


class Utils:
    @staticmethod
    def round_int(x):
        return int(round(x))

    @staticmethod
    def clamp(x, minimum, maximum):
        return min(max(x, minimum), maximum)