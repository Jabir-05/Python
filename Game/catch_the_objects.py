import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Falling Objects")

# Clock and font
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# Basket properties
basket_width = 100
basket_height = 20
basket_x = WIDTH // 2 - basket_width // 2
basket_y = HEIGHT - basket_height - 10
basket_speed = 10

# Object properties
object_width = 30
object_height = 30
object_x = random.randint(0, WIDTH - object_width)
object_y = 0
object_speed = 5

# Score
score = 0

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Basket movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket_x > 0:
        basket_x -= basket_speed
    if keys[pygame.K_RIGHT] and basket_x < WIDTH - basket_width:
        basket_x += basket_speed

    # Move the falling object
    object_y += object_speed

    # Check for collision
    if (
        basket_x < object_x + object_width and
        basket_x + basket_width > object_x and
        basket_y < object_y + object_height and
        basket_y + basket_height > object_y
    ):
        score += 1
        object_x = random.randint(0, WIDTH - object_width)
        object_y = 0

    # Reset object if it falls off screen
    if object_y > HEIGHT:
        object_x = random.randint(0, WIDTH - object_width)
        object_y = 0

    # Drawing everything
    screen.fill(WHITE)

    # Draw basket
    pygame.draw.rect(screen, BLUE, (basket_x, basket_y, basket_width, basket_height))

    # Draw falling object
    pygame.draw.rect(screen, RED, (object_x, object_y, object_width, object_height))

    # Draw score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Update display
    pygame.display.flip()

    # Frame rate
    clock.tick(30)

# Quit pygame
pygame.quit()
sys.exit()
