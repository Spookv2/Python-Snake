import pygame
from constants import *
from home_screen import home_screen
from game_modes import classic_mode, time_challenge_mode

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock
clock = pygame.time.Clock()

# Main game loop
while True:
    game_state = home_screen(screen)

    if game_state == CLASSIC_MODE:
        if not classic_mode(screen, clock):
            break
    elif game_state == TIME_CHALLENGE_MODE:
        if not time_challenge_mode(screen, clock):
            break
    else:
        break

pygame.quit()