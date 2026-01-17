import pygame

pygame.init()

# 0 = air
# 1 = solid platform

tileSize = 32

level1 = [
2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0,
1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
]

class MapGen:
    def __init__(self, Level, Screen):
        self.level = Level
        self.screen = Screen
        self.screenSize = Screen.get_size()[0]

    def designLevel(self):
        self.platforms = []
        self.clouds = []

        for i, v in enumerate(self.level): # i = index, v = value
            x = (i % 16) * tileSize
            y = (i // 16) * tileSize
            if v == 1:
                self.platforms.append(pygame.Rect(x, y, tileSize, tileSize))
            if v == 2:
                self.clouds.append(pygame.Rect(x, y, tileSize, tileSize))


    def drawMap(self):
        for cloud in self.clouds: # i becomes the coluds
            pygame.draw.rect(self.screen, (225, 225, 225), cloud)

        for platform in self.platforms: # i becomes the platform
            pygame.draw.rect(self.screen, (110, 110, 110), platform)