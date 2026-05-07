import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Multiple Balls")

clock = pygame.time.Clock()

balls = []

# Create 5 balls
for i in range(5):

    ball = {
        "x": random.randint(100, 700),
        "y": random.randint(100, 500),
        "radius": random.randint(20, 50),

        "speed_x": random.choice([-5, 5]),
        "speed_y": random.choice([-5, 5]),

        "color": (
            random.randint(0,255),
            random.randint(0,255),
            random.randint(0,255)
        )
    }

    balls.append(ball)

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((20, 20, 20))

    for ball in balls:

        ball["x"] += ball["speed_x"]
        ball["y"] += ball["speed_y"]

        # Bounce walls
        if ball["x"] + ball["radius"] >= WIDTH or ball["x"] - ball["radius"] <= 0:
            ball["speed_x"] = -ball["speed_x"]

        if ball["y"] + ball["radius"] >= HEIGHT or ball["y"] - ball["radius"] <= 0:
            ball["speed_y"] = -ball["speed_y"]

        pygame.draw.circle(
            screen,
            ball["color"],
            (ball["x"], ball["y"]),
            ball["radius"]
        )

    pygame.display.update()

    clock.tick(60)

pygame.quit()
sys.exit()