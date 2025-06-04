# 1 - Import packages
import pygame
from pygame.locals import * # pygame.locals: Gives you constants like QUIT, KEYDOWN, etc., without prefixing them (e.g., pygame.QUIT).
import sys
from pathlib import Path

# 2 - Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 1920/2
WINDOW_HEIGHT = 1080/2
FRAMES_PER_SECOND = 30

BASE_PATH = Path(__file__).resolve().parent
print(BASE_PATH)
pathToBall = BASE_PATH / 'images/ball.png'


# 3 - Initialize the world
pygame.init()   # pygame.init(): Initializes all Pygame modules.
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))     # display.set_mode(...): Creates the window with specified width and height.
clock = pygame.time.Clock()     #   pygame.time.Clock(): Used to control the frame rate (timing).


# 4 - Load assets: image(s), sound(s), etc.
ballImage = pygame.image.load(pathToBall)

# 5 - Initialize variables


# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get(): # pygame.event.get() gets all the events (like mouse clicks, key presses, window close, etc.) that have occurred since the last time it was called.
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    # 8 - Do any "per frame" actions
    window.fill(BLACK)
    pygame.display.update()


    # 9 - Clear the window
    clock.tick(FRAMES_PER_SECOND)

    # 10 - Draw all window elements
    # draw ball at position 100 across (x) and 200 down (y)
    window.blit(ballImage, (100, 200))


    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)