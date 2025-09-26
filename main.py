import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Window setup
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("UFO Reclaimer Prototype")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Load assets (placeholder rectangles for now)
PLAYER_SIZE = 50
ENEMY_SIZE = 40

# Player (UFO)
player = pygame.Rect(WIDTH // 2, HEIGHT - 100, PLAYER_SIZE, PLAYER_SIZE)

# Enemy list
enemies = []

# Game clock
clock = pygame.time.Clock()

# Font
font = pygame.font.SysFont("arial", 30)

# Movement speed
PLAYER_SPEED = 5
ENEMY_SPEED = 3

def spawn_enemy():
    x_pos = random.randint(0, WIDTH - ENEMY_SIZE)
    enemies.append(pygame.Rect(x_pos, 0, ENEMY_SIZE, ENEMY_SIZE))

def draw_window():
    WIN.fill((0, 0, 0))  # Black background
    # Draw text
    title = font.render("UFO Reclaimer Prototype", True, GREEN)
    WIN.blit(title, (20, 20))

    # Draw player (UFO = green square for now)
    pygame.draw.rect(WIN, GREEN, player)

    # Draw enemies (white squares)
    for enemy in enemies:
        pygame.draw.rect(WIN, WHITE, enemy)

    pygame.display.update()

def main():
    run = True
    spawn_timer = 0

    while run:
        clock.tick(60)  # 60 FPS

        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Player input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_SPEED > 0:
            player.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT] and player.x + PLAYER_SPEED < WIDTH - PLAYER_SIZE:
            player.x += PLAYER_SPEED
        if keys[pygame.K_UP] and player.y - PLAYER_SPEED > 0:
            player.y -= PLAYER_SPEED
        if keys[pygame.K_DOWN] and player.y + PLAYER_SPEED < HEIGHT - PLAYER_SIZE:
            player.y += PLAYER_SPEED

        # Spawn enemies
        spawn_timer += 1
        if spawn_timer > 50:
            spawn_enemy()
            spawn_timer = 0

        # Move enemies
        for enemy in enemies[:]:
            enemy.y += ENEMY_SPEED
            if enemy.y > HEIGHT:
                enemies.remove(enemy)

            # Collision check
            if player.colliderect(enemy):
                print("💥 Game Over!")
                run = False

        draw_window()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
