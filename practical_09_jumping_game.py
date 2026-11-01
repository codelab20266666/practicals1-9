"""Practical No. 9 - Jumping game with Pygame (coins, obstacles, win state).

Controls: Left/Right arrows to move, Space to jump, R to restart after
game over or winning. Reach the right edge of the screen to win.
"""
import sys

import pygame

pygame.init()

# Screen settings
WIDTH = 800
HEIGHT = 500
GROUND_Y = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Practical 9 - Jumping Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 32)


def make_obstacles():
    return [
        pygame.Rect(350, GROUND_Y - 40, 40, 40),
        pygame.Rect(600, GROUND_Y - 40, 40, 40),
    ]


def make_coins():
    return [
        pygame.Rect(220, GROUND_Y - 80, 20, 20),
        pygame.Rect(480, GROUND_Y - 100, 20, 20),
        pygame.Rect(720, GROUND_Y - 80, 20, 20),
    ]


# Player
player = pygame.Rect(80, GROUND_Y - 50, 40, 50)
player_speed = 5
velocity_y = 0
gravity = 0.8
jump_power = -14
on_ground = True

obstacles = make_obstacles()
coins = make_coins()

score = 0
game_over = False
won = False
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_SPACE and on_ground
                    and not game_over and not won):
                velocity_y = jump_power
                on_ground = False

            if event.key == pygame.K_r and (game_over or won):
                player.x = 80
                player.y = GROUND_Y - 50
                velocity_y = 0
                on_ground = True
                score = 0
                game_over = False
                won = False
                obstacles = make_obstacles()
                coins = make_coins()

    if not game_over and not won:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.x -= player_speed
        if keys[pygame.K_RIGHT]:
            player.x += player_speed

        player.clamp_ip(screen.get_rect())

        # Jumping and gravity
        velocity_y += gravity
        player.y += int(velocity_y)

        if player.bottom >= GROUND_Y:
            player.bottom = GROUND_Y
            velocity_y = 0
            on_ground = True

        # Obstacle collision
        for obstacle in obstacles:
            if player.colliderect(obstacle):
                game_over = True

        # Coin collection
        for coin in coins[:]:
            if player.colliderect(coin):
                coins.remove(coin)
                score += 10

        # Winning condition
        if player.right >= WIDTH - 20:
            won = True

    # Draw background
    screen.fill((135, 206, 235))

    # Draw ground
    pygame.draw.rect(
        screen, (50, 170, 70),
        (0, GROUND_Y, WIDTH, HEIGHT - GROUND_Y)
    )

    # Draw player
    pygame.draw.rect(screen, (220, 40, 40), player)

    # Draw obstacles
    for obstacle in obstacles:
        pygame.draw.rect(screen, (40, 40, 40), obstacle)

    # Draw coins
    for coin in coins:
        pygame.draw.circle(screen, (255, 215, 0), coin.center, 10)

    # Display score and instructions
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (20, 20))

    instruction = font.render(
        "Arrow Keys: Move | Space: Jump", True, (0, 0, 0)
    )
    screen.blit(instruction, (20, 55))

    # Game over message
    if game_over:
        message = font.render(
            "GAME OVER! Press R to Restart", True, (180, 0, 0)
        )
        screen.blit(message, (200, 220))

    # Winning message
    if won:
        message = font.render(
            "YOU WIN! Press R to Play Again", True, (0, 100, 0)
        )
        screen.blit(message, (200, 220))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
