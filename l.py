import pygame
from map import Level
from map import Platform

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

level = Level()   # create map object

p1 = Platform(200, 150, 150, 120)
p2 = Platform(10, 280, 250, 120)
p3 = Platform(250, 450, 150, 120)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 30))
    level.draw(screen)
    Platform.draw(p1, screen)
    Platform.draw(p2, screen)
    Platform.draw(p3, screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
