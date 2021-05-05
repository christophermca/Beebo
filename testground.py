import pygame
from pygame.locals import QUIT

resolution = (1200, 1200)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

screen = pygame.display.set_mode(resolution)

while True:
    screen.fill(white)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
