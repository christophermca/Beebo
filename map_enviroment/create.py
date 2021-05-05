from random import randrange
import numpy as np


def place_pkg():
    return [randr(dim_sq), randr(dim_sq), randr(dim_sq)]


def randr(max):
    return randrange(0, max)


def set_item(x, y, item, map_env):
    map_env[y][x] = item
    return map_env


def create_map(x, y):
    return np.ones((x, y))


# TODO move this to Beebo after testing


if __name__ == '__main__':
    dim_sq = 16
    _map = create_map(dim_sq, dim_sq)
    _pkg = 2
    x, y, bot = place_pkg()

    set_item(x, y, _pkg, _map)
    map_output = set_item(0, bot, -1, _map)

    # TODO move this to Beebo after testing
    # print(find_pkg(bot, _pkg, map_output))

    # print('item was placed at %d X %d' % (x, y))
    # print('BOT @ row %d' % (bot))
    # print('Map Environment: \n\n %s' % (map_output))
