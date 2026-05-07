import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Box")

clock = pygame.time.Clock()

x = 100
y = 100
speed = 5

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= speed

    if keys[pygame.K_RIGHT]:
        x += speed

    if keys[pygame.K_UP]:
        y -= speed

    if keys[pygame.K_DOWN]:
        y += speed

    screen.fill((30, 30, 30))

    pygame.draw.rect(screen, (0, 255, 0), (x, y, 100, 100))

    pygame.display.update()

    clock.tick(60)

pygame.quit()
sys.exit()