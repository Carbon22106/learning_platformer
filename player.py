import pygame

pygame.init()

class Player():
    def __init__(self, x:int, y:int, w:int, h:int):
        # Constants
        self.PLAYER = "IMAGELOCATIONHERE"
        self.PLAYER_VEL = 5
        self.PLAYER_JUMP_STRENGTH = 15
        self.GRAVITY = 0.5

        #not constants
        self.playerChangeY = 0
        self.onGround = False

        self.playerRect = pygame.Rect(x, y, w, h)
        #self.playerRect = PLAYER.get_rect()

    def drawPlayer(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.playerRect)

    def playerMovement(self, keys, keys_justpressed):
        # gravity
        self.playerChangeY += self.GRAVITY
        self.playerRect.y += self.playerChangeY

        if keys[pygame.K_d]:
            self.playerRect.x += self.PLAYER_VEL
        if keys[pygame.K_a]:
            self.playerRect.x -= self.PLAYER_VEL
        if keys_justpressed[pygame.K_SPACE] and self.onGround:
            self.playerChangeY -= self.PLAYER_JUMP_STRENGTH

    def playerCollisions(self, Platforms):
        for i in Platforms:
            if self.playerRect.colliderect(i):
                self.playerChangeY = 0
                self.playerRect.bottom = i.top
                self.onGround = True
            if self.playerChangeY < 0:
                self.onGround = False

        print(self.onGround)