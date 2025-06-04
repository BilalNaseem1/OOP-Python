import pygame
from pygame.locals import * # pygame.locals: Gives you constants like QUIT, KEYDOWN, etc., without prefixing them (e.g., pygame.QUIT).
import sys

BLACK = (0, 0, 0)
WINDOW_WIDTH = 1920/2
WINDOW_HEIGHT = 1080/2
FRAMES_PER_SECOND = 30


pygame.init()   # pygame.init(): Initializes all Pygame modules.
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))     # display.set_mode(...): Creates the window with specified width and height.
clock = pygame.time.Clock()     #   pygame.time.Clock(): Used to control the frame rate (timing).

while True:
    for event in pygame.event.get(): # pygame.event.get() gets all the events (like mouse clicks, key presses, window close, etc.) that have occurred since the last time it was called.
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.fill(BLACK)
    pygame.display.update()

    clock.tick(FRAMES_PER_SECOND)