import pygame
import random

# Initialize Pygame
pygame.init()

# Game constants
WIDTH, HEIGHT = 800, 600
BALL_SPEED = 5
PADDLE_SPEED = 10
BLOCK_WIDTH = 60
BLOCK_HEIGHT = 20
BLOCK_ROWS = 5
BLOCK_COLUMNS = 10

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Create the game window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Block Breaker Game")

# Create the paddle
paddle = pygame.Rect(WIDTH // 2 - 50, HEIGHT - 20, 100, 10)

# Create the ball
ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
ball_dx = BALL_SPEED
ball_dy = -BALL_SPEED

# Create blocks
blocks = []
for row in range(BLOCK_ROWS):
    for col in range(BLOCK_COLUMNS):
        block = pygame.Rect(col * (BLOCK_WIDTH + 5), row * (BLOCK_HEIGHT + 5), BLOCK_WIDTH, BLOCK_HEIGHT)
        blocks.append(block)

# Game loop
clock = pygame.time.Clock()
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.x -= PADDLE_SPEED
    if keys[pygame.K_RIGHT]:
        paddle.x += PADDLE_SPEED

    ball.x += ball_dx
    ball.y += ball_dy

    # Collisions with walls
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_dx = -ball_dx
    if ball.top <= 0:
        ball_dy = -ball_dy

    # Collisions with paddle
    if ball.colliderect(paddle) and ball_dy > 0:
        ball_dy = -ball_dy

    # Collisions with blocks
    for block in blocks:
        if ball.colliderect(block):
            blocks.remove(block)
            ball_dy = -ball_dy

    # Check game over
    if ball.bottom >= HEIGHT:
        game_over = True

    window.fill(WHITE)
    pygame.draw.rect(window, BLUE, paddle)
    pygame.draw.ellipse(window, RED, ball)
    for block in blocks:
        pygame.draw.rect(window, BLUE, block)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
