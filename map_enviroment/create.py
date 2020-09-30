from random import randrange
import numpy as np
bot = u'\u29BF'


def place_bbot(y, map_env):
    map_env[0][y] = -1
    return map_env


def set_item(x, y, map_env):
    map_env[x][y] = 2
    return map_env


def create_map(x, y):
    return np.ones((x, y))


if __name__ == '__main__':
    disq = 16

    def randr(max):
        return randrange(0, max)

    x = randr(disq)
    y = randr(disq)
    b = randr(disq)

    _map = create_map(disq, disq)
    final = set_item(x, y, _map)
    final = place_bbot(b, _map)

    print(x, y)
    print(final)
