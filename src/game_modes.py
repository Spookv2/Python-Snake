import pygame
from constants import *
from game import Game
from home_screen import draw_text
from game import small_font
from game import font

def game_over(screen, score):
    screen.fill(BLACK)
    draw_text(screen, "Game Over!", font, RED, WIDTH // 2 - 100, HEIGHT // 2 - 50)
    draw_text(screen, f"Score: {score}", small_font, WHITE, WIDTH // 2 - 50, HEIGHT // 2)
    draw_text(screen, "Press R to Restart or Q to Quit", small_font, WHITE, WIDTH // 2 - 180, HEIGHT // 2 + 50)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return True  # Restart
                elif event.key == pygame.K_q:
                    return False  # Quit

def classic_mode(screen, clock):
    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and game.snake_direction != (0, CELL_SIZE):
                    game.snake_direction = (0, -CELL_SIZE)
                elif event.key == pygame.K_DOWN and game.snake_direction != (0, -CELL_SIZE):
                    game.snake_direction = (0, CELL_SIZE)
                elif event.key == pygame.K_LEFT and game.snake_direction != (CELL_SIZE, 0):
                    game.snake_direction = (-CELL_SIZE, 0)
                elif event.key == pygame.K_RIGHT and game.snake_direction != (-CELL_SIZE, 0):
                    game.snake_direction = (CELL_SIZE, 0)

        # Move snake
        game.move_snake()

        # Check for food collision
        if game.check_collision():
            game.snake.append(game.snake[-1])  # Grow the snake
            game.score += 10
            game.food = game.spawn_food()

        # Draw everything
        screen.fill(BLACK)
        game.draw_snake(screen)
        game.draw_food(screen)
        draw_text(screen, f"Score: {game.score}", small_font, WHITE, 10, 10)

        # Update display
        pygame.display.flip()

        # Control game speed
        clock.tick(10)

def time_challenge_mode(screen, clock):
    game = Game()
    time_left = 60  # 60 seconds

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and game.snake_direction != (0, CELL_SIZE):
                    game.snake_direction = (0, -CELL_SIZE)
                elif event.key == pygame.K_DOWN and game.snake_direction != (0, -CELL_SIZE):
                    game.snake_direction = (0, CELL_SIZE)
                elif event.key == pygame.K_LEFT and game.snake_direction != (CELL_SIZE, 0):
                    game.snake_direction = (-CELL_SIZE, 0)
                elif event.key == pygame.K_RIGHT and game.snake_direction != (-CELL_SIZE, 0):
                    game.snake_direction = (CELL_SIZE, 0)

        # Move snake
        game.move_snake()

        # Check for food collision
        if game.check_collision():
            game.snake.append(game.snake[-1])  # Grow the snake
            game.score += 10
            time_left += 5  # Add 5 seconds for each food eaten
            game.food = game.spawn_food()

        # Update timer
        time_left -= 1 / clock.get_fps()
        if time_left <= 0:
            if game_over(screen, game.score):
                return True  # Restart
            else:
                return False  # Quit

        # Draw everything
        screen.fill(BLACK)
        game.draw_snake(screen)
        game.draw_food(screen)
        draw_text(screen, f"Score: {game.score}", small_font, WHITE, 10, 10)
        draw_text(screen, f"Time: {int(time_left)}", small_font, WHITE, WIDTH - 150, 10)

        # Update display
        pygame.display.flip()

        # Control game speed
        clock.tick(10)