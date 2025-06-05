# pygame demo 3(b) - one image, continuous mode, move as long as a key is down

import pygame
from pygame.locals import *
import sys
import random

# Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
BALL_WIDTH_HEIGHT = 100
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT

TARGET_X = 400
TARGET_Y = 320
TARGET_WIDTH_HEIGHT = 120
N_PIXELS_TO_MOVE = 3

# Initialize pygame
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# Load images
ballImage = pygame.image.load('images/ball.png')
targetImage = pygame.image.load('images/target.jpg')

# Initialize ball position randomly within bounds
ballX = random.randrange(MAX_WIDTH)
ballY = random.randrange(MAX_HEIGHT)

# Create target rectangle
targetRect = pygame.Rect(TARGET_X, TARGET_Y, TARGET_WIDTH_HEIGHT, TARGET_WIDTH_HEIGHT)

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Poll keyboard state for continuous movement
    keyPressedTuple = pygame.key.get_pressed()

    if keyPressedTuple[pygame.K_LEFT]:
        ballX = max(0, ballX - N_PIXELS_TO_MOVE)  # Prevent moving out of window
    if keyPressedTuple[pygame.K_RIGHT]:
        ballX = min(MAX_WIDTH, ballX + N_PIXELS_TO_MOVE)
    if keyPressedTuple[pygame.K_UP]:
        ballY = max(0, ballY - N_PIXELS_TO_MOVE)
    if keyPressedTuple[pygame.K_DOWN]:
        ballY = min(MAX_HEIGHT, ballY + N_PIXELS_TO_MOVE)

    # Check collision with target
    ballRect = pygame.Rect(ballX, ballY, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)
    if ballRect.colliderect(targetRect):
        print('Ball is touching the target')

    # Clear screen
    window.fill(BLACK)

    # Draw target and ball
    window.blit(targetImage, (TARGET_X, TARGET_Y))
    window.blit(ballImage, (ballX, ballY))

    # Update display
    pygame.display.update()

    # Maintain frame rate
    clock.tick(FRAMES_PER_SECOND)
