import pygame
import random

# Initialize Pygame
pygame.init()

# Game Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 10
BALL_SIZE = 10
BRICK_WIDTH = 60
BRICK_HEIGHT = 20
ROWS_OF_BRICKS = 5
COLUMNS_OF_BRICKS = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Brick Breaker Game")

# Paddle
paddle = pygame.Rect(SCREEN_WIDTH // 2 - PADDLE_WIDTH // 2, SCREEN_HEIGHT - 40, PADDLE_WIDTH, PADDLE_HEIGHT)

# Ball
ball = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, BALL_SIZE, BALL_SIZE)
ball_speed = [5, -5]

# Bricks
bricks = []
for row in range(ROWS_OF_BRICKS):
    for col in range(COLUMNS_OF_BRICKS):
        brick = pygame.Rect(col * (BRICK_WIDTH + 10) + 35, row * (BRICK_HEIGHT + 10) + 50, BRICK_WIDTH, BRICK_HEIGHT)
        bricks.append(brick)

# Function to draw everything
def draw_objects():
    screen.fill(BLACK)
    pygame.draw.rect(screen, BLUE, paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    for brick in bricks:
        pygame.draw.rect(screen, RED, brick)
    pygame.display.flip()

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.move_ip(-10, 0)
    if keys[pygame.K_RIGHT] and paddle.right < SCREEN_WIDTH:
        paddle.move_ip(10, 0)
    
    # Ball movement
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]
    
    # Ball collision with walls
    if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
        ball_speed[0] = -ball_speed[0]
    if ball.top <= 0:
        ball_speed[1] = -ball_speed[1]
    
    # Ball collision with paddle
    if ball.colliderect(paddle):
        ball_speed[1] = -ball_speed[1]
    
    # Ball collision with bricks
    for brick in bricks[:]:
        if ball.colliderect(brick):
            ball_speed[1] = -ball_speed[1]
            bricks.remove(brick)
    
    # Ball falling below paddle (lose condition)
    if ball.bottom >= SCREEN_HEIGHT:
        print("You lose!")
        running = False
    
    # Win condition: All bricks cleared
    if not bricks:
        print("You win!")
        running = False
    
    # Draw all objects
    draw_objects()

# Quit Pygame
pygame.quit()