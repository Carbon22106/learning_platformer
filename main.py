# # # © MASTERv22106, 2026. All rights reserved.

import pygame
import sys
from map import MapGen
import map
from player import Player


pygame.init()
pygame.mixer.init()

# Clock
clock = pygame.time.Clock()
FPS = 60

# screen and game conf
screenXY = 512
screen = pygame.display.set_mode((screenXY, screenXY))
#pygame.display.set_icon(pygame.image.load(""))
pygame.display.set_caption("My First Platformer Game")

# player
player = Player(25, 25, 50, 75)

# Map Generation
map = MapGen(map.level1, screen)
map.designLevel()
# functions


# quit
def QUIT_GAME():
    running = False
    pygame.quit()
    sys.exit()

def main():
    # Game Loop
    running = True
    while running:
        clock.tick(FPS)
        screen.fill((90, 160, 255))
        map.drawMap()
        #player.drawPlayer(screen)
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                QUIT_GAME()

        pygame.display.flip()

if __name__ == "__main__":
    main()