import pygame
import sys

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("UFO Reclaimer - Prototype")

# Clock for framerate
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # black background

    # Draw placeholder text
    font = pygame.font.SysFont(None, 48)
    text = font.render("UFO Reclaimer Prototype Running...", True, (0, 255, 0))
    screen.blit(text, (50, 280))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
