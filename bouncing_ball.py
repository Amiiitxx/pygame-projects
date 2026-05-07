import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 1000, 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball")

clock = pygame.time.Clock()

x = 100
y = 100

radius = 30

speed_x = 5
speed_y = 5

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    x += speed_x
    y += speed_y

    # Bounce left/right
    if x + radius >= WIDTH or x - radius <= 0:
        speed_x = -speed_x

    # Bounce top/bottom
    if y + radius >= HEIGHT or y - radius <= 0:
        speed_y = -speed_y

    screen.fill((30, 30, 30))

    pygame.draw.circle(screen, (0, 0,255), (x, y), radius)
 # Colors:
 # Red	(255, 0, 0)
 # Green	(0, 255, 0)
 # Blue	(0, 0, 255)
 # White	(255, 255, 255)
 # Black	(0, 0, 0)
 # Yellow	(255, 255, 0)

    pygame.display.update()

    clock.tick(60)

pygame.quit()
sys.exit()