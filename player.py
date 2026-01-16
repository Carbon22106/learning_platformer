import pygame


class Player():
    def __init__(self, x:int, y:int, w:int, h:int):
        self.playerRect = pygame.Rect(x, y, w, h)

    def drawPlayer(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.playerRect)

