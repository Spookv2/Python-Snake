import pygame
from constants import *
from game import small_font
from game import font

def draw_text(screen, text, font, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def home_screen(screen):
    screen.fill(BLACK)
    draw_text(screen, "Snake Game", font, GREEN, WIDTH // 2 - 120, HEIGHT // 2 - 100)
    draw_text(screen, "1. Classic Mode", small_font, WHITE, WIDTH // 2 - 100, HEIGHT // 2 - 20)
    draw_text(screen, "2. Time Challenge Mode", small_font, WHITE, WIDTH // 2 - 140, HEIGHT // 2 + 20)
    draw_text(screen, "Press 1 or 2 to Start", small_font, WHITE, WIDTH // 2 - 130, HEIGHT // 2 + 60)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return CLASSIC_MODE
                elif event.key == pygame.K_2:
                    return TIME_CHALLENGE_MODE