from os import path, getcwd

__all__ = ['Utils']


class Utils:
    @staticmethod
    def round_int(x):
        return int(round(x))

    @staticmethod
    def clamp(x, minimum, maximum):
        return min(max(x, minimum), maximum)

    @staticmethod
    def get_path(file):
        return path.join(getcwd(), 'media', file)