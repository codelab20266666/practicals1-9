"""Practical No. 8 - Simple obstacle game with Pygame.

Controls: Left/Right arrows to move, Space to jump, R to restart after
game over. Collect coins, avoid the dark obstacles.
"""
import sys

import pygame

pygame.init()

WIDTH, HEIGHT = 800, 500
GROUND_Y = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Practical 8 - Obstacle Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 32)


def make_obstacles():
    return [
        pygame.Rect(400, GROUND_Y - 35, 35, 35),
        pygame.Rect(650, GROUND_Y - 35, 35, 35),
    ]


def make_coins():
    return [
        pygame.Rect(250, GROUND_Y - 90, 20, 20),
        pygame.Rect(520, GROUND_Y - 100, 20, 20),
    ]


player = pygame.Rect(80, GROUND_Y - 50, 40, 50)
obstacles = make_obstacles()
coins = make_coins()

player_speed = 5
velocity_y = 0
gravity = 0.8
jump_power = -14
on_ground = True

score = 0
game_over = False
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and on_ground and not game_over:
                velocity_y = jump_power
                on_ground = False

            if event.key == pygame.K_r and game_over:
                player.x = 80
                player.y = GROUND_Y - 50
                velocity_y = 0
                on_ground = True
                score = 0
                game_over = False
                obstacles = make_obstacles()
                coins = make_coins()

    if not game_over:
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

    # Drawing
    screen.fill((135, 206, 235))
    pygame.draw.rect(
        screen, (60, 170, 70),
        (0, GROUND_Y, WIDTH, HEIGHT - GROUND_Y)
    )
    pygame.draw.rect(screen, (220, 50, 50), player)

    for obstacle in obstacles:
        pygame.draw.rect(screen, (40, 40, 40), obstacle)

    for coin in coins:
        pygame.draw.circle(screen, (255, 215, 0), coin.center, 10)

    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (20, 20))

    instruction = font.render("Arrows: Move | Space: Jump", True, (0, 0, 0))
    screen.blit(instruction, (20, 55))

    if game_over:
        message = font.render(
            "GAME OVER - Press R to Restart", True, (180, 0, 0)
        )
        screen.blit(message, (210, 220))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
