import pdb
import time
import curses
import threading
import pygame
from curses import wrapper
import Beebo
bot = u'\u29BF'
bot2 = u'\u29BE'
marked_bot = u'\u2B53'
t = None

def main(screen):
    runningTestGround = True
    curses.start_color()

    def __init__():
        beeb = Beebo.Beebo()
        print(beeb.get_status())
        screen.clear()

    def setup():
        # configure curses
        curses.curs_set(0)

        # colors
        curses.init_pair(1, curses.COLOR_WHITE, 0)
        curses.init_pair(2, curses.COLOR_RED, 0)
        curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLUE)
        curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_GREEN)
        curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_MAGENTA)

        screen.bkgd(curses.ACS_CKBOARD, curses.COLOR_BLACK)
        screen.noutrefresh()

        winu = curses.newwin(24, 64, 6, 10)
        winu.bkgd(curses.ACS_BOARD, curses.COLOR_RED)
        winu.noutrefresh()
        screen.refresh()

        return winu

    board = setup()

    board.addch(1, 3, marked_bot, curses.COLOR_RED)
    board.addch(1, 3, marked_bot, curses.color_pair(2))
    board.refresh()

    while runningTestGround:
        c = screen.getch()

        if c == ord('q'):
            print('ending')
            runningTestGround = False

    curses.endwin()


if __name__ == '__main__':
    wrapper(main)
